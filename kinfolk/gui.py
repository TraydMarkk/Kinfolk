"""
Kinfolk GTK4/Adwaita GUI
Main application window with three-panel layout for Werewolf: The Apocalypse
"""

import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, Gio, GLib

import os
from .character import Character
from .data import (
    ATTRIBUTES, PRIMARY_ABILITIES, SECONDARY_ABILITIES,
    BACKGROUNDS, BREEDS, AUSPICES, TRIBES, FORMS,
    BREED_GIFTS, AUSPICE_GIFTS, TRIBE_GIFTS,
    WYRMISH_BREED_GIFTS, WYRMISH_AUSPICE_GIFTS,
    ARCHETYPES, MERITS, FLAWS,
    CREATION_RULES, FREEBIE_COSTS, EXPERIENCE_COSTS, CONCEPTS, RENOWN_TYPES,
    CHANGING_BREEDS
)


class DotRating(Gtk.Box):
    """Widget for displaying/editing dot ratings (1-5 or 1-10)."""
    
    def __init__(self, max_dots: int = 5, current: int = 0, min_dots: int = 0,
                 on_change=None, editable: bool = True):
        super().__init__(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
        
        self.max_dots = max_dots
        self.min_dots = min_dots
        self.current = current
        self.on_change = on_change
        self.editable = editable
        self.buttons = []
        
        for i in range(max_dots):
            btn = Gtk.Button()
            btn.set_has_frame(False)
            btn.add_css_class("dot-button")
            btn.set_size_request(20, 20)
            btn.connect("clicked", self._on_dot_clicked, i + 1)
            if not editable:
                btn.set_sensitive(False)
            self.buttons.append(btn)
            self.append(btn)
        
        self._update_display()
    
    def _on_dot_clicked(self, button, dot_num):
        if not self.editable:
            return
        
        if dot_num == self.current:
            new_val = max(self.min_dots, dot_num - 1)
        else:
            new_val = max(self.min_dots, dot_num)
        
        self.set_value(new_val)
    
    def _update_display(self):
        for i, btn in enumerate(self.buttons):
            if i < self.current:
                btn.set_label("●")
                btn.add_css_class("dot-filled")
                btn.remove_css_class("dot-empty")
            else:
                btn.set_label("○")
                btn.add_css_class("dot-empty")
                btn.remove_css_class("dot-filled")
    
    def set_value(self, value: int):
        old_value = self.current
        self.current = max(self.min_dots, min(value, self.max_dots))
        self._update_display()
        if self.on_change and old_value != self.current:
            self.on_change(self.current)
    
    def get_value(self) -> int:
        return self.current
    
    def set_editable(self, editable: bool):
        self.editable = editable
        for btn in self.buttons:
            btn.set_sensitive(editable)


class TraitRow(Gtk.Box):
    """Row widget for a single trait with label and dot rating."""
    
    def __init__(self, name: str, max_dots: int = 5, current: int = 0,
                 min_dots: int = 0, on_change=None, editable: bool = True,
                 show_specialty: bool = False, on_specialty_change=None):
        super().__init__(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        self.set_hexpand(True)
        
        self.name = name
        self.on_change = on_change
        self.on_specialty_change = on_specialty_change
        
        label = Gtk.Label(label=name)
        label.set_xalign(0)
        label.set_hexpand(True)
        label.set_width_chars(15)
        self.append(label)
        
        self.specialty_entry = None
        if show_specialty:
            self.specialty_entry = Gtk.Entry()
            self.specialty_entry.set_placeholder_text("Specialty")
            self.specialty_entry.set_width_chars(12)
            if on_specialty_change:
                self.specialty_entry.connect("changed", self._on_specialty_changed)
            self.append(self.specialty_entry)
        
        self.dots = DotRating(max_dots, current, min_dots, 
                             self._on_dots_changed, editable)
        self.append(self.dots)
    
    def _on_dots_changed(self, value):
        if self.on_change:
            self.on_change(self.name, value)
    
    def _on_specialty_changed(self, entry):
        if self.on_specialty_change:
            text = entry.get_text().strip()
            self.on_specialty_change(self.name, text)
    
    def set_value(self, value: int):
        self.dots.set_value(value)
    
    def get_value(self) -> int:
        return self.dots.get_value()
    
    def set_specialty(self, specialty: str):
        """Set the specialty text."""
        if self.specialty_entry:
            self.specialty_entry.set_text(specialty)
    
    def get_specialty(self) -> str:
        """Get the specialty text."""
        if self.specialty_entry:
            return self.specialty_entry.get_text().strip()
        return ""


class CharacterEditor(Gtk.Box):
    """Main character editing panel."""
    
    def __init__(self, app):
        super().__init__(orientation=Gtk.Orientation.VERTICAL)
        self.app = app
        self.character = None
        self.trait_widgets = {}
        self._updating = False
        self.garou_sections = []  # Track Garou-specific sections
        
        scrolled = Gtk.ScrolledWindow()
        scrolled.set_vexpand(True)
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        
        content = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=16)
        content.set_margin_start(16)
        content.set_margin_end(16)
        content.set_margin_top(16)
        content.set_margin_bottom(16)
        
        # Build sections
        content.append(self._create_identity_section())
        content.append(Gtk.Separator())
        content.append(self._create_attributes_section())
        content.append(Gtk.Separator())
        content.append(self._create_abilities_section())
        content.append(Gtk.Separator())
        
        # Changing breed-specific sections (wrapped for toggling)
        self.garou_wrapper = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=16)
        self.purchased_gifts_section = self._create_purchased_gifts_section()
        self.garou_wrapper.append(self.purchased_gifts_section)
        self.garou_wrapper.append(Gtk.Separator())
        # Store forms section reference for dynamic updates
        self.forms_section = self._create_forms_section()
        self.garou_wrapper.append(self.forms_section)
        self.garou_wrapper.append(Gtk.Separator())
        self.garou_wrapper.append(self._create_backgrounds_section())
        self.garou_wrapper.append(Gtk.Separator())
        self.garou_wrapper.append(self._create_core_traits_section())
        self.garou_wrapper.append(Gtk.Separator())
        self.garou_wrapper.append(self._create_renown_section())
        content.append(self.garou_wrapper)
        
        content.append(Gtk.Separator())
        content.append(self._create_merits_flaws_section())
        content.append(Gtk.Separator())
        content.append(self._create_notes_section())
        
        scrolled.set_child(content)
        self.append(scrolled)
    
    def _create_section_header(self, title: str) -> Gtk.Label:
        label = Gtk.Label(label=title)
        label.add_css_class("title-2")
        label.set_xalign(0)
        label.set_margin_top(8)
        label.set_margin_bottom(4)
        return label
    
    def _create_identity_section(self) -> Gtk.Box:
        section = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        section.append(self._create_section_header("Identity"))
        
        # Character Type dropdown (for changing breeds support)
        type_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        type_label = Gtk.Label(label="Character Type:")
        type_label.set_width_chars(15)
        type_label.set_xalign(0)
        self.character_type_combo = Gtk.ComboBoxText()
        for breed_key, breed_data in CHANGING_BREEDS.items():
            self.character_type_combo.append_text(breed_data["display_name"])
        self.character_type_combo.set_active(0)  # Default to Garou
        self.character_type_combo.connect("changed", self._on_character_type_changed)
        type_box.append(type_label)
        type_box.append(self.character_type_combo)
        section.append(type_box)
        
        # Name row
        name_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        name_label = Gtk.Label(label="Name:")
        name_label.set_width_chars(12)
        name_label.set_xalign(0)
        self.name_entry = Gtk.Entry()
        self.name_entry.set_hexpand(True)
        self.name_entry.connect("changed", self._on_identity_changed, "name")
        name_box.append(name_label)
        name_box.append(self.name_entry)
        section.append(name_box)
        
        # Player and Chronicle
        row1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=16)
        
        player_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        player_label = Gtk.Label(label="Player:")
        player_label.set_width_chars(12)
        player_label.set_xalign(0)
        self.player_entry = Gtk.Entry()
        self.player_entry.set_hexpand(True)
        self.player_entry.connect("changed", self._on_identity_changed, "player")
        player_box.append(player_label)
        player_box.append(self.player_entry)
        player_box.set_hexpand(True)
        row1.append(player_box)
        
        chron_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        chron_label = Gtk.Label(label="Chronicle:")
        chron_label.set_width_chars(12)
        chron_label.set_xalign(0)
        self.chronicle_entry = Gtk.Entry()
        self.chronicle_entry.set_hexpand(True)
        self.chronicle_entry.connect("changed", self._on_identity_changed, "chronicle")
        chron_box.append(chron_label)
        chron_box.append(self.chronicle_entry)
        chron_box.set_hexpand(True)
        row1.append(chron_box)
        
        section.append(row1)
        
        # Concept
        concept_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        concept_label = Gtk.Label(label="Concept:")
        concept_label.set_width_chars(12)
        concept_label.set_xalign(0)
        self.concept_combo = Gtk.ComboBoxText()
        self.concept_combo.set_entry_text_column(0)
        self.concept_combo.append_text("")
        for concept in CONCEPTS:
            self.concept_combo.append_text(concept)
        self.concept_combo.set_hexpand(True)
        self.concept_combo.connect("changed", self._on_identity_changed, "concept")
        concept_box.append(concept_label)
        concept_box.append(self.concept_combo)
        section.append(concept_box)
        
        # Breed, Auspice, and Tribe (Garou-specific)
        self.breed_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=16)
        
        breed_inner = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        breed_label = Gtk.Label(label="Breed:")
        breed_label.set_width_chars(12)
        breed_label.set_xalign(0)
        self.breed_combo = Gtk.ComboBoxText()
        self.breed_combo.append_text("")
        for breed in BREEDS.keys():
            self.breed_combo.append_text(breed)
        self.breed_combo.set_hexpand(True)
        self.breed_combo.connect("changed", self._on_breed_changed)
        breed_inner.append(breed_label)
        breed_inner.append(self.breed_combo)
        breed_inner.set_hexpand(True)
        self.breed_box.append(breed_inner)
        
        auspice_inner = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        auspice_label = Gtk.Label(label="Auspice:")
        auspice_label.set_width_chars(12)
        auspice_label.set_xalign(0)
        self.auspice_combo = Gtk.ComboBoxText()
        self.auspice_combo.append_text("")
        for auspice in AUSPICES.keys():
            self.auspice_combo.append_text(auspice)
        self.auspice_combo.set_hexpand(True)
        self.auspice_combo.connect("changed", self._on_auspice_changed)
        auspice_inner.append(auspice_label)
        auspice_inner.append(self.auspice_combo)
        auspice_inner.set_hexpand(True)
        self.breed_box.append(auspice_inner)
        
        section.append(self.breed_box)
        
        # Tribe
        tribe_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        tribe_label = Gtk.Label(label="Tribe:")
        tribe_label.set_width_chars(12)
        tribe_label.set_xalign(0)
        self.tribe_combo = Gtk.ComboBoxText()
        self.tribe_combo.append_text("")
        for tribe in TRIBES.keys():
            self.tribe_combo.append_text(tribe)
        self.tribe_combo.set_hexpand(True)
        self.tribe_combo.connect("changed", self._on_tribe_changed)
        tribe_box.append(tribe_label)
        tribe_box.append(self.tribe_combo)
        section.append(tribe_box)
        
        # Metis deformity (only shown for Metis)
        self.deformity_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        deformity_label = Gtk.Label(label="Deformity:")
        deformity_label.set_width_chars(12)
        deformity_label.set_xalign(0)
        self.deformity_combo = Gtk.ComboBoxText()
        self.deformity_combo.set_hexpand(True)
        self.deformity_combo.connect("changed", self._on_deformity_changed)
        self.deformity_box.append(deformity_label)
        self.deformity_box.append(self.deformity_combo)
        self.deformity_box.set_visible(False)
        section.append(self.deformity_box)
        
        # Nature and Demeanor
        arch_row = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=16)
        
        nature_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        nature_label = Gtk.Label(label="Nature:")
        nature_label.set_width_chars(12)
        nature_label.set_xalign(0)
        self.nature_combo = Gtk.ComboBoxText()
        self.nature_combo.append_text("")
        for archetype in ARCHETYPES.keys():
            self.nature_combo.append_text(archetype)
        self.nature_combo.set_hexpand(True)
        self.nature_combo.connect("changed", self._on_identity_changed, "nature")
        nature_box.append(nature_label)
        nature_box.append(self.nature_combo)
        nature_box.set_hexpand(True)
        arch_row.append(nature_box)
        
        demeanor_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        demeanor_label = Gtk.Label(label="Demeanor:")
        demeanor_label.set_width_chars(12)
        demeanor_label.set_xalign(0)
        self.demeanor_combo = Gtk.ComboBoxText()
        self.demeanor_combo.append_text("")
        for archetype in ARCHETYPES.keys():
            self.demeanor_combo.append_text(archetype)
        self.demeanor_combo.set_hexpand(True)
        self.demeanor_combo.connect("changed", self._on_identity_changed, "demeanor")
        demeanor_box.append(demeanor_label)
        demeanor_box.append(self.demeanor_combo)
        demeanor_box.set_hexpand(True)
        arch_row.append(demeanor_box)
        
        section.append(arch_row)
        
        return section
    
    def _on_character_type_changed(self, widget):
        """Handle character type change - update breed/auspice/tribe dropdowns."""
        if self._updating:
            return
        
        char_type_display = widget.get_active_text() or ""
        # Find the breed key from display name
        char_type = "Garou"  # Default
        for breed_key, breed_data in CHANGING_BREEDS.items():
            if breed_data["display_name"] == char_type_display:
                char_type = breed_key
                break
        
        breed_data = CHANGING_BREEDS.get(char_type, CHANGING_BREEDS["Garou"])
        is_garou = (char_type == "Garou")
        
        # Show/hide changing breed-specific sections (visible for all breeds)
        self.garou_wrapper.set_visible(True)  # Always show for all changing breeds
        self.breed_box.set_visible(True)  # Always show breed/auspice/tribe
        
        # Rebuild forms section for the new character type
        self._rebuild_forms_section(char_type)
        
        # Update character type
        if self.character:
            self.character.character_type = char_type
        
        # Update breed dropdown
        self.breed_combo.remove_all()
        self.breed_combo.append_text("")
        if breed_data.get("breeds"):
            for breed in breed_data["breeds"].keys():
                self.breed_combo.append_text(breed)
        
        # Update auspice dropdown
        self.auspice_combo.remove_all()
        self.auspice_combo.append_text("")
        if breed_data.get("auspices"):
            for auspice in breed_data["auspices"].keys():
                self.auspice_combo.append_text(auspice)
        elif is_garou:
            # Fallback to Garou auspices
            for auspice in AUSPICES.keys():
                self.auspice_combo.append_text(auspice)
        
        # Update tribe dropdown
        self.tribe_combo.remove_all()
        self.tribe_combo.append_text("")
        if breed_data.get("tribes"):
            for tribe in breed_data["tribes"].keys():
                self.tribe_combo.append_text(tribe)
        elif is_garou:
            # Fallback to Garou tribes
            for tribe in TRIBES.keys():
                self.tribe_combo.append_text(tribe)
        
        # Update renown types if character exists
        if self.character:
            renown_types = breed_data.get("renown_types", ["Glory", "Honor", "Wisdom"])
            # Initialize renown dict with new types
            new_renown = {}
            for renown_type in renown_types:
                new_renown[renown_type] = self.character.renown.get(renown_type, 0)
            self.character.renown = new_renown
            self._update_renown_display()
        
        # Clear selections when changing type
        self.breed_combo.set_active(0)
        self.auspice_combo.set_active(0)
        self.tribe_combo.set_active(0)
    
    def _create_attributes_section(self) -> Gtk.Box:
        section = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        section.append(self._create_section_header("Attributes"))
        
        # Priority selection
        priority_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=16)
        priority_label = Gtk.Label(label="Priorities:")
        priority_label.set_margin_end(8)
        priority_box.append(priority_label)
        
        self.attr_priority_combos = {}
        priorities = ["", "primary", "secondary", "tertiary"]
        
        for category in ["Physical", "Social", "Mental"]:
            cat_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=4)
            cat_label = Gtk.Label(label=f"{category}:")
            combo = Gtk.ComboBoxText()
            for p in priorities:
                combo.append_text(p.capitalize() if p else "—")
            combo.set_active(0)
            combo.connect("changed", self._on_attr_priority_changed, category)
            self.attr_priority_combos[category] = combo
            cat_box.append(cat_label)
            cat_box.append(combo)
            priority_box.append(cat_box)
        
        section.append(priority_box)
        
        # Attribute rows in columns
        attr_grid = Gtk.Grid()
        attr_grid.set_column_spacing(32)
        attr_grid.set_row_spacing(4)
        
        col = 0
        for category, attrs in ATTRIBUTES.items():
            header = Gtk.Label(label=category.upper())
            header.add_css_class("heading")
            header.set_margin_bottom(4)
            attr_grid.attach(header, col, 0, 1, 1)
            
            for row, attr in enumerate(attrs, 1):
                trait_row = TraitRow(attr, 5, 1, 1, self._on_attribute_changed,
                                    show_specialty=True, on_specialty_change=self._on_attribute_specialty_changed)
                self.trait_widgets[f"attr_{attr}"] = trait_row
                attr_grid.attach(trait_row, col, row, 1, 1)
            
            col += 1
        
        section.append(attr_grid)
        return section
    
    def _create_abilities_section(self) -> Gtk.Box:
        section = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        section.append(self._create_section_header("Abilities"))
        
        # Priority selection
        priority_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=16)
        priority_label = Gtk.Label(label="Priorities:")
        priority_label.set_margin_end(8)
        priority_box.append(priority_label)
        
        self.ability_priority_combos = {}
        priorities = ["", "primary", "secondary", "tertiary"]
        
        for category in ["Talents", "Skills", "Knowledges"]:
            cat_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=4)
            cat_label = Gtk.Label(label=f"{category}:")
            combo = Gtk.ComboBoxText()
            for p in priorities:
                combo.append_text(p.capitalize() if p else "—")
            combo.set_active(0)
            combo.connect("changed", self._on_ability_priority_changed, category)
            self.ability_priority_combos[category] = combo
            cat_box.append(cat_label)
            cat_box.append(combo)
            priority_box.append(cat_box)
        
        section.append(priority_box)
        
        # Create notebook for Primary/Secondary abilities
        notebook = Gtk.Notebook()
        
        primary_box = self._create_abilities_grid(PRIMARY_ABILITIES, "primary")
        notebook.append_page(primary_box, Gtk.Label(label="Primary Abilities"))
        
        secondary_box = self._create_abilities_grid(SECONDARY_ABILITIES, "secondary")
        notebook.append_page(secondary_box, Gtk.Label(label="Secondary Abilities"))
        
        section.append(notebook)
        return section
    
    def _create_abilities_grid(self, abilities_dict: dict, prefix: str) -> Gtk.Box:
        container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        container.set_margin_top(8)
        container.set_margin_bottom(8)
        
        grid = Gtk.Grid()
        grid.set_column_spacing(32)
        grid.set_row_spacing(4)
        
        col = 0
        for category, abilities in abilities_dict.items():
            header = Gtk.Label(label=category.upper())
            header.add_css_class("heading")
            header.set_margin_bottom(4)
            grid.attach(header, col, 0, 1, 1)
            
            for row, ability in enumerate(abilities, 1):
                trait_row = TraitRow(ability, 5, 0, 0, self._on_ability_changed, 
                                    show_specialty=True, on_specialty_change=self._on_ability_specialty_changed)
                self.trait_widgets[f"ability_{ability}"] = trait_row
                grid.attach(trait_row, col, row, 1, 1)
            
            col += 1
        
        container.append(grid)
        return container
    
    def _create_purchased_gifts_section(self) -> Gtk.Box:
        """Create section showing purchased gifts with a button to purchase more."""
        section = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        section.append(self._create_section_header("Gifts"))
        
        # Purchase Gifts button
        purchase_btn = Gtk.Button(label="Purchase Gifts")
        purchase_btn.add_css_class("suggested-action")
        purchase_btn.connect("clicked", self._on_purchase_gifts_clicked)
        section.append(purchase_btn)
        
        # Purchased gifts display
        self.purchased_gifts_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        self.purchased_gifts_box.set_margin_start(8)
        self.purchased_gifts_box.set_margin_end(8)
        section.append(self.purchased_gifts_box)
        
        return section
    
    def _update_purchased_gifts_display(self):
        """Update the display of purchased gifts."""
        # Clear existing display
        while child := self.purchased_gifts_box.get_first_child():
            self.purchased_gifts_box.remove(child)
        
        if not self.character or not self.character.gifts:
            no_gifts_label = Gtk.Label(label="No gifts purchased yet.")
            no_gifts_label.add_css_class("dim-label")
            no_gifts_label.set_xalign(0)
            self.purchased_gifts_box.append(no_gifts_label)
            return
        
        # Get character type and gift structure
        char_type = getattr(self.character, 'character_type', 'Garou')
        breed_data = CHANGING_BREEDS.get(char_type, CHANGING_BREEDS["Garou"])
        gifts_data = breed_data.get("gifts", {})
        
        breed_gifts_data = gifts_data.get("breed", BREED_GIFTS)
        auspice_gifts_data = gifts_data.get("auspice", AUSPICE_GIFTS)
        tribe_gifts_data = gifts_data.get("tribe", TRIBE_GIFTS)
        general_gifts_data = gifts_data.get("general", {})
        
        # Group gifts by type and level
        breed_gifts = []
        auspice_gifts = []
        tribe_gifts = []
        general_gifts = []
        
        for gift_name, level in sorted(self.character.gifts.items()):
            gift_info = (gift_name, level)
            # Determine gift type by checking data
            found = False
            
            # Check breed gifts
            if self.character.breed:
                if isinstance(breed_gifts_data, dict) and self.character.breed in breed_gifts_data:
                    gifts_dict = breed_gifts_data[self.character.breed]
                    for lvl, gifts in gifts_dict.items():
                        if lvl == level and any(g[0] == gift_name for g in gifts):
                            breed_gifts.append(gift_info)
                            found = True
                            break
                elif self.character.breed in BREED_GIFTS:  # Fallback for Garou
                    gifts_dict = BREED_GIFTS[self.character.breed]
                    for lvl, gifts in gifts_dict.items():
                        if lvl == level and any(g[0] == gift_name for g in gifts):
                            breed_gifts.append(gift_info)
                            found = True
                            break
            
            # Check auspice gifts
            if not found and self.character.auspice:
                if isinstance(auspice_gifts_data, dict) and self.character.auspice in auspice_gifts_data:
                    gifts_dict = auspice_gifts_data[self.character.auspice]
                    for lvl, gifts in gifts_dict.items():
                        if lvl == level and any(g[0] == gift_name for g in gifts):
                            auspice_gifts.append(gift_info)
                            found = True
                            break
                elif self.character.auspice in AUSPICE_GIFTS:  # Fallback for Garou
                    gifts_dict = AUSPICE_GIFTS[self.character.auspice]
                    for lvl, gifts in gifts_dict.items():
                        if lvl == level and any(g[0] == gift_name for g in gifts):
                            auspice_gifts.append(gift_info)
                            found = True
                            break
            
            # Check tribe gifts
            if not found and self.character.tribe:
                if isinstance(tribe_gifts_data, dict) and self.character.tribe in tribe_gifts_data:
                    gifts_dict = tribe_gifts_data[self.character.tribe]
                    for lvl, gifts in gifts_dict.items():
                        if lvl == level and any(g[0] == gift_name for g in gifts):
                            tribe_gifts.append(gift_info)
                            found = True
                            break
                elif self.character.tribe in TRIBE_GIFTS:  # Fallback for Garou
                    gifts_dict = TRIBE_GIFTS[self.character.tribe]
                    for lvl, gifts in gifts_dict.items():
                        if lvl == level and any(g[0] == gift_name for g in gifts):
                            tribe_gifts.append(gift_info)
                            found = True
                            break
            
            # Check general gifts
            if not found and general_gifts_data:
                for lvl, gifts in general_gifts_data.items():
                    if lvl == level and any(g[0] == gift_name for g in gifts):
                        general_gifts.append(gift_info)
                        found = True
                        break
            
            # Check umbral danser gifts
            if not found and umbral_danser_gifts_data:
                for lvl, gifts in umbral_danser_gifts_data.items():
                    if lvl == level and any(g[0] == gift_name for g in gifts):
                        umbral_danser_gifts.append(gift_info)
                        found = True
                        break
            
            # Check Wyrmish breed gifts if character is Black Spiral Dancer
            if not found and self.character.tribe == "Black Spiral Dancers" and self.character.breed and self.character.breed in WYRMISH_BREED_GIFTS:
                gifts_dict = WYRMISH_BREED_GIFTS[self.character.breed]
                for lvl, gifts in gifts_dict.items():
                    if lvl == level and any(g[0] == gift_name for g in gifts):
                        breed_gifts.append(gift_info)
                        found = True
                        break
            
            # Check Wyrmish auspice gifts if character is Black Spiral Dancer
            if not found and self.character.tribe == "Black Spiral Dancers" and self.character.auspice and self.character.auspice in WYRMISH_AUSPICE_GIFTS:
                gifts_dict = WYRMISH_AUSPICE_GIFTS[self.character.auspice]
                for lvl, gifts in gifts_dict.items():
                    if lvl == level and any(g[0] == gift_name for g in gifts):
                        auspice_gifts.append(gift_info)
                        found = True
                        break
        
        # Helper function to get gift description
        def get_gift_description(gift_name, level, gift_type):
            # Check changing breed gifts first
            if gift_type == "breed" and self.character.breed:
                if isinstance(breed_gifts_data, dict) and self.character.breed in breed_gifts_data:
                    gifts_dict = breed_gifts_data[self.character.breed]
                    if level in gifts_dict:
                        for g_name, g_desc in gifts_dict[level]:
                            if g_name == gift_name:
                                return g_desc
                elif self.character.breed in BREED_GIFTS:  # Fallback for Garou
                    gifts_dict = BREED_GIFTS[self.character.breed]
                    if level in gifts_dict:
                        for g_name, g_desc in gifts_dict[level]:
                            if g_name == gift_name:
                                return g_desc
            elif gift_type == "auspice" and self.character.auspice:
                if isinstance(auspice_gifts_data, dict) and self.character.auspice in auspice_gifts_data:
                    gifts_dict = auspice_gifts_data[self.character.auspice]
                    if level in gifts_dict:
                        for g_name, g_desc in gifts_dict[level]:
                            if g_name == gift_name:
                                return g_desc
                elif self.character.auspice in AUSPICE_GIFTS:  # Fallback for Garou
                    gifts_dict = AUSPICE_GIFTS[self.character.auspice]
                    if level in gifts_dict:
                        for g_name, g_desc in gifts_dict[level]:
                            if g_name == gift_name:
                                return g_desc
            elif gift_type == "tribe" and self.character.tribe:
                if isinstance(tribe_gifts_data, dict) and self.character.tribe in tribe_gifts_data:
                    gifts_dict = tribe_gifts_data[self.character.tribe]
                    if level in gifts_dict:
                        for g_name, g_desc in gifts_dict[level]:
                            if g_name == gift_name:
                                return g_desc
                elif self.character.tribe in TRIBE_GIFTS:  # Fallback for Garou
                    gifts_dict = TRIBE_GIFTS[self.character.tribe]
                    if level in gifts_dict:
                        for g_name, g_desc in gifts_dict[level]:
                            if g_name == gift_name:
                                return g_desc
            elif gift_type == "general" and general_gifts_data:
                if level in general_gifts_data:
                    for g_name, g_desc in general_gifts_data[level]:
                        if g_name == gift_name:
                            return g_desc
            elif gift_type == "umbral_danser" and umbral_danser_gifts_data:
                if level in umbral_danser_gifts_data:
                    for g_name, g_desc in umbral_danser_gifts_data[level]:
                        if g_name == gift_name:
                            return g_desc
            
            # Check Wyrmish gifts if character is Black Spiral Dancer
            if self.character.tribe == "Black Spiral Dancers":
                if gift_type == "breed" and self.character.breed and self.character.breed in WYRMISH_BREED_GIFTS:
                    gifts_dict = WYRMISH_BREED_GIFTS[self.character.breed]
                    if level in gifts_dict:
                        for g_name, g_desc in gifts_dict[level]:
                            if g_name == gift_name:
                                return g_desc
                elif gift_type == "auspice" and self.character.auspice and self.character.auspice in WYRMISH_AUSPICE_GIFTS:
                    gifts_dict = WYRMISH_AUSPICE_GIFTS[self.character.auspice]
                    if level in gifts_dict:
                        for g_name, g_desc in gifts_dict[level]:
                            if g_name == gift_name:
                                return g_desc
            
            return ""
        
        # Display gifts
        if breed_gifts:
            label = Gtk.Label(label="Breed Gifts:")
            label.add_css_class("heading")
            label.set_xalign(0)
            self.purchased_gifts_box.append(label)
            for gift_name, level in breed_gifts:
                # Gift container (vertical box for name and description)
                gift_container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
                gift_container.set_margin_start(8)
                gift_container.set_margin_end(8)
                gift_container.set_margin_bottom(8)
                
                # Top row with name and remove button
                row = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
                gift_label = Gtk.Label(label=f"• {gift_name} (Level {level})")
                gift_label.set_xalign(0)
                gift_label.set_hexpand(True)
                row.append(gift_label)
                
                # Remove button
                remove_btn = Gtk.Button(icon_name="edit-delete-symbolic")
                remove_btn.add_css_class("flat")
                remove_btn.set_tooltip_text("Remove gift")
                remove_btn.connect("clicked", self._on_remove_gift, gift_name)
                row.append(remove_btn)
                gift_container.append(row)
                
                # Description
                desc = get_gift_description(gift_name, level, "breed")
                if desc:
                    desc_label = Gtk.Label(label=desc)
                    desc_label.set_xalign(0)
                    desc_label.set_wrap(True)
                    desc_label.add_css_class("dim-label")
                    desc_label.set_margin_start(16)
                    gift_container.append(desc_label)
                
                self.purchased_gifts_box.append(gift_container)
        
        if auspice_gifts:
            label = Gtk.Label(label="Auspice Gifts:")
            label.add_css_class("heading")
            label.set_xalign(0)
            self.purchased_gifts_box.append(label)
            for gift_name, level in auspice_gifts:
                # Gift container (vertical box for name and description)
                gift_container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
                gift_container.set_margin_start(8)
                gift_container.set_margin_end(8)
                gift_container.set_margin_bottom(8)
                
                # Top row with name and remove button
                row = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
                gift_label = Gtk.Label(label=f"• {gift_name} (Level {level})")
                gift_label.set_xalign(0)
                gift_label.set_hexpand(True)
                row.append(gift_label)
                
                # Remove button
                remove_btn = Gtk.Button(icon_name="edit-delete-symbolic")
                remove_btn.add_css_class("flat")
                remove_btn.set_tooltip_text("Remove gift")
                remove_btn.connect("clicked", self._on_remove_gift, gift_name)
                row.append(remove_btn)
                gift_container.append(row)
                
                # Description
                desc = get_gift_description(gift_name, level, "auspice")
                if desc:
                    desc_label = Gtk.Label(label=desc)
                    desc_label.set_xalign(0)
                    desc_label.set_wrap(True)
                    desc_label.add_css_class("dim-label")
                    desc_label.set_margin_start(16)
                    gift_container.append(desc_label)
                
                self.purchased_gifts_box.append(gift_container)
        
        if tribe_gifts:
            label = Gtk.Label(label="Tribe Gifts:")
            label.add_css_class("heading")
            label.set_xalign(0)
            self.purchased_gifts_box.append(label)
            for gift_name, level in tribe_gifts:
                # Gift container (vertical box for name and description)
                gift_container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
                gift_container.set_margin_start(8)
                gift_container.set_margin_end(8)
                gift_container.set_margin_bottom(8)
                
                # Top row with name and remove button
                row = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
                gift_label = Gtk.Label(label=f"• {gift_name} (Level {level})")
                gift_label.set_xalign(0)
                gift_label.set_hexpand(True)
                row.append(gift_label)
                
                # Remove button
                remove_btn = Gtk.Button(icon_name="edit-delete-symbolic")
                remove_btn.add_css_class("flat")
                remove_btn.set_tooltip_text("Remove gift")
                remove_btn.connect("clicked", self._on_remove_gift, gift_name)
                row.append(remove_btn)
                gift_container.append(row)
                
                # Description
                desc = get_gift_description(gift_name, level, "tribe")
                if desc:
                    desc_label = Gtk.Label(label=desc)
                    desc_label.set_xalign(0)
                    desc_label.set_wrap(True)
                    desc_label.add_css_class("dim-label")
                    desc_label.set_margin_start(16)
                    gift_container.append(desc_label)
                
                self.purchased_gifts_box.append(gift_container)
        
        if general_gifts:
            label = Gtk.Label(label="General Gifts:")
            label.add_css_class("heading")
            label.set_xalign(0)
            self.purchased_gifts_box.append(label)
            for gift_name, level in general_gifts:
                # Gift container (vertical box for name and description)
                gift_container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
                gift_container.set_margin_start(8)
                gift_container.set_margin_end(8)
                gift_container.set_margin_bottom(8)
                
                # Top row with name and remove button
                row = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
                gift_label = Gtk.Label(label=f"• {gift_name} (Level {level})")
                gift_label.set_xalign(0)
                gift_label.set_hexpand(True)
                row.append(gift_label)
                
                # Remove button
                remove_btn = Gtk.Button(icon_name="edit-delete-symbolic")
                remove_btn.add_css_class("flat")
                remove_btn.set_tooltip_text("Remove gift")
                remove_btn.connect("clicked", self._on_remove_gift, gift_name)
                row.append(remove_btn)
                gift_container.append(row)
                
                # Description
                desc = get_gift_description(gift_name, level, "general")
                if desc:
                    desc_label = Gtk.Label(label=desc)
                    desc_label.set_xalign(0)
                    desc_label.set_wrap(True)
                    desc_label.add_css_class("dim-label")
                    desc_label.set_margin_start(16)
                    gift_container.append(desc_label)
                
                self.purchased_gifts_box.append(gift_container)
        
        if umbral_danser_gifts:
            label = Gtk.Label(label="Umbral Danser Gifts:")
            label.add_css_class("heading")
            label.set_xalign(0)
            self.purchased_gifts_box.append(label)
            for gift_name, level in umbral_danser_gifts:
                # Gift container (vertical box for name and description)
                gift_container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
                gift_container.set_margin_start(8)
                gift_container.set_margin_end(8)
                gift_container.set_margin_bottom(8)
                
                # Top row with name and remove button
                row = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
                gift_label = Gtk.Label(label=f"• {gift_name} (Level {level})")
                gift_label.set_xalign(0)
                gift_label.set_hexpand(True)
                row.append(gift_label)
                
                # Remove button
                remove_btn = Gtk.Button(icon_name="edit-delete-symbolic")
                remove_btn.add_css_class("flat")
                remove_btn.set_tooltip_text("Remove gift")
                remove_btn.connect("clicked", self._on_remove_gift, gift_name)
                row.append(remove_btn)
                gift_container.append(row)
                
                # Description
                desc = get_gift_description(gift_name, level, "umbral_danser")
                if desc:
                    desc_label = Gtk.Label(label=desc)
                    desc_label.set_xalign(0)
                    desc_label.set_wrap(True)
                    desc_label.add_css_class("dim-label")
                    desc_label.set_margin_start(16)
                    gift_container.append(desc_label)
                
                self.purchased_gifts_box.append(gift_container)
    
    def _on_remove_gift(self, button, gift_name):
        """Remove a gift from the character."""
        if not self.character or gift_name not in self.character.gifts:
            return
        del self.character.gifts[gift_name]
        self._update_purchased_gifts_display()
        self.app.update_tracker()
    
    def _on_purchase_gifts_clicked(self, button):
        """Open the gift purchase dialog."""
        if not self.character:
            return
        
        dialog = GiftPurchaseDialog(self.app.win, self.character, self)
        dialog.present()
    
    def _create_gifts_section(self) -> Gtk.Box:
        section = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        section.append(self._create_section_header("Gifts"))
        
        # Create notebook for Breed, Auspice, and Tribe Gifts
        notebook = Gtk.Notebook()
        
        # Breed Gifts tab
        breed_scroll = Gtk.ScrolledWindow()
        breed_scroll.set_min_content_height(400)
        breed_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        breed_box.set_margin_start(8)
        breed_box.set_margin_end(8)
        breed_box.set_margin_top(8)
        
        self.gift_checks = {}
        # Check if character exists and what mode we're in
        show_all_levels = self.character and self.character.creation_mode == "xp"
        
        for breed, gifts_dict in BREED_GIFTS.items():
            for level, gifts in sorted(gifts_dict.items()):
                # Only show Level 1 in Creation/Freebie mode, all levels in XP mode
                if show_all_levels or level == 1:
                    cat_label = Gtk.Label(label=f"{breed} Breed Gifts - Level {level}")
                    cat_label.add_css_class("heading")
                    cat_label.set_xalign(0)
                    breed_box.append(cat_label)
                    
                    for gift_name, gift_desc in gifts:
                        check_row = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
                        check = Gtk.CheckButton(label=gift_name)
                        check.set_tooltip_text(gift_desc)
                        check.connect("toggled", self._on_gift_toggled, gift_name, "breed", level)
                        self.gift_checks[f"breed_{gift_name}_{level}"] = check
                        check_row.append(check)
                        breed_box.append(check_row)
        
        breed_scroll.set_child(breed_box)
        notebook.append_page(breed_scroll, Gtk.Label(label="Breed Gifts"))
        
        # Auspice Gifts tab
        auspice_scroll = Gtk.ScrolledWindow()
        auspice_scroll.set_min_content_height(400)
        auspice_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        auspice_box.set_margin_start(8)
        auspice_box.set_margin_end(8)
        auspice_box.set_margin_top(8)
        
        for auspice, gifts_dict in AUSPICE_GIFTS.items():
            for level, gifts in sorted(gifts_dict.items()):
                if show_all_levels or level == 1:
                    cat_label = Gtk.Label(label=f"{auspice} Auspice Gifts - Level {level}")
                    cat_label.add_css_class("heading")
                    cat_label.set_xalign(0)
                    auspice_box.append(cat_label)
                    
                    for gift_name, gift_desc in gifts:
                        check_row = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
                        check = Gtk.CheckButton(label=gift_name)
                        check.set_tooltip_text(gift_desc)
                        check.connect("toggled", self._on_gift_toggled, gift_name, "auspice", level)
                        self.gift_checks[f"auspice_{gift_name}_{level}"] = check
                        check_row.append(check)
                        auspice_box.append(check_row)
        
        auspice_scroll.set_child(auspice_box)
        notebook.append_page(auspice_scroll, Gtk.Label(label="Auspice Gifts"))
        
        # Tribe Gifts tab
        tribe_scroll = Gtk.ScrolledWindow()
        tribe_scroll.set_min_content_height(400)
        tribe_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        tribe_box.set_margin_start(8)
        tribe_box.set_margin_end(8)
        tribe_box.set_margin_top(8)
        
        for tribe, gifts_dict in TRIBE_GIFTS.items():
            for level, gifts in sorted(gifts_dict.items()):
                if show_all_levels or level == 1:
                    cat_label = Gtk.Label(label=f"{tribe} Tribe Gifts - Level {level}")
                    cat_label.add_css_class("heading")
                    cat_label.set_xalign(0)
                    tribe_box.append(cat_label)
                    
                    for gift_name, gift_desc in gifts:
                        check_row = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
                        check = Gtk.CheckButton(label=gift_name)
                        check.set_tooltip_text(gift_desc)
                        check.connect("toggled", self._on_gift_toggled, gift_name, "tribe", level)
                        self.gift_checks[f"tribe_{gift_name}_{level}"] = check
                        check_row.append(check)
                        tribe_box.append(check_row)
        
        tribe_scroll.set_child(tribe_box)
        notebook.append_page(tribe_scroll, Gtk.Label(label="Tribe Gifts"))
        
        section.append(notebook)
        return section
    
    
    def _create_forms_section(self, forms_dict=None) -> Gtk.Box:
        """Create forms section. If forms_dict is None, uses FORMS (Garou default)."""
        section = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        section.append(self._create_section_header("Forms"))
        
        # Use provided forms dict or default to Garou FORMS
        if forms_dict is None:
            forms_dict = FORMS
        
        # Create expandable sections for each form
        first_form = list(forms_dict.keys())[0] if forms_dict else "Homid"
        for form_name, form_data in forms_dict.items():
            expander = Gtk.Expander(label=form_name)
            # Expand first form by default (usually Homid or similar)
            expander.set_expanded(form_name == first_form)
            
            form_content = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
            form_content.set_margin_start(16)
            form_content.set_margin_end(16)
            form_content.set_margin_top(8)
            form_content.set_margin_bottom(8)
            
            # Description
            desc_label = Gtk.Label(label=form_data["description"])
            desc_label.set_wrap(True)
            desc_label.set_xalign(0)
            form_content.append(desc_label)
            
            # Size
            size_label = Gtk.Label(label=f"Size: {form_data['size']}")
            size_label.set_xalign(0)
            form_content.append(size_label)
            
            # Shift Difficulty
            diff_label = Gtk.Label(label=f"Shift Difficulty: {form_data['shift_difficulty']}")
            diff_label.set_xalign(0)
            form_content.append(diff_label)
            
            # Attribute Modifiers
            modifiers_label = Gtk.Label(label="Attribute Modifiers:")
            modifiers_label.add_css_class("heading")
            modifiers_label.set_xalign(0)
            form_content.append(modifiers_label)
            
            modifiers = form_data["statistics_adjustment"]
            mod_grid = Gtk.Grid()
            mod_grid.set_column_spacing(16)
            mod_grid.set_row_spacing(4)
            
            col = 0
            for category, attrs in ATTRIBUTES.items():
                header = Gtk.Label(label=category)
                header.add_css_class("heading")
                mod_grid.attach(header, col, 0, 1, 1)
                
                for row, attr in enumerate(attrs, 1):
                    mod = modifiers.get(attr, 0)
                    mod_str = f"{attr}: {mod:+d}" if mod != 0 else f"{attr}: —"
                    mod_label = Gtk.Label(label=mod_str)
                    mod_label.set_xalign(0)
                    mod_grid.attach(mod_label, col, row, 1, 1)
                
                col += 1
            
            form_content.append(mod_grid)
            
            # Special abilities
            if form_data.get("special"):
                form_content.append(Gtk.Separator())
                special_label = Gtk.Label(label=f"Special: {form_data['special']}")
                special_label.set_wrap(True)
                special_label.set_xalign(0)
                form_content.append(special_label)
            
            expander.set_child(form_content)
            section.append(expander)
        
        return section
    
    def _rebuild_forms_section(self, char_type):
        """Rebuild the forms section for the given character type."""
        # Get forms for this character type
        breed_data = CHANGING_BREEDS.get(char_type, CHANGING_BREEDS["Garou"])
        forms_dict = breed_data.get("forms", FORMS)
        
        # Find the forms section and the separator before it
        prev_sibling = None
        for child in self.garou_wrapper:
            if child == self.forms_section:
                break
            prev_sibling = child
        
        # Remove old forms section
        self.garou_wrapper.remove(self.forms_section)
        
        # Create new forms section
        self.forms_section = self._create_forms_section(forms_dict)
        
        # Insert after the previous sibling (or at start if no previous)
        if prev_sibling:
            self.garou_wrapper.insert_child_after(self.forms_section, prev_sibling)
        else:
            # Insert at the beginning (after gifts section)
            first_child = self.garou_wrapper.get_first_child()
            if first_child:
                self.garou_wrapper.insert_child_after(self.forms_section, first_child)
            else:
                self.garou_wrapper.append(self.forms_section)
    
    def _create_backgrounds_section(self) -> Gtk.Box:
        section = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        section.append(self._create_section_header("Backgrounds"))
        
        std_expander = Gtk.Expander(label="Standard Backgrounds")
        std_expander.set_expanded(True)
        std_box = Gtk.FlowBox()
        std_box.set_selection_mode(Gtk.SelectionMode.NONE)
        std_box.set_max_children_per_line(3)
        std_box.set_column_spacing(16)
        std_box.set_row_spacing(4)
        
        for bg_name, bg_desc in BACKGROUNDS["standard"]:
            trait_row = TraitRow(bg_name, 5, 0, 0, self._on_background_changed)
            trait_row.set_tooltip_text(bg_desc)
            self.trait_widgets[f"bg_{bg_name}"] = trait_row
            std_box.append(trait_row)
        
        std_expander.set_child(std_box)
        section.append(std_expander)
        
        return section
    
    def _create_core_traits_section(self) -> Gtk.Box:
        section = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        section.append(self._create_section_header("Core Traits"))
        
        # Rage
        rage_row = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        rage_label = Gtk.Label(label="Rage:")
        rage_label.set_width_chars(15)
        rage_label.set_xalign(0)
        self.rage_dots = DotRating(10, 1, 1, self._on_rage_changed)
        rage_row.append(rage_label)
        rage_row.append(self.rage_dots)
        section.append(rage_row)
        
        # Gnosis
        gnosis_row = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        gnosis_label = Gtk.Label(label="Gnosis:")
        gnosis_label.set_width_chars(15)
        gnosis_label.set_xalign(0)
        self.gnosis_dots = DotRating(10, 1, 1, self._on_gnosis_changed)
        gnosis_row.append(gnosis_label)
        gnosis_row.append(self.gnosis_dots)
        section.append(gnosis_row)
        
        # Willpower
        will_row = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        will_label = Gtk.Label(label="Willpower:")
        will_label.set_width_chars(15)
        will_label.set_xalign(0)
        self.willpower_dots = DotRating(10, 3, 1, self._on_willpower_changed)
        will_row.append(will_label)
        will_row.append(self.willpower_dots)
        section.append(will_row)
        
        # Rank
        rank_row = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        rank_label = Gtk.Label(label="Rank:")
        rank_label.set_width_chars(15)
        rank_label.set_xalign(0)
        self.rank_spin = Gtk.SpinButton.new_with_range(1, 10, 1)
        self.rank_spin.connect("value-changed", self._on_rank_changed)
        rank_row.append(rank_label)
        rank_row.append(self.rank_spin)
        section.append(rank_row)
        
        return section
    
    def _create_renown_section(self) -> Gtk.Box:
        section = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        section.append(self._create_section_header("Renown"))
        
        # Store reference to section for dynamic updates
        self.renown_section = section
        self.renown_rows = {}  # Store renown rows for dynamic updates
        
        # Initial population with default (Garou) renown types
        self._update_renown_display()
        
        return section
    
    def _update_renown_display(self):
        """Update renown display based on current character type."""
        if not hasattr(self, 'renown_section'):
            return
        
        # Get current character type
        char_type = "Garou"
        if self.character:
            char_type = self.character.character_type
        elif hasattr(self, 'character_type_combo'):
            char_type_display = self.character_type_combo.get_active_text() or ""
            for breed_key, breed_data in CHANGING_BREEDS.items():
                if breed_data["display_name"] == char_type_display:
                    char_type = breed_key
                    break
        
        breed_data = CHANGING_BREEDS.get(char_type, CHANGING_BREEDS["Garou"])
        renown_types = breed_data.get("renown_types", ["Glory", "Honor", "Wisdom"])
        
        # Remove old renown rows
        for renown_type, row in self.renown_rows.items():
            if row.get_parent():
                self.renown_section.remove(row)
            if f"renown_{renown_type}" in self.trait_widgets:
                del self.trait_widgets[f"renown_{renown_type}"]
        self.renown_rows.clear()
        
        # Add new renown rows
        for renown_type in renown_types:
            renown_row = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
            renown_label = Gtk.Label(label=f"{renown_type}:")
            renown_label.set_width_chars(15)
            renown_label.set_xalign(0)
            current_value = 0
            if self.character and renown_type in self.character.renown:
                current_value = self.character.renown[renown_type]
            renown_dots = DotRating(10, current_value, 0, 
                                   lambda val, rt=renown_type: self._on_renown_changed(rt, val))
            self.trait_widgets[f"renown_{renown_type}"] = renown_dots
            renown_row.append(renown_label)
            renown_row.append(renown_dots)
            self.renown_section.append(renown_row)
            self.renown_rows[renown_type] = renown_row
    
    def _create_merits_flaws_section(self) -> Gtk.Box:
        section = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        section.append(self._create_section_header("Merits & Flaws"))
        
        notebook = Gtk.Notebook()
        
        # Merits tab
        merits_scroll = Gtk.ScrolledWindow()
        merits_scroll.set_min_content_height(200)
        merits_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        merits_box.set_margin_start(8)
        merits_box.set_margin_end(8)
        merits_box.set_margin_top(8)
        
        self.merit_checks = {}
        for category, merits in MERITS.items():
            cat_label = Gtk.Label(label=category)
            cat_label.add_css_class("heading")
            cat_label.set_xalign(0)
            merits_box.append(cat_label)
            
            for merit_name, merit_data in merits.items():
                check_row = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
                check = Gtk.CheckButton(label=f"{merit_name} ({merit_data['cost']} pts)")
                check.set_tooltip_text(merit_data['description'])
                check.connect("toggled", self._on_merit_toggled, merit_name, merit_data['cost'])
                self.merit_checks[merit_name] = check
                check_row.append(check)
                merits_box.append(check_row)
        
        merits_scroll.set_child(merits_box)
        notebook.append_page(merits_scroll, Gtk.Label(label="Merits"))
        
        # Flaws tab
        flaws_scroll = Gtk.ScrolledWindow()
        flaws_scroll.set_min_content_height(200)
        flaws_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        flaws_box.set_margin_start(8)
        flaws_box.set_margin_end(8)
        flaws_box.set_margin_top(8)
        
        self.flaw_checks = {}
        for category, flaws in FLAWS.items():
            cat_label = Gtk.Label(label=category)
            cat_label.add_css_class("heading")
            cat_label.set_xalign(0)
            flaws_box.append(cat_label)
            
            for flaw_name, flaw_data in flaws.items():
                check_row = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
                check = Gtk.CheckButton(label=f"{flaw_name} ({flaw_data['bonus']} pts)")
                check.set_tooltip_text(flaw_data['description'])
                check.connect("toggled", self._on_flaw_toggled, flaw_name, flaw_data['bonus'])
                self.flaw_checks[flaw_name] = check
                check_row.append(check)
                flaws_box.append(check_row)
        
        flaws_scroll.set_child(flaws_box)
        notebook.append_page(flaws_scroll, Gtk.Label(label="Flaws"))
        
        section.append(notebook)
        return section
    
    def _create_notes_section(self) -> Gtk.Box:
        section = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        section.append(self._create_section_header("Notes"))
        
        self.notes_text = Gtk.TextView()
        self.notes_text.set_wrap_mode(Gtk.WrapMode.WORD)
        self.notes_text.get_buffer().connect("changed", self._on_notes_changed)
        
        notes_frame = Gtk.Frame()
        notes_frame.set_child(self.notes_text)
        notes_frame.set_size_request(-1, 120)
        section.append(notes_frame)
        
        return section
    
    # Event handlers
    def _on_identity_changed(self, widget, field):
        if self._updating or not self.character:
            return
        
        if field == "name":
            self.character.name = widget.get_text()
        elif field == "player":
            self.character.player = widget.get_text()
        elif field == "chronicle":
            self.character.chronicle = widget.get_text()
        elif field == "concept":
            self.character.concept = widget.get_active_text() or ""
        elif field == "nature":
            self.character.nature = widget.get_active_text() or ""
        elif field == "demeanor":
            self.character.demeanor = widget.get_active_text() or ""
        
        self.app.update_tracker()
    
    def _on_breed_changed(self, widget):
        if self._updating or not self.character:
            return
        
        breed = widget.get_active_text() or ""
        self.character.breed = breed
        
        # Get current character type data
        char_type = self.character.character_type or "Garou"
        breed_data = CHANGING_BREEDS.get(char_type, CHANGING_BREEDS["Garou"])
        breeds = breed_data.get("breeds", BREEDS)
        
        # Show/hide Metis deformity selector (works for Garou and other breeds with Metis)
        is_metis = (breed == "Metis" or breed in ["Metis", "Ahi"])  # Ahi is Nagah metis
        self.deformity_box.set_visible(is_metis)
        
        if is_metis:
            if breed in breeds and "deformities" in breeds[breed]:
                self.deformity_combo.remove_all()
                self.deformity_combo.append_text("")
                for deformity in breeds[breed]["deformities"]:
                    self.deformity_combo.append_text(deformity)
            elif breed == "Metis" and char_type == "Garou" and breed in BREEDS and "deformities" in BREEDS[breed]:
                # Fallback for Garou
                self.deformity_combo.remove_all()
                self.deformity_combo.append_text("")
                for deformity in BREEDS[breed]["deformities"]:
                    self.deformity_combo.append_text(deformity)
        
        # Set initial Gnosis based on breed
        if breed in breeds and "initial_gnosis" in breeds[breed]:
            initial_gnosis = breeds[breed]["initial_gnosis"]
            if self.character.gnosis != initial_gnosis:
                self._updating = True
                self.character.gnosis = initial_gnosis
                self.gnosis_dots.set_value(initial_gnosis)
                self._updating = False
        elif breed in BREEDS and char_type == "Garou":
            # Fallback for Garou
            initial_gnosis = BREEDS[breed]["initial_gnosis"]
            if self.character.gnosis != initial_gnosis:
                self._updating = True
                self.character.gnosis = initial_gnosis
                self.gnosis_dots.set_value(initial_gnosis)
                self._updating = False
        
        self.app.update_tracker()
    
    def _on_auspice_changed(self, widget):
        if self._updating or not self.character:
            return
        
        auspice = widget.get_active_text() or ""
        self.character.auspice = auspice
        
        # Get current character type data
        char_type = self.character.character_type or "Garou"
        breed_data = CHANGING_BREEDS.get(char_type, CHANGING_BREEDS["Garou"])
        auspices = breed_data.get("auspices", AUSPICES)
        
        # Set initial Rage based on auspice
        if auspice in auspices:
            auspice_data = auspices[auspice]
            if "initial_rage" in auspice_data:
                initial_rage = auspice_data["initial_rage"]
                if initial_rage > 0 and self.character.rage != initial_rage:
                    self._updating = True
                    self.character.rage = initial_rage
                    self.rage_dots.set_value(initial_rage)
                    self._updating = False
            # Some breeds have initial_gnosis in auspice
            if "initial_gnosis" in auspice_data:
                initial_gnosis = auspice_data["initial_gnosis"]
                if self.character.gnosis != initial_gnosis:
                    self._updating = True
                    self.character.gnosis = initial_gnosis
                    self.gnosis_dots.set_value(initial_gnosis)
                    self._updating = False
            # Some breeds have initial_willpower in auspice
            if "initial_willpower" in auspice_data:
                initial_willpower = auspice_data["initial_willpower"]
                if initial_willpower > 0 and self.character.willpower != initial_willpower:
                    self._updating = True
                    self.character.willpower = initial_willpower
                    self.willpower_dots.set_value(initial_willpower)
                    self._updating = False
        elif auspice in AUSPICES and char_type == "Garou":
            # Fallback for Garou
            initial_rage = AUSPICES[auspice]["initial_rage"]
            if self.character.rage != initial_rage:
                self._updating = True
                self.character.rage = initial_rage
                self.rage_dots.set_value(initial_rage)
                self._updating = False
        
        self.app.update_tracker()
    
    def _on_tribe_changed(self, widget):
        if self._updating or not self.character:
            return
        
        tribe = widget.get_active_text() or ""
        self.character.tribe = tribe
        
        # Get current character type data
        char_type = self.character.character_type or "Garou"
        breed_data = CHANGING_BREEDS.get(char_type, CHANGING_BREEDS["Garou"])
        tribes = breed_data.get("tribes", TRIBES)
        
        # Set initial traits based on tribe
        if tribe in tribes:
            tribe_data = tribes[tribe]
            # Some breeds have initial_willpower in tribe (e.g., Garou, Bastet)
            if "initial_willpower" in tribe_data:
                initial_willpower = tribe_data["initial_willpower"]
                if initial_willpower > 0 and self.character.willpower != initial_willpower:
                    self._updating = True
                    self.character.willpower = initial_willpower
                    self.willpower_dots.set_value(initial_willpower)
                    self._updating = False
            # Some breeds have initial_rage in tribe (e.g., Bastet)
            if "initial_rage" in tribe_data:
                initial_rage = tribe_data["initial_rage"]
                if initial_rage > 0 and self.character.rage != initial_rage:
                    self._updating = True
                    self.character.rage = initial_rage
                    self.rage_dots.set_value(initial_rage)
                    self._updating = False
            # Some breeds have initial_gnosis in tribe
            if "initial_gnosis" in tribe_data:
                initial_gnosis = tribe_data["initial_gnosis"]
                if self.character.gnosis != initial_gnosis:
                    self._updating = True
                    self.character.gnosis = initial_gnosis
                    self.gnosis_dots.set_value(initial_gnosis)
                    self._updating = False
        elif tribe in TRIBES and char_type == "Garou":
            # Fallback for Garou
            initial_willpower = TRIBES[tribe]["initial_willpower"]
            if self.character.willpower != initial_willpower:
                self._updating = True
                self.character.willpower = initial_willpower
                self.willpower_dots.set_value(initial_willpower)
                self._updating = False
        else:
            # Check if willpower is fixed for this breed
            starting_traits = breed_data.get("starting_traits", {})
            if "willpower" in starting_traits and isinstance(starting_traits["willpower"], int):
                fixed_willpower = starting_traits["willpower"]
                if self.character.willpower != fixed_willpower:
                    self._updating = True
                    self.character.willpower = fixed_willpower
                    self.willpower_dots.set_value(fixed_willpower)
                    self._updating = False
        
        self.app.update_tracker()
    
    def _on_deformity_changed(self, widget):
        if self._updating or not self.character:
            return
        self.character.metis_deformity = widget.get_active_text() or ""
    
    def _on_attr_priority_changed(self, widget, category):
        if self._updating or not self.character:
            return
        
        text = widget.get_active_text()
        priority = text.lower() if text and text != "—" else None
        self.character.attribute_priorities[category] = priority
        self._update_attr_priority_options()
        self.app.update_tracker()
    
    def _on_ability_priority_changed(self, widget, category):
        if self._updating or not self.character:
            return
        
        text = widget.get_active_text()
        priority = text.lower() if text and text != "—" else None
        self.character.ability_priorities[category] = priority
        self._update_ability_priority_options()
        self.app.update_tracker()
    
    def _update_attr_priority_options(self):
        """Update attribute priority combos to hide already-selected priorities."""
        if self._updating or not self.character:
            return
        
        self._updating = True
        
        selected = {}
        for cat, combo in self.attr_priority_combos.items():
            text = combo.get_active_text()
            if text and text != "—":
                selected[cat] = text.lower()
        
        for cat, combo in self.attr_priority_combos.items():
            current_selection = selected.get(cat)
            used_by_others = [p for c, p in selected.items() if c != cat]
            
            combo.remove_all()
            combo.append_text("—")
            
            for priority in ["primary", "secondary", "tertiary"]:
                if priority not in used_by_others:
                    combo.append_text(priority.capitalize())
            
            if current_selection:
                model = combo.get_model()
                for i, row in enumerate(model):
                    if row[0] and row[0].lower() == current_selection:
                        combo.set_active(i)
                        break
            else:
                combo.set_active(0)
        
        self._updating = False
    
    def _update_ability_priority_options(self):
        """Update ability priority combos to hide already-selected priorities."""
        if self._updating or not self.character:
            return
        
        self._updating = True
        
        selected = {}
        for cat, combo in self.ability_priority_combos.items():
            text = combo.get_active_text()
            if text and text != "—":
                selected[cat] = text.lower()
        
        for cat, combo in self.ability_priority_combos.items():
            current_selection = selected.get(cat)
            used_by_others = [p for c, p in selected.items() if c != cat]
            
            combo.remove_all()
            combo.append_text("—")
            
            for priority in ["primary", "secondary", "tertiary"]:
                if priority not in used_by_others:
                    combo.append_text(priority.capitalize())
            
            if current_selection:
                model = combo.get_model()
                for i, row in enumerate(model):
                    if row[0] and row[0].lower() == current_selection:
                        combo.set_active(i)
                        break
            else:
                combo.set_active(0)
        
        self._updating = False
    
    def _change_trait(self, trait_type: str, trait_name: str, new_value: int, 
                     current_value: int = None) -> bool:
        """Handle trait changes with cost calculation and restrictions."""
        if self._updating or not self.character:
            return False
        
        char = self.character
        
        if current_value is None:
            if trait_type == "attribute":
                current_value = char.attributes.get(trait_name, 1)
            elif trait_type == "ability":
                current_value = char.abilities.get(trait_name, 0)
            elif trait_type == "background":
                current_value = char.backgrounds.get(trait_name, 0)
            elif trait_type == "rage":
                current_value = char.rage
            elif trait_type == "gnosis":
                current_value = char.gnosis
            elif trait_type == "willpower":
                current_value = char.willpower
            else:
                return False
        
        min_value = char.get_minimum_value(trait_type, trait_name)
        if new_value < min_value:
            widget = self.trait_widgets.get(f"{trait_type}_{trait_name}")
            if widget:
                self._updating = True
                widget.set_value(min_value)
                self._updating = False
            
            dialog = Adw.MessageDialog(
                transient_for=self.app.win,
                heading="Cannot Reduce Trait",
                body=f"Cannot reduce {trait_name} below {min_value} (set in previous mode)."
            )
            dialog.add_response("ok", "OK")
            dialog.present()
            return False
        
        if char.creation_mode == "freebie" and not self.app.tracker.storyteller_override:
            cost = char.calculate_freebie_cost(trait_type, trait_name, current_value, new_value)
            if cost > 0:
                if cost > char.freebie_points_available:
                    dialog = Adw.MessageDialog(
                        transient_for=self.app.win,
                        heading="Insufficient Freebie Points",
                        body=f"Need {cost} freebie points, but only {char.freebie_points_available} available."
                    )
                    dialog.add_response("ok", "OK")
                    dialog.present()
                    widget = self.trait_widgets.get(f"{trait_type}_{trait_name}")
                    if widget:
                        self._updating = True
                        widget.set_value(current_value)
                        self._updating = False
                    return False
                
                char.freebie_points_spent += cost
        
        elif char.creation_mode == "xp" and not self.app.tracker.storyteller_override:
            cost = char.calculate_xp_cost(trait_type, trait_name, current_value, new_value)
            if cost > 0:
                if cost > char.experience_available:
                    dialog = Adw.MessageDialog(
                        transient_for=self.app.win,
                        heading="Insufficient Experience Points",
                        body=f"Need {cost} XP, but only {char.experience_available} available."
                    )
                    dialog.add_response("ok", "OK")
                    dialog.present()
                    widget = self.trait_widgets.get(f"{trait_type}_{trait_name}")
                    if widget:
                        self._updating = True
                        widget.set_value(current_value)
                        self._updating = False
                    return False
                
                char.experience_spent += cost
        
        if trait_type == "attribute":
            char.attributes[trait_name] = new_value
        elif trait_type == "ability":
            if new_value > 0:
                char.abilities[trait_name] = new_value
            elif trait_name in char.abilities:
                del char.abilities[trait_name]
        elif trait_type == "background":
            if new_value > 0:
                char.backgrounds[trait_name] = new_value
            elif trait_name in char.backgrounds:
                del char.backgrounds[trait_name]
        elif trait_type == "rage":
            char.rage = new_value
            char.rage_current = min(char.rage_current, new_value)
        elif trait_type == "gnosis":
            char.gnosis = new_value
            char.gnosis_current = min(char.gnosis_current, new_value)
        elif trait_type == "willpower":
            char.willpower = new_value
            char.willpower_current = min(char.willpower_current, new_value)
        
        self.app.update_tracker()
        return True
    
    def _on_attribute_changed(self, name, value):
        self._change_trait("attribute", name, value)
    
    def _on_attribute_specialty_changed(self, name, specialty):
        """Handle attribute specialty changes."""
        if self._updating or not self.character:
            return
        if specialty:
            # Store as a list (like abilities)
            if name not in self.character.specialties:
                self.character.specialties[name] = []
            # Replace the list with a single specialty (or could support multiple)
            self.character.specialties[name] = [specialty] if specialty else []
        elif name in self.character.specialties:
            del self.character.specialties[name]
        self.app.update_tracker()
    
    def _on_ability_changed(self, name, value):
        self._change_trait("ability", name, value)
    
    def _on_ability_specialty_changed(self, name, specialty):
        """Handle ability specialty changes."""
        if self._updating or not self.character:
            return
        if specialty:
            # Parse comma-separated specialties
            specialties = [s.strip() for s in specialty.split(",") if s.strip()]
            self.character.specialties[name] = specialties
        elif name in self.character.specialties:
            del self.character.specialties[name]
        self.app.update_tracker()
    
    def _on_background_changed(self, name, value):
        self._change_trait("background", name, value)
    
    def _on_rage_changed(self, value):
        self._change_trait("rage", "Rage", value)
    
    def _on_gnosis_changed(self, value):
        self._change_trait("gnosis", "Gnosis", value)
    
    def _on_willpower_changed(self, value):
        self._change_trait("willpower", "Willpower", value)
    
    def _on_rank_changed(self, widget):
        if self._updating or not self.character:
            return
        self.character.rank = int(widget.get_value())
        self.app.update_tracker()
    
    def _on_renown_changed(self, renown_type, value):
        if self._updating or not self.character:
            return
        self.character.renown[renown_type] = value
        self.app.update_tracker()
    
    def _on_gift_toggled(self, widget, gift_name, gift_type, level):
        if self._updating or not self.character:
            return
        if widget.get_active():
            self.character.gifts[gift_name] = level
        elif gift_name in self.character.gifts:
            del self.character.gifts[gift_name]
        self._update_purchased_gifts_display()
        self.app.update_tracker()
    
    def _on_merit_toggled(self, widget, name, cost):
        if self._updating or not self.character:
            return
        if widget.get_active():
            self.character.merits[name] = cost
        elif name in self.character.merits:
            del self.character.merits[name]
        self.app.update_tracker()
    
    def _on_flaw_toggled(self, widget, name, bonus):
        if self._updating or not self.character:
            return
        if widget.get_active():
            self.character.flaws[name] = bonus
        elif name in self.character.flaws:
            del self.character.flaws[name]
        self.app.update_tracker()
    
    def _on_notes_changed(self, buffer):
        if self._updating or not self.character:
            return
        start, end = buffer.get_bounds()
        self.character.notes = buffer.get_text(start, end, False)
    
    def load_character(self, character: Character):
        """Load a character into the editor."""
        self._updating = True
        self.character = character
        
        # Set character type first (before updating breed/auspice/tribe dropdowns)
        char_type = getattr(character, 'character_type', 'Garou')
        # Find the display name for the character type
        for breed_key, breed_data in CHANGING_BREEDS.items():
            if breed_key == char_type:
                display_name = breed_data["display_name"]
                # Find and set the combo box using the model
                model = self.character_type_combo.get_model()
                if model:
                    for i, row in enumerate(model):
                        if row[0] == display_name:
                            self.character_type_combo.set_active(i)
                            break
                break
        
        # Rebuild forms section for the character type
        self._rebuild_forms_section(char_type)
        
        # Update purchased gifts display
        self._update_purchased_gifts_display()
        
        # Identity
        self.name_entry.set_text(character.name)
        self.player_entry.set_text(character.player)
        self.chronicle_entry.set_text(character.chronicle)
        
        self._set_combo_text(self.concept_combo, character.concept)
        self._set_combo_text(self.breed_combo, character.breed)
        self._set_combo_text(self.auspice_combo, character.auspice)
        self._set_combo_text(self.tribe_combo, character.tribe)
        self._set_combo_text(self.nature_combo, character.nature)
        self._set_combo_text(self.demeanor_combo, character.demeanor)
        
        # Update renown display for the character type
        self._update_renown_display()
        
        # Show/hide Metis deformity
        is_metis = (character.breed == "Metis")
        self.deformity_box.set_visible(is_metis)
        if is_metis:
            if character.breed in BREEDS and "deformities" in BREEDS[character.breed]:
                self.deformity_combo.remove_all()
                self.deformity_combo.append_text("")
                for deformity in BREEDS[character.breed]["deformities"]:
                    self.deformity_combo.append_text(deformity)
            self._set_combo_text(self.deformity_combo, character.metis_deformity)
        
        # Priorities
        priority_map = {"primary": 1, "secondary": 2, "tertiary": 3}
        for cat, priority in character.attribute_priorities.items():
            combo = self.attr_priority_combos.get(cat)
            if combo:
                combo.set_active(priority_map.get(priority, 0))
        
        for cat, priority in character.ability_priorities.items():
            combo = self.ability_priority_combos.get(cat)
            if combo:
                combo.set_active(priority_map.get(priority, 0))
        
        # Attributes
        for attr, value in character.attributes.items():
            widget = self.trait_widgets.get(f"attr_{attr}")
            if widget:
                widget.set_value(value)
                # Load specialty if it exists
                if attr in character.specialties and character.specialties[attr]:
                    # Specialties are stored as lists, get first one
                    specialty = character.specialties[attr][0] if isinstance(character.specialties[attr], list) else character.specialties[attr]
                    widget.set_specialty(specialty)
                else:
                    widget.set_specialty("")
        
        # Abilities
        for key, widget in self.trait_widgets.items():
            if key.startswith("ability_"):
                ability = key[8:]
                widget.set_value(character.abilities.get(ability, 0))
                # Load specialty if it exists
                if ability in character.specialties and character.specialties[ability]:
                    # Specialties are stored as lists
                    specialties = character.specialties[ability] if isinstance(character.specialties[ability], list) else [character.specialties[ability]]
                    widget.set_specialty(", ".join(specialties))
                else:
                    widget.set_specialty("")
        
        # Gifts display is updated via _update_purchased_gifts_display()
        
        # Backgrounds
        for key, widget in self.trait_widgets.items():
            if key.startswith("bg_"):
                bg = key[3:]
                widget.set_value(character.backgrounds.get(bg, 0))
        
        # Set starting traits based on breed/auspice/tribe if not already set
        # (This ensures traits are correct even if character was created without selecting breed/auspice/tribe)
        char_type = getattr(character, 'character_type', 'Garou')
        breed_data = CHANGING_BREEDS.get(char_type, CHANGING_BREEDS["Garou"])
        
        # Set Gnosis from breed (only if not already set or if breed explicitly sets it)
        if character.breed:
            breeds = breed_data.get("breeds", {})
            if character.breed in breeds and "initial_gnosis" in breeds[character.breed]:
                initial_gnosis = breeds[character.breed]["initial_gnosis"]
                if initial_gnosis > 0:  # Only set if positive
                    character.gnosis = initial_gnosis
        
        # Set Rage from auspice
        if character.auspice:
            auspices = breed_data.get("auspices", {})
            if character.auspice in auspices and "initial_rage" in auspices[character.auspice]:
                initial_rage = auspices[character.auspice]["initial_rage"]
                if initial_rage > 0:
                    character.rage = initial_rage
            # Some breeds have initial_gnosis in auspice
            if character.auspice in auspices and "initial_gnosis" in auspices[character.auspice]:
                initial_gnosis = auspices[character.auspice]["initial_gnosis"]
                if initial_gnosis > 0:  # Only set if positive
                    character.gnosis = initial_gnosis
            # Some breeds have initial_willpower in auspice
            if character.auspice in auspices and "initial_willpower" in auspices[character.auspice]:
                initial_willpower = auspices[character.auspice]["initial_willpower"]
                if initial_willpower > 0:
                    character.willpower = initial_willpower
        
        # Set Willpower from tribe
        if character.tribe:
            tribes = breed_data.get("tribes", {})
            if character.tribe in tribes:
                tribe_data = tribes[character.tribe]
                if "initial_willpower" in tribe_data:
                    initial_willpower = tribe_data["initial_willpower"]
                    if initial_willpower > 0:
                        character.willpower = initial_willpower
                if "initial_rage" in tribe_data:
                    initial_rage = tribe_data["initial_rage"]
                    if initial_rage > 0:
                        character.rage = initial_rage
                if "initial_gnosis" in tribe_data:
                    initial_gnosis = tribe_data["initial_gnosis"]
                    if initial_gnosis > 0:  # Only set if positive
                        character.gnosis = initial_gnosis
        
        # Check for fixed starting traits
        starting_traits = breed_data.get("starting_traits", {})
        if "rage" in starting_traits and isinstance(starting_traits["rage"], int):
            character.rage = starting_traits["rage"]
        if "gnosis" in starting_traits and isinstance(starting_traits["gnosis"], int):
            character.gnosis = starting_traits["gnosis"]
        if "willpower" in starting_traits and isinstance(starting_traits["willpower"], int):
            character.willpower = starting_traits["willpower"]
        
        # Core traits
        self.rage_dots.set_value(character.rage)
        self.gnosis_dots.set_value(character.gnosis)
        self.willpower_dots.set_value(character.willpower)
        self.rank_spin.set_value(character.rank)
        
        # Renown
        for renown_type in RENOWN_TYPES:
            widget = self.trait_widgets.get(f"renown_{renown_type}")
            if widget:
                widget.set_value(character.renown.get(renown_type, 0))
        
        # Merits and Flaws
        for name, check in self.merit_checks.items():
            check.set_active(name in character.merits)
        
        for name, check in self.flaw_checks.items():
            check.set_active(name in character.flaws)
        
        # Notes
        self.notes_text.get_buffer().set_text(character.notes)
        
        self._updating = False
    
    def _set_combo_text(self, combo, text):
        """Set combo box to show specific text."""
        model = combo.get_model()
        if model is None:
            return
        for i, row in enumerate(model):
            if row[0] == text:
                combo.set_active(i)
                return
        combo.set_active(0)


# Continue with ProgressTracker, CharacterList, and main app...
# (These sections will be similar to MageMaker but adapted for Werewolf)

class GiftPurchaseDialog(Adw.Window):
    """Dialog for purchasing gifts."""
    
    def __init__(self, parent, character: Character, editor):
        super().__init__()
        self.set_transient_for(parent)
        self.set_modal(True)
        self.set_title("Purchase Gifts")
        self.set_default_size(800, 600)
        
        self.character = character
        self.editor = editor
        self.gift_checks = {}
        
        # Main content
        content = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=16)
        content.set_margin_start(16)
        content.set_margin_end(16)
        content.set_margin_top(16)
        content.set_margin_bottom(16)
        
        # Header
        header_label = Gtk.Label(label="Select Gifts")
        header_label.add_css_class("title-2")
        content.append(header_label)
        
        # Create notebook for Breed, Auspice, and Tribe Gifts
        notebook = Gtk.Notebook()
        
        # Check what mode we're in
        show_all_levels = character and character.creation_mode == "xp"
        
        # Get character type and gift structure
        char_type = getattr(character, 'character_type', 'Garou')
        breed_data = CHANGING_BREEDS.get(char_type, CHANGING_BREEDS["Garou"])
        gifts_data = breed_data.get("gifts", {})
        
        # Get gift dictionaries
        breed_gifts = gifts_data.get("breed", BREED_GIFTS)
        auspice_gifts = gifts_data.get("auspice", AUSPICE_GIFTS)
        tribe_gifts = gifts_data.get("tribe", TRIBE_GIFTS)
        general_gifts = gifts_data.get("general", {})
        umbral_danser_gifts = gifts_data.get("umbral_danser", {})  # For Nuwisha
        
        # Breed Gifts tab
        breed_scroll = Gtk.ScrolledWindow()
        breed_scroll.set_min_content_height(400)
        breed_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        breed_box.set_margin_start(8)
        breed_box.set_margin_end(8)
        breed_box.set_margin_top(8)
        
        # Only show gifts for the character's breed if they have one
        if character.breed and breed_gifts:
            if isinstance(breed_gifts, dict) and character.breed in breed_gifts:
                gifts_dict = breed_gifts[character.breed]
                for level, gifts in sorted(gifts_dict.items()):
                    if show_all_levels or level == 1:
                        cat_label = Gtk.Label(label=f"{character.breed} Breed Gifts - Level {level}")
                        cat_label.add_css_class("heading")
                        cat_label.set_xalign(0)
                        breed_box.append(cat_label)
                        
                        for gift_name, gift_desc in gifts:
                            check_row = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
                            check = Gtk.CheckButton(label=gift_name)
                            check.set_tooltip_text(gift_desc)
                            check.connect("toggled", self._on_gift_toggled, gift_name, "breed", level)
                            self.gift_checks[f"breed_{gift_name}_{level}"] = check
                            # Set initial state
                            check.set_active(character.gifts.get(gift_name) == level)
                            check_row.append(check)
                            breed_box.append(check_row)
            elif isinstance(breed_gifts, dict):
                # Show all breeds (for Garou)
                for breed, gifts_dict in breed_gifts.items():
                    for level, gifts in sorted(gifts_dict.items()):
                        if show_all_levels or level == 1:
                            cat_label = Gtk.Label(label=f"{breed} Breed Gifts - Level {level}")
                            cat_label.add_css_class("heading")
                            cat_label.set_xalign(0)
                            breed_box.append(cat_label)
                            
                            for gift_name, gift_desc in gifts:
                                check_row = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
                                check = Gtk.CheckButton(label=gift_name)
                                check.set_tooltip_text(gift_desc)
                                check.connect("toggled", self._on_gift_toggled, gift_name, "breed", level)
                                self.gift_checks[f"breed_{gift_name}_{level}"] = check
                                # Set initial state
                                check.set_active(character.gifts.get(gift_name) == level)
                                check_row.append(check)
                                breed_box.append(check_row)
        
        breed_scroll.set_child(breed_box)
        notebook.append_page(breed_scroll, Gtk.Label(label="Breed Gifts"))
        
        # Auspice Gifts tab
        auspice_scroll = Gtk.ScrolledWindow()
        auspice_scroll.set_min_content_height(400)
        auspice_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        auspice_box.set_margin_start(8)
        auspice_box.set_margin_end(8)
        auspice_box.set_margin_top(8)
        
        # Only show gifts for the character's auspice if they have one
        if character.auspice and auspice_gifts:
            if isinstance(auspice_gifts, dict) and character.auspice in auspice_gifts:
                gifts_dict = auspice_gifts[character.auspice]
                for level, gifts in sorted(gifts_dict.items()):
                    if show_all_levels or level == 1:
                        cat_label = Gtk.Label(label=f"{character.auspice} Auspice Gifts - Level {level}")
                        cat_label.add_css_class("heading")
                        cat_label.set_xalign(0)
                        auspice_box.append(cat_label)
                        
                        for gift_name, gift_desc in gifts:
                            check_row = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
                            check = Gtk.CheckButton(label=gift_name)
                            check.set_tooltip_text(gift_desc)
                            check.connect("toggled", self._on_gift_toggled, gift_name, "auspice", level)
                            self.gift_checks[f"auspice_{gift_name}_{level}"] = check
                            # Set initial state
                            check.set_active(character.gifts.get(gift_name) == level)
                            check_row.append(check)
                            auspice_box.append(check_row)
            elif isinstance(auspice_gifts, dict):
                # Show all auspices (for Garou)
                for auspice, gifts_dict in auspice_gifts.items():
                    for level, gifts in sorted(gifts_dict.items()):
                        if show_all_levels or level == 1:
                            cat_label = Gtk.Label(label=f"{auspice} Auspice Gifts - Level {level}")
                            cat_label.add_css_class("heading")
                            cat_label.set_xalign(0)
                            auspice_box.append(cat_label)
                            
                            for gift_name, gift_desc in gifts:
                                check_row = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
                                check = Gtk.CheckButton(label=gift_name)
                                check.set_tooltip_text(gift_desc)
                                check.connect("toggled", self._on_gift_toggled, gift_name, "auspice", level)
                                self.gift_checks[f"auspice_{gift_name}_{level}"] = check
                                # Set initial state
                                check.set_active(character.gifts.get(gift_name) == level)
                                check_row.append(check)
                                auspice_box.append(check_row)
        
        auspice_scroll.set_child(auspice_box)
        notebook.append_page(auspice_scroll, Gtk.Label(label="Auspice Gifts"))
        
        # Tribe Gifts tab
        tribe_scroll = Gtk.ScrolledWindow()
        tribe_scroll.set_min_content_height(400)
        tribe_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        tribe_box.set_margin_start(8)
        tribe_box.set_margin_end(8)
        tribe_box.set_margin_top(8)
        
        # Only show gifts for the character's tribe if they have one
        if character.tribe and tribe_gifts:
            if isinstance(tribe_gifts, dict) and character.tribe in tribe_gifts:
                gifts_dict = tribe_gifts[character.tribe]
                for level, gifts in sorted(gifts_dict.items()):
                    if show_all_levels or level == 1:
                        cat_label = Gtk.Label(label=f"{character.tribe} Tribe Gifts - Level {level}")
                        cat_label.add_css_class("heading")
                        cat_label.set_xalign(0)
                        tribe_box.append(cat_label)
                        
                        for gift_name, gift_desc in gifts:
                            check_row = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
                            check = Gtk.CheckButton(label=gift_name)
                            check.set_tooltip_text(gift_desc)
                            check.connect("toggled", self._on_gift_toggled, gift_name, "tribe", level)
                            self.gift_checks[f"tribe_{gift_name}_{level}"] = check
                            # Set initial state
                            check.set_active(character.gifts.get(gift_name) == level)
                            check_row.append(check)
                            tribe_box.append(check_row)
            elif isinstance(tribe_gifts, dict):
                # Show all tribes (for Garou)
                for tribe, gifts_dict in tribe_gifts.items():
                    for level, gifts in sorted(gifts_dict.items()):
                        if show_all_levels or level == 1:
                            cat_label = Gtk.Label(label=f"{tribe} Tribe Gifts - Level {level}")
                            cat_label.add_css_class("heading")
                            cat_label.set_xalign(0)
                            tribe_box.append(cat_label)
                            
                            for gift_name, gift_desc in gifts:
                                check_row = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
                                check = Gtk.CheckButton(label=gift_name)
                                check.set_tooltip_text(gift_desc)
                                check.connect("toggled", self._on_gift_toggled, gift_name, "tribe", level)
                                self.gift_checks[f"tribe_{gift_name}_{level}"] = check
                                # Set initial state
                                check.set_active(character.gifts.get(gift_name) == level)
                                check_row.append(check)
                                tribe_box.append(check_row)
        
        # Add General Gifts tab if they exist
        if general_gifts:
            general_scroll = Gtk.ScrolledWindow()
            general_scroll.set_min_content_height(400)
            general_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
            general_box.set_margin_start(8)
            general_box.set_margin_end(8)
            general_box.set_margin_top(8)
            
            for level, gifts in sorted(general_gifts.items()):
                if show_all_levels or level == 1:
                    cat_label = Gtk.Label(label=f"General Gifts - Level {level}")
                    cat_label.add_css_class("heading")
                    cat_label.set_xalign(0)
                    general_box.append(cat_label)
                    
                    for gift_name, gift_desc in gifts:
                        check_row = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
                        check = Gtk.CheckButton(label=gift_name)
                        check.set_tooltip_text(gift_desc)
                        check.connect("toggled", self._on_gift_toggled, gift_name, "general", level)
                        self.gift_checks[f"general_{gift_name}_{level}"] = check
                        # Set initial state
                        check.set_active(character.gifts.get(gift_name) == level)
                        check_row.append(check)
                        general_box.append(check_row)
            
            general_scroll.set_child(general_box)
            notebook.append_page(general_scroll, Gtk.Label(label="General Gifts"))
        
        # Add Umbral Danser Gifts tab for Nuwisha if they exist
        if umbral_danser_gifts:
            umbral_scroll = Gtk.ScrolledWindow()
            umbral_scroll.set_min_content_height(400)
            umbral_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
            umbral_box.set_margin_start(8)
            umbral_box.set_margin_end(8)
            umbral_box.set_margin_top(8)
            
            for level, gifts in sorted(umbral_danser_gifts.items()):
                if show_all_levels or level == 1:
                    cat_label = Gtk.Label(label=f"Umbral Danser Gifts - Level {level}")
                    cat_label.add_css_class("heading")
                    cat_label.set_xalign(0)
                    umbral_box.append(cat_label)
                    
                    for gift_name, gift_desc in gifts:
                        check_row = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
                        check = Gtk.CheckButton(label=gift_name)
                        check.set_tooltip_text(gift_desc)
                        check.connect("toggled", self._on_gift_toggled, gift_name, "umbral_danser", level)
                        self.gift_checks[f"umbral_danser_{gift_name}_{level}"] = check
                        # Set initial state
                        check.set_active(character.gifts.get(gift_name) == level)
                        check_row.append(check)
                        umbral_box.append(check_row)
            
            umbral_scroll.set_child(umbral_box)
            notebook.append_page(umbral_scroll, Gtk.Label(label="Umbral Danser Gifts"))
        
        tribe_scroll.set_child(tribe_box)
        notebook.append_page(tribe_scroll, Gtk.Label(label="Tribe Gifts"))
        
        # Add Wyrmish tabs if character is Black Spiral Dancer
        if character.tribe == "Black Spiral Dancers":
            # Wyrmish Breed Gifts tab
            wyrmish_breed_scroll = Gtk.ScrolledWindow()
            wyrmish_breed_scroll.set_min_content_height(400)
            wyrmish_breed_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
            wyrmish_breed_box.set_margin_start(8)
            wyrmish_breed_box.set_margin_end(8)
            wyrmish_breed_box.set_margin_top(8)
            
            for breed, gifts_dict in WYRMISH_BREED_GIFTS.items():
                for level, gifts in sorted(gifts_dict.items()):
                    if show_all_levels or level == 1:
                        cat_label = Gtk.Label(label=f"Wyrmish {breed} Breed Gifts - Level {level}")
                        cat_label.add_css_class("heading")
                        cat_label.set_xalign(0)
                        wyrmish_breed_box.append(cat_label)
                        
                        for gift_name, gift_desc in gifts:
                            check_row = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
                            check = Gtk.CheckButton(label=gift_name)
                            check.set_tooltip_text(gift_desc)
                            check.connect("toggled", self._on_gift_toggled, gift_name, "breed", level)
                            self.gift_checks[f"wyrmish_breed_{gift_name}_{level}"] = check
                            # Set initial state
                            check.set_active(character.gifts.get(gift_name) == level)
                            check_row.append(check)
                            wyrmish_breed_box.append(check_row)
            
            wyrmish_breed_scroll.set_child(wyrmish_breed_box)
            notebook.append_page(wyrmish_breed_scroll, Gtk.Label(label="Wyrmish Breed Gifts"))
            
            # Wyrmish Auspice Gifts tab
            wyrmish_auspice_scroll = Gtk.ScrolledWindow()
            wyrmish_auspice_scroll.set_min_content_height(400)
            wyrmish_auspice_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
            wyrmish_auspice_box.set_margin_start(8)
            wyrmish_auspice_box.set_margin_end(8)
            wyrmish_auspice_box.set_margin_top(8)
            
            for auspice, gifts_dict in WYRMISH_AUSPICE_GIFTS.items():
                for level, gifts in sorted(gifts_dict.items()):
                    if show_all_levels or level == 1:
                        cat_label = Gtk.Label(label=f"Wyrmish {auspice} Auspice Gifts - Level {level}")
                        cat_label.add_css_class("heading")
                        cat_label.set_xalign(0)
                        wyrmish_auspice_box.append(cat_label)
                        
                        for gift_name, gift_desc in gifts:
                            check_row = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
                            check = Gtk.CheckButton(label=gift_name)
                            check.set_tooltip_text(gift_desc)
                            check.connect("toggled", self._on_gift_toggled, gift_name, "auspice", level)
                            self.gift_checks[f"wyrmish_auspice_{gift_name}_{level}"] = check
                            # Set initial state
                            check.set_active(character.gifts.get(gift_name) == level)
                            check_row.append(check)
                            wyrmish_auspice_box.append(check_row)
            
            wyrmish_auspice_scroll.set_child(wyrmish_auspice_box)
            notebook.append_page(wyrmish_auspice_scroll, Gtk.Label(label="Wyrmish Auspice Gifts"))
        
        content.append(notebook)
        
        # Close button
        button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        button_box.set_halign(Gtk.Align.END)
        close_btn = Gtk.Button(label="Close")
        close_btn.connect("clicked", lambda b: self.close())
        button_box.append(close_btn)
        content.append(button_box)
        
        self.set_content(content)
    
    def _on_gift_toggled(self, widget, gift_name, gift_type, level):
        """Handle gift checkbox toggle."""
        if widget.get_active():
            self.character.gifts[gift_name] = level
        elif gift_name in self.character.gifts:
            del self.character.gifts[gift_name]
        
        # Update the purchased gifts display in the editor
        self.editor._update_purchased_gifts_display()
        self.editor.app.update_tracker()


class ProgressTracker(Gtk.Box):
    """Right sidebar showing progress through character creation."""
    
    def __init__(self, app):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        self.app = app
        self.set_margin_start(12)
        self.set_margin_end(12)
        self.set_margin_top(12)
        self.set_margin_bottom(12)
        
        self.mode_label = Gtk.Label(label="Creation Mode")
        self.mode_label.add_css_class("title-3")
        self.append(self.mode_label)
        
        self.mode_button = Gtk.Button(label="Advance to Freebie Mode")
        self.mode_button.connect("clicked", self._on_mode_advance)
        self.append(self.mode_button)
        
        self.append(Gtk.Separator())
        
        self.progress_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        self.append(self.progress_box)
        
        self.xp_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        self.xp_label = Gtk.Label()
        self.xp_label.set_xalign(0)
        self.xp_box.append(self.xp_label)
        
        xp_entry_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=4)
        xp_entry_label = Gtk.Label(label="Add XP:")
        self.xp_entry = Gtk.SpinButton.new_with_range(0, 1000, 1)
        xp_add_btn = Gtk.Button(label="Add")
        xp_add_btn.connect("clicked", self._on_add_xp)
        xp_entry_box.append(xp_entry_label)
        xp_entry_box.append(self.xp_entry)
        xp_entry_box.append(xp_add_btn)
        self.xp_box.append(xp_entry_box)
        
        self.xp_box.append(Gtk.Separator())
        
        override_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        override_header = Gtk.Label(label="Storyteller Override")
        override_header.add_css_class("heading")
        override_header.set_xalign(0)
        override_box.append(override_header)
        
        override_desc = Gtk.Label(label="Enable to change stats directly\nwithout spending XP (for ST-\ndictated changes, curses, etc.)")
        override_desc.set_xalign(0)
        override_desc.add_css_class("dim-label")
        override_box.append(override_desc)
        
        self.override_switch = Gtk.Switch()
        self.override_switch.set_halign(Gtk.Align.START)
        self.override_switch.connect("state-set", self._on_override_toggled)
        
        switch_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        switch_label = Gtk.Label(label="Force Edit Mode:")
        switch_box.append(switch_label)
        switch_box.append(self.override_switch)
        override_box.append(switch_box)
        
        self.xp_box.append(override_box)
        
        self.xp_box.set_visible(False)
        self.append(self.xp_box)
        
        self.storyteller_override = False
    
    def _on_mode_advance(self, button):
        if not self.app.current_character:
            return
        
        char = self.app.current_character
        
        can_advance, warnings = char.can_advance_mode()
        
        if not can_advance:
            dialog = Adw.MessageDialog(
                transient_for=self.app.win,
                heading="Cannot Advance Mode",
                body="Please resolve all issues before advancing:\n\n" + "\n".join(f"• {w}" for w in warnings)
            )
            dialog.add_response("ok", "OK")
            dialog.present()
            return
        
        char.snapshot_baseline()
        
        if char.creation_mode == "creation":
            char.creation_mode = "freebie"
            self.mode_button.set_label("Advance to XP Mode")
        elif char.creation_mode == "freebie":
            char.creation_mode = "xp"
            self.mode_button.set_label("(In XP Mode)")
            self.mode_button.set_sensitive(False)
        
        # Update purchased gifts display (in case mode change affects visibility)
        self.app.editor._update_purchased_gifts_display()
        self.update()
    
    def _on_add_xp(self, button):
        if not self.app.current_character:
            return
        
        amount = int(self.xp_entry.get_value())
        if amount > 0:
            self.app.current_character.experience_total += amount
            self.xp_entry.set_value(0)
            self.update()
    
    def _on_override_toggled(self, switch, state):
        self.storyteller_override = state
        if state:
            self.mode_label.set_label("XP Mode (OVERRIDE)")
            self.mode_label.add_css_class("warning")
        else:
            self.mode_label.set_label("Experience Mode")
            self.mode_label.remove_css_class("warning")
        return False
    
    def update(self):
        """Update the tracker display."""
        while child := self.progress_box.get_first_child():
            self.progress_box.remove(child)
        
        if not self.app.current_character:
            return
        
        char = self.app.current_character
        
        mode_names = {"creation": "Creation Mode", "freebie": "Freebie Point Mode", "xp": "Experience Mode"}
        
        self.mode_label.remove_css_class("warning")
        
        if char.creation_mode == "xp" and self.storyteller_override:
            self.mode_label.set_label("XP Mode (OVERRIDE)")
            self.mode_label.add_css_class("warning")
        else:
            self.mode_label.set_label(mode_names.get(char.creation_mode, "Unknown"))
        
        if char.creation_mode == "creation":
            self._show_creation_progress(char)
            self.mode_button.set_label("Advance to Freebie Mode")
            self.mode_button.set_sensitive(True)
            self.xp_box.set_visible(False)
            self.storyteller_override = False
            self.override_switch.set_active(False)
            
        elif char.creation_mode == "freebie":
            self._show_freebie_progress(char)
            self.mode_button.set_label("Advance to XP Mode")
            self.mode_button.set_sensitive(True)
            self.xp_box.set_visible(False)
            self.storyteller_override = False
            self.override_switch.set_active(False)
            
        elif char.creation_mode == "xp":
            self._show_xp_progress(char)
            self.mode_button.set_label("(In XP Mode)")
            self.mode_button.set_sensitive(False)
            self.xp_box.set_visible(True)
    
    def _show_creation_progress(self, char: Character):
        """Show creation mode progress."""
        remaining = char.get_creation_dots_remaining()
        
        header = Gtk.Label(label="Attributes")
        header.add_css_class("heading")
        header.set_xalign(0)
        self.progress_box.append(header)
        
        for category in ["Physical", "Social", "Mental"]:
            priority = char.attribute_priorities.get(category)
            priority_str = f" ({priority})" if priority else ""
            dots = remaining["attributes"][category]
            color = "success" if dots == 0 else ("warning" if dots > 0 else "error")
            
            label = Gtk.Label(label=f"  {category}{priority_str}: {dots}")
            label.set_xalign(0)
            label.add_css_class(color)
            self.progress_box.append(label)
        
        self.progress_box.append(Gtk.Separator())
        
        header = Gtk.Label(label="Abilities")
        header.add_css_class("heading")
        header.set_xalign(0)
        self.progress_box.append(header)
        
        for category in ["Talents", "Skills", "Knowledges"]:
            priority = char.ability_priorities.get(category)
            priority_str = f" ({priority})" if priority else ""
            dots = remaining["abilities"][category]
            color = "success" if dots == 0 else ("warning" if dots > 0 else "error")
            
            label = Gtk.Label(label=f"  {category}{priority_str}: {dots}")
            label.set_xalign(0)
            label.add_css_class(color)
            self.progress_box.append(label)
        
        self.progress_box.append(Gtk.Separator())
        
        bg_dots = remaining["backgrounds"]
        bg_color = "success" if bg_dots == 0 else ("warning" if bg_dots > 0 else "error")
        bg_label = Gtk.Label(label=f"Backgrounds: {bg_dots}")
        bg_label.set_xalign(0)
        bg_label.add_css_class(bg_color)
        self.progress_box.append(bg_label)
        
        # Check breed, auspice, tribe
        if not char.breed:
            breed_label = Gtk.Label(label="⚠ No Breed selected")
            breed_label.set_xalign(0)
            breed_label.add_css_class("warning")
            self.progress_box.append(breed_label)
        
        if not char.auspice:
            auspice_label = Gtk.Label(label="⚠ No Auspice selected")
            auspice_label.set_xalign(0)
            auspice_label.add_css_class("warning")
            self.progress_box.append(auspice_label)
        
        if not char.tribe:
            tribe_label = Gtk.Label(label="⚠ No Tribe selected")
            tribe_label.set_xalign(0)
            tribe_label.add_css_class("warning")
            self.progress_box.append(tribe_label)
        
        # Check starting gifts
        if len(char.gifts) < 3:
            gift_label = Gtk.Label(label=f"⚠ Gifts: {3 - len(char.gifts)} starting gift(s) missing")
            gift_label.set_xalign(0)
            gift_label.add_css_class("warning")
            self.progress_box.append(gift_label)
        
        can_advance, warnings = char.can_advance_mode()
        if not can_advance and warnings:
            self.progress_box.append(Gtk.Separator())
            warning_header = Gtk.Label(label="⚠ Cannot Advance Mode")
            warning_header.add_css_class("heading")
            warning_header.add_css_class("error")
            warning_header.set_xalign(0)
            self.progress_box.append(warning_header)
            
            for warning in warnings:
                warn_label = Gtk.Label(label=f"  • {warning}")
                warn_label.set_xalign(0)
                warn_label.add_css_class("error")
                self.progress_box.append(warn_label)
    
    def _show_freebie_progress(self, char: Character):
        """Show freebie point mode progress."""
        available = char.freebie_points_available
        total = char.freebie_points_total
        
        avail_color = "success" if available >= 0 else "error"
        header = Gtk.Label(label=f"Freebie Points: {available}/{total}")
        header.add_css_class("heading")
        header.add_css_class(avail_color)
        header.set_xalign(0)
        self.progress_box.append(header)
        
        base_label = Gtk.Label(label=f"  Base: {CREATION_RULES['freebie_points']}")
        base_label.set_xalign(0)
        self.progress_box.append(base_label)
        
        flaw_bonus = min(sum(char.flaws.values()), CREATION_RULES["max_flaw_points"])
        flaw_label = Gtk.Label(label=f"  Flaws (bonus): +{flaw_bonus}")
        flaw_label.set_xalign(0)
        flaw_label.add_css_class("success")
        self.progress_box.append(flaw_label)
        
        merit_cost = char.merit_costs
        merit_label = Gtk.Label(label=f"  Merits (cost): -{merit_cost}")
        merit_label.set_xalign(0)
        if merit_cost > 0:
            merit_label.add_css_class("warning")
        self.progress_box.append(merit_label)
        
        spent_label = Gtk.Label(label=f"  Other spent: -{char.freebie_points_spent}")
        spent_label.set_xalign(0)
        self.progress_box.append(spent_label)
        
        self.progress_box.append(Gtk.Separator())
        
        ref_header = Gtk.Label(label="Freebie Costs:")
        ref_header.add_css_class("heading")
        ref_header.set_xalign(0)
        self.progress_box.append(ref_header)
        
        costs = [
            ("Attribute", FREEBIE_COSTS["attribute"]),
            ("Ability", FREEBIE_COSTS["ability"]),
            ("Background", FREEBIE_COSTS["background"]),
            ("Gift", FREEBIE_COSTS["gift"]),
            ("Rage", FREEBIE_COSTS["rage"]),
            ("Gnosis", FREEBIE_COSTS["gnosis"]),
            ("Willpower", FREEBIE_COSTS["willpower"]),
        ]
        
        for name, cost in costs:
            label = Gtk.Label(label=f"  {name}: {cost}/dot")
            label.set_xalign(0)
            self.progress_box.append(label)
        
        can_advance, warnings = char.can_advance_mode()
        if not can_advance and warnings:
            self.progress_box.append(Gtk.Separator())
            warning_header = Gtk.Label(label="⚠ Cannot Advance Mode")
            warning_header.add_css_class("heading")
            warning_header.add_css_class("error")
            warning_header.set_xalign(0)
            self.progress_box.append(warning_header)
            
            for warning in warnings:
                warn_label = Gtk.Label(label=f"  • {warning}")
                warn_label.set_xalign(0)
                warn_label.add_css_class("error")
                self.progress_box.append(warn_label)
    
    def _show_xp_progress(self, char: Character):
        """Show XP mode progress."""
        self.xp_label.set_label(
            f"Total XP: {char.experience_total}\n"
            f"Spent: {char.experience_spent}\n"
            f"Available: {char.experience_available}"
        )
        
        if self.storyteller_override:
            override_label = Gtk.Label(label="⚠ OVERRIDE MODE ACTIVE")
            override_label.add_css_class("warning")
            override_label.set_xalign(0)
            self.progress_box.append(override_label)
            
            override_info = Gtk.Label(label="Changes do not cost XP")
            override_info.set_xalign(0)
            self.progress_box.append(override_info)
            
            self.progress_box.append(Gtk.Separator())
        
        header = Gtk.Label(label="XP Costs:")
        header.add_css_class("heading")
        header.set_xalign(0)
        self.progress_box.append(header)
        
        costs = [
            ("New Ability", str(EXPERIENCE_COSTS["new_ability"])),
            ("New Gift", str(EXPERIENCE_COSTS["new_gift"])),
            ("Attribute", f"current × {EXPERIENCE_COSTS['attribute']}"),
            ("Ability", f"current × {EXPERIENCE_COSTS['ability']}"),
            ("Background", f"current × {EXPERIENCE_COSTS['background']}"),
            ("Willpower", f"current × {EXPERIENCE_COSTS['willpower']}"),
            ("Rage", f"current × {EXPERIENCE_COSTS['rage']}"),
            ("Gnosis", f"current × {EXPERIENCE_COSTS['gnosis']}"),
            ("Renown", f"current × {EXPERIENCE_COSTS['renown']}"),
        ]
        
        for name, cost in costs:
            label = Gtk.Label(label=f"  {name}: {cost}")
            label.set_xalign(0)
            self.progress_box.append(label)


class CharacterList(Gtk.Box):
    """Left sidebar showing saved characters."""
    
    def __init__(self, app):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        self.app = app
        self.set_margin_start(12)
        self.set_margin_end(12)
        self.set_margin_top(12)
        self.set_margin_bottom(12)
        
        header = Gtk.Label(label="Characters")
        header.add_css_class("title-3")
        self.append(header)
        
        new_btn = Gtk.Button(label="New Character")
        new_btn.connect("clicked", self._on_new_character)
        self.append(new_btn)
        
        self.append(Gtk.Separator())
        
        scrolled = Gtk.ScrolledWindow()
        scrolled.set_vexpand(True)
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        
        self.listbox = Gtk.ListBox()
        self.listbox.set_selection_mode(Gtk.SelectionMode.SINGLE)
        self.listbox.connect("row-selected", self._on_character_selected)
        scrolled.set_child(self.listbox)
        
        self.append(scrolled)
        
        refresh_btn = Gtk.Button(label="Refresh")
        refresh_btn.connect("clicked", lambda b: self.refresh_list())
        self.append(refresh_btn)
    
    def _on_new_character(self, button):
        self.app.new_character()
    
    def _on_character_selected(self, listbox, row):
        if row is None:
            return
        
        filepath = row.filepath
        self.app.load_character(filepath)
    
    def refresh_list(self):
        """Refresh the character list from the save directory."""
        while child := self.listbox.get_first_child():
            self.listbox.remove(child)
        
        save_dir = self.app.save_directory
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
            return
        
        for filename in sorted(os.listdir(save_dir)):
            if filename.endswith(".md"):
                filepath = os.path.join(save_dir, filename)
                
                try:
                    char = Character.load_from_markdown(filepath)
                    name = char.name
                except:
                    name = filename[:-3]
                
                row = Gtk.ListBoxRow()
                row.filepath = filepath
                
                box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
                box.set_margin_start(4)
                box.set_margin_end(4)
                box.set_margin_top(4)
                box.set_margin_bottom(4)
                
                label = Gtk.Label(label=name)
                label.set_xalign(0)
                label.set_hexpand(True)
                box.append(label)
                
                row.set_child(box)
                self.listbox.append(row)


class KinfolkApp(Adw.Application):
    """Main application class."""
    
    def __init__(self):
        super().__init__(application_id="org.kinfolk.Kinfolk",
                        flags=Gio.ApplicationFlags.FLAGS_NONE)
        
        self.current_character = None
        self.current_filepath = None
        
        cwd = os.getcwd()
        self.save_directory = os.path.join(cwd, "characters")
        os.makedirs(self.save_directory, exist_ok=True)
        
        self.connect("activate", self.on_activate)
    
    def on_activate(self, app):
        self.win = Adw.ApplicationWindow(application=app)
        self.win.set_title("Kinfolk - Werewolf: The Apocalypse 20th Anniversary Edition")
        self.win.set_default_size(1400, 900)
        
        self._apply_css()
        
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        
        header = Adw.HeaderBar()
        
        save_btn = Gtk.Button(label="Save")
        save_btn.connect("clicked", self._on_save)
        header.pack_start(save_btn)
        
        export_btn = Gtk.Button(label="Export TXT")
        export_btn.connect("clicked", self._on_export)
        header.pack_end(export_btn)
        
        main_box.append(header)
        
        paned_outer = Gtk.Paned(orientation=Gtk.Orientation.HORIZONTAL)
        paned_outer.set_vexpand(True)
        
        self.char_list = CharacterList(self)
        self.char_list.set_size_request(200, -1)
        
        left_frame = Gtk.Frame()
        left_frame.set_child(self.char_list)
        paned_outer.set_start_child(left_frame)
        paned_outer.set_shrink_start_child(False)
        
        paned_inner = Gtk.Paned(orientation=Gtk.Orientation.HORIZONTAL)
        
        self.editor = CharacterEditor(self)
        
        center_frame = Gtk.Frame()
        center_frame.set_child(self.editor)
        center_frame.set_hexpand(True)
        paned_inner.set_start_child(center_frame)
        paned_inner.set_shrink_start_child(False)
        
        self.tracker = ProgressTracker(self)
        self.tracker.set_size_request(250, -1)
        
        right_frame = Gtk.Frame()
        right_frame.set_child(self.tracker)
        paned_inner.set_end_child(right_frame)
        paned_inner.set_shrink_end_child(False)
        
        paned_outer.set_end_child(paned_inner)
        paned_outer.set_shrink_end_child(False)
        
        main_box.append(paned_outer)
        
        self.win.set_content(main_box)
        
        self.char_list.refresh_list()
        
        self.new_character()
        
        self.win.present()
    
    def _apply_css(self):
        """Apply custom CSS styling."""
        css = b"""
        .title-2 {
            font-size: 16pt;
            font-weight: bold;
        }
        .title-3 {
            font-size: 14pt;
            font-weight: bold;
        }
        .heading {
            font-weight: bold;
            margin-top: 8px;
        }
        .dot-button {
            min-width: 20px;
            min-height: 20px;
            padding: 0;
        }
        .dot-filled {
            color: @accent_color;
        }
        .dot-empty {
            color: alpha(@window_fg_color, 0.3);
        }
        .success {
            color: #2ec27e;
        }
        .warning {
            color: #e5a50a;
        }
        .error {
            color: #c01c28;
        }
        """
        
        provider = Gtk.CssProvider()
        provider.load_from_data(css)
        Gtk.StyleContext.add_provider_for_display(
            self.win.get_display(),
            provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
    
    def new_character(self):
        """Create a new character."""
        self.current_character = Character()
        self.current_filepath = None
        self.editor.load_character(self.current_character)
        self.update_tracker()
    
    def load_character(self, filepath: str):
        """Load a character from file."""
        try:
            self.current_character = Character.load_from_markdown(filepath)
            self.current_filepath = filepath
            self.editor.load_character(self.current_character)
            self.update_tracker()
        except Exception as e:
            dialog = Adw.MessageDialog(
                transient_for=self.win,
                heading="Error Loading Character",
                body=str(e)
            )
            dialog.add_response("ok", "OK")
            dialog.present()
    
    def _on_save(self, button):
        """Save current character."""
        if not self.current_character:
            return
        
        if not self.current_filepath:
            safe_name = "".join(c for c in self.current_character.name if c.isalnum() or c in " -_").strip()
            if not safe_name:
                safe_name = "New Character"
            self.current_filepath = os.path.join(self.save_directory, f"{safe_name}.md")
        
        try:
            self.current_character.save_to_markdown(self.current_filepath)
            self.char_list.refresh_list()
        except Exception as e:
            dialog = Adw.MessageDialog(
                transient_for=self.win,
                heading="Error Saving Character",
                body=str(e)
            )
            dialog.add_response("ok", "OK")
            dialog.present()
    
    def _on_export(self, button):
        """Export character to TXT."""
        if not self.current_character:
            return
        
        dialog = Gtk.FileDialog()
        dialog.set_initial_name(f"{self.current_character.name}.txt")
        
        def on_save_response(dialog, result):
            try:
                file = dialog.save_finish(result)
                if file:
                    filepath = file.get_path()
                    # Save as markdown (can add text export later)
                    self.current_character.save_to_markdown(filepath)
            except GLib.Error:
                pass
        
        dialog.save(self.win, None, on_save_response)
    
    def update_tracker(self):
        """Update the progress tracker."""
        self.tracker.update()


def main():
    """Entry point for the application."""
    app = KinfolkApp()
    app.run(None)


if __name__ == "__main__":
    main()
