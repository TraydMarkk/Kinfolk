"""
Character model for Werewolf: The Apocalypse 20th Anniversary Edition
"""

import json
import os
from datetime import datetime
from typing import Optional
from dataclasses import dataclass, field
from .data import (
    ATTRIBUTES, PRIMARY_ABILITIES, SECONDARY_ABILITIES,
    BACKGROUNDS, BREEDS, AUSPICES, TRIBES, FORMS,
    CREATION_RULES, FREEBIE_COSTS, EXPERIENCE_COSTS, RENOWN_TYPES
)


@dataclass
class Character:
    """Represents a Werewolf character."""
    
    # Identity
    name: str = "New Character"
    player: str = ""
    chronicle: str = ""
    concept: str = ""
    
    # Character Type
    character_type: str = "Garou"  # Garou, Ajaba, Ananasi, Bastet, Corax, Gurahl, Kitsune, Mokolé, Nagah, Nuwisha, Ratkin, Rokea
    
    # Werewolf/Changing Breed Identity
    breed: str = ""  # Homid, Metis, Lupus (or breed-specific names)
    auspice: str = ""  # Ragabash, Theurge, Philodox, Galliard, Ahroun (or auspice-specific names)
    tribe: str = ""  # Tribe name (or faction/stream/etc. for other breeds)
    metis_deformity: str = ""  # Only for Metis (or breed-specific deformity)
    
    # Nature and Demeanor
    nature: str = ""
    demeanor: str = ""
    
    # Attributes (dict of attribute name -> rating)
    attributes: dict = field(default_factory=lambda: {
        attr: 1 for category in ATTRIBUTES.values() for attr in category
    })
    
    # Priority assignments for creation mode
    attribute_priorities: dict = field(default_factory=lambda: {
        "Physical": None, "Social": None, "Mental": None
    })
    ability_priorities: dict = field(default_factory=lambda: {
        "Talents": None, "Skills": None, "Knowledges": None
    })
    
    # Abilities (dict of ability name -> rating)
    abilities: dict = field(default_factory=dict)
    
    # Specialties (dict of trait name -> list of specialties)
    specialties: dict = field(default_factory=dict)
    
    # Gifts (dict of gift name -> level)
    gifts: dict = field(default_factory=dict)
    
    # Backgrounds (dict of background name -> rating)
    backgrounds: dict = field(default_factory=dict)
    
    # Core traits
    rage: int = 1
    rage_current: int = 1
    gnosis: int = 1
    gnosis_current: int = 1
    willpower: int = 3
    willpower_current: int = 3
    
    # Renown (dict of type -> rating)
    renown: dict = field(default_factory=lambda: {
        "Glory": 0, "Honor": 0, "Wisdom": 0
    })
    rank: int = 1  # Starting rank is 1 (cliath)
    
    # Health
    health_levels: dict = field(default_factory=lambda: {
        "Bruised": False, "Hurt": False, "Injured": False,
        "Wounded": False, "Mauled": False, "Crippled": False,
        "Incapacitated": False
    })
    
    # Merits and Flaws (dict of name -> cost/bonus)
    merits: dict = field(default_factory=dict)
    flaws: dict = field(default_factory=dict)
    
    # Experience
    experience_total: int = 0
    experience_spent: int = 0
    experience_log: list = field(default_factory=list)
    
    # Character creation tracking
    creation_mode: str = "creation"  # creation, freebie, xp
    freebie_points_spent: int = 0
    
    # Track baseline values from previous modes (cannot be reduced below these)
    creation_baselines: dict = field(default_factory=dict)  # trait_name -> value
    freebie_baselines: dict = field(default_factory=dict)   # trait_name -> value
    
    # Metadata
    created_date: str = field(default_factory=lambda: datetime.now().isoformat())
    modified_date: str = field(default_factory=lambda: datetime.now().isoformat())
    notes: str = ""
    
    def __post_init__(self):
        """Initialize abilities to empty if not set."""
        if not self.abilities:
            self.abilities = {}
    
    @property
    def experience_available(self) -> int:
        """Get available experience points."""
        return self.experience_total - self.experience_spent
    
    @property
    def freebie_points_total(self) -> int:
        """Get total freebie points including flaws (flaws add points)."""
        base = CREATION_RULES["freebie_points"]
        flaw_bonus = min(sum(self.flaws.values()), CREATION_RULES["max_flaw_points"])
        return base + flaw_bonus
    
    @property
    def merit_costs(self) -> int:
        """Get total cost of merits (merits cost freebie points)."""
        return sum(self.merits.values())
    
    @property
    def freebie_points_available(self) -> int:
        """Get remaining freebie points (merits subtract from available)."""
        return self.freebie_points_total - self.freebie_points_spent - self.merit_costs
    
    @property
    def total_renown(self) -> int:
        """Get total renown points."""
        return sum(self.renown.values())
    
    def get_attribute_category(self, attr_name: str) -> Optional[str]:
        """Get the category for an attribute."""
        for category, attrs in ATTRIBUTES.items():
            if attr_name in attrs:
                return category
        return None
    
    def get_ability_category(self, ability_name: str) -> Optional[str]:
        """Get the category for an ability."""
        for category, abilities in PRIMARY_ABILITIES.items():
            if ability_name in abilities:
                return category
        for category, abilities in SECONDARY_ABILITIES.items():
            if ability_name in abilities:
                return category
        return None
    
    def get_form_modifiers(self, form_name: str) -> dict:
        """Get attribute modifiers for a specific form."""
        if form_name in FORMS:
            return FORMS[form_name]["statistics_adjustment"].copy()
        return {attr: 0 for attr in ["Strength", "Dexterity", "Stamina", 
                                     "Charisma", "Manipulation", "Appearance",
                                     "Perception", "Intelligence", "Wits"]}
    
    def get_attributes_in_form(self, form_name: str) -> dict:
        """Get effective attributes in a specific form."""
        base_attrs = self.attributes.copy()
        modifiers = self.get_form_modifiers(form_name)
        effective = {}
        for attr, base_value in base_attrs.items():
            effective[attr] = max(1, base_value + modifiers.get(attr, 0))
        return effective
    
    def calculate_creation_dots_spent(self) -> dict:
        """Calculate dots spent in creation mode for each category."""
        result = {
            "attributes": {"Physical": 0, "Social": 0, "Mental": 0},
            "abilities": {"Talents": 0, "Skills": 0, "Knowledges": 0},
            "backgrounds": 0
        }
        
        # Count attribute dots (minus base 1)
        for category, attrs in ATTRIBUTES.items():
            for attr in attrs:
                result["attributes"][category] += max(0, self.attributes.get(attr, 1) - 1)
        
        # Count ability dots
        for ability, rating in self.abilities.items():
            category = self.get_ability_category(ability)
            if category:
                result["abilities"][category] += rating
        
        # Count background dots
        for bg, rating in self.backgrounds.items():
            result["backgrounds"] += rating
        
        return result
    
    def get_creation_dots_remaining(self) -> dict:
        """Get remaining dots to spend in creation mode."""
        spent = self.calculate_creation_dots_spent()
        rules = CREATION_RULES
        
        # Determine attribute allowances based on priorities
        attr_allowances = {"Physical": 0, "Social": 0, "Mental": 0}
        priority_values = {"primary": rules["attributes"]["primary"],
                         "secondary": rules["attributes"]["secondary"],
                         "tertiary": rules["attributes"]["tertiary"]}
        
        for category, priority in self.attribute_priorities.items():
            if priority:
                attr_allowances[category] = priority_values.get(priority, 0)
        
        # Determine ability allowances based on priorities
        ability_allowances = {"Talents": 0, "Skills": 0, "Knowledges": 0}
        priority_values_abilities = {"primary": rules["abilities"]["primary"],
                                    "secondary": rules["abilities"]["secondary"],
                                    "tertiary": rules["abilities"]["tertiary"]}
        
        for category, priority in self.ability_priorities.items():
            if priority:
                ability_allowances[category] = priority_values_abilities.get(priority, 0)
        
        return {
            "attributes": {
                cat: attr_allowances[cat] - spent["attributes"][cat]
                for cat in ATTRIBUTES.keys()
            },
            "abilities": {
                cat: ability_allowances[cat] - spent["abilities"][cat]
                for cat in PRIMARY_ABILITIES.keys()
            },
            "backgrounds": rules["backgrounds"] - spent["backgrounds"]
        }
    
    def get_minimum_value(self, trait_type: str, trait_name: str) -> int:
        """Get minimum allowed value for a trait (from previous modes)."""
        key = f"{trait_type}:{trait_name}"
        # Check freebie baseline first (highest), then creation baseline
        if key in self.freebie_baselines:
            return self.freebie_baselines[key]
        if key in self.creation_baselines:
            return self.creation_baselines[key]
        # Default minimums
        if trait_type == "attribute":
            return 1  # All attributes start at 1
        return 0
    
    def can_advance_mode(self) -> tuple[bool, list[str]]:
        """Check if character can advance to next mode. Returns (can_advance, warnings)."""
        warnings = []
        
        if self.creation_mode == "creation":
            remaining = self.get_creation_dots_remaining()
            
            # Check attributes
            for cat, dots in remaining["attributes"].items():
                if dots > 0:
                    warnings.append(f"{cat} Attributes: {dots} dots remaining")
            
            # Check abilities
            for cat, dots in remaining["abilities"].items():
                if dots > 0:
                    warnings.append(f"{cat}: {dots} dots remaining")
            
            # Check backgrounds
            if remaining["backgrounds"] > 0:
                warnings.append(f"Backgrounds: {remaining['backgrounds']} dots remaining")
            
            # Check breed, auspice, tribe
            if not self.breed:
                warnings.append("No Breed selected")
            if not self.auspice:
                warnings.append("No Auspice selected")
            if not self.tribe:
                warnings.append("No Tribe selected")
            
            # Check starting gifts (should have 3: breed, auspice, tribe)
            if len(self.gifts) < 3:
                warnings.append(f"Gifts: {3 - len(self.gifts)} starting gift(s) missing")
            
            return len(warnings) == 0, warnings
        
        elif self.creation_mode == "freebie":
            if self.freebie_points_available > 0:
                warnings.append(f"Freebie Points: {self.freebie_points_available} remaining")
            
            return len(warnings) == 0, warnings
        
        # XP mode - can't advance further
        return False, ["Already in XP mode"]
    
    def calculate_freebie_cost(self, trait_type: str, trait_name: str, 
                              old_value: int, new_value: int) -> int:
        """Calculate freebie point cost for changing a trait."""
        if new_value <= old_value:
            return 0  # No cost for decreases (though they may not be allowed)
        
        costs = FREEBIE_COSTS
        total_cost = 0
        
        # Calculate cost for each dot increase
        for rating in range(old_value, new_value):
            if trait_type == "attribute":
                total_cost += costs["attribute"]
            elif trait_type == "ability":
                total_cost += costs["ability"]
            elif trait_type == "background":
                total_cost += costs["background"]
            elif trait_type == "gift":
                total_cost += costs["gift"]
            elif trait_type == "rage":
                total_cost += costs["rage"]
            elif trait_type == "gnosis":
                total_cost += costs["gnosis"]
            elif trait_type == "willpower":
                total_cost += costs["willpower"]
            elif trait_type == "renown":
                total_cost += costs["renown"]
        
        return total_cost
    
    def calculate_xp_cost(self, trait_type: str, trait_name: str,
                         old_value: int, new_value: int) -> int:
        """Calculate XP cost for changing a trait."""
        if new_value <= old_value:
            return 0  # No cost for decreases (though they may not be allowed)
        
        costs = EXPERIENCE_COSTS
        total_cost = 0
        
        # Calculate cost for each dot increase
        for rating in range(old_value, new_value):
            if trait_type == "attribute":
                total_cost += (rating + 1) * costs["attribute"]
            elif trait_type == "ability":
                if rating == 0:
                    total_cost += costs["new_ability"]
                else:
                    total_cost += (rating + 1) * costs["ability"]
            elif trait_type == "gift":
                if rating == 0:
                    total_cost += costs["new_gift"]
                else:
                    total_cost += (rating + 1) * costs["new_gift"]
            elif trait_type == "rage":
                total_cost += (rating + 1) * costs["rage"]
            elif trait_type == "gnosis":
                total_cost += (rating + 1) * costs["gnosis"]
            elif trait_type == "background":
                total_cost += (rating + 1) * costs["background"]
            elif trait_type == "willpower":
                total_cost += (rating + 1) * costs["willpower"]
            elif trait_type == "renown":
                total_cost += (rating + 1) * costs["renown"]
        
        return total_cost
    
    def snapshot_baseline(self):
        """Snapshot current values as baseline for current mode."""
        # Snapshot all current trait values
        baselines = {}
        
        # Attributes
        for attr, value in self.attributes.items():
            baselines[f"attribute:{attr}"] = value
        
        # Abilities
        for ability, value in self.abilities.items():
            baselines[f"ability:{ability}"] = value
        
        # Backgrounds
        for bg, value in self.backgrounds.items():
            baselines[f"background:{bg}"] = value
        
        # Gifts
        for gift, value in self.gifts.items():
            baselines[f"gift:{gift}"] = value
        
        # Core traits
        baselines["rage"] = self.rage
        baselines["gnosis"] = self.gnosis
        baselines["willpower"] = self.willpower
        
        # Store in appropriate baseline dict
        if self.creation_mode == "creation":
            self.creation_baselines = baselines.copy()
        elif self.creation_mode == "freebie":
            self.freebie_baselines = baselines.copy()
    
    def to_dict(self) -> dict:
        """Convert character to dictionary for serialization."""
        return {
            "name": self.name,
            "player": self.player,
            "chronicle": self.chronicle,
            "concept": self.concept,
            "character_type": self.character_type,
            "breed": self.breed,
            "auspice": self.auspice,
            "tribe": self.tribe,
            "metis_deformity": self.metis_deformity,
            "nature": self.nature,
            "demeanor": self.demeanor,
            "attributes": self.attributes,
            "attribute_priorities": self.attribute_priorities,
            "ability_priorities": self.ability_priorities,
            "abilities": self.abilities,
            "specialties": self.specialties,
            "gifts": self.gifts,
            "backgrounds": self.backgrounds,
            "rage": self.rage,
            "rage_current": self.rage_current,
            "gnosis": self.gnosis,
            "gnosis_current": self.gnosis_current,
            "willpower": self.willpower,
            "willpower_current": self.willpower_current,
            "renown": self.renown,
            "rank": self.rank,
            "health_levels": self.health_levels,
            "merits": self.merits,
            "flaws": self.flaws,
            "experience_total": self.experience_total,
            "experience_spent": self.experience_spent,
            "experience_log": self.experience_log,
            "creation_mode": self.creation_mode,
            "freebie_points_spent": self.freebie_points_spent,
            "creation_baselines": self.creation_baselines,
            "freebie_baselines": self.freebie_baselines,
            "created_date": self.created_date,
            "modified_date": self.modified_date,
            "notes": self.notes
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Character':
        """Create character from dictionary."""
        char = cls()
        for key, value in data.items():
            if hasattr(char, key):
                setattr(char, key, value)
        return char
    
    def save_to_markdown(self, filepath: str):
        """Save character to markdown file."""
        self.modified_date = datetime.now().isoformat()
        
        md_content = self._generate_markdown()
        
        # Append JSON data as a hidden block
        json_data = json.dumps(self.to_dict(), indent=2)
        md_content += f"\n\n<!-- CHARACTER_DATA\n{json_data}\nEND_CHARACTER_DATA -->\n"
        
        with open(filepath, 'w') as f:
            f.write(md_content)
    
    def _generate_markdown(self) -> str:
        """Generate readable markdown representation."""
        lines = []
        lines.append(f"# {self.name}")
        lines.append("")
        
        # Identity
        lines.append("## Identity")
        lines.append(f"- **Player:** {self.player}")
        lines.append(f"- **Chronicle:** {self.chronicle}")
        lines.append(f"- **Concept:** {self.concept}")
        lines.append(f"- **Breed:** {self.breed}")
        lines.append(f"- **Auspice:** {self.auspice}")
        lines.append(f"- **Tribe:** {self.tribe}")
        if self.metis_deformity:
            lines.append(f"- **Metis Deformity:** {self.metis_deformity}")
        lines.append(f"- **Nature:** {self.nature}")
        lines.append(f"- **Demeanor:** {self.demeanor}")
        lines.append("")
        
        # Attributes
        lines.append("## Attributes")
        for category, attrs in ATTRIBUTES.items():
            lines.append(f"### {category}")
            for attr in attrs:
                rating = self.attributes.get(attr, 1)
                dots = "●" * rating + "○" * (5 - rating)
                spec = ""
                if attr in self.specialties:
                    specialties = self.specialties[attr]
                    if isinstance(specialties, list):
                        spec = f" ({', '.join(specialties)})"
                    else:
                        spec = f" ({specialties})"
                lines.append(f"- **{attr}:** {dots}{spec}")
            lines.append("")
        
        # Abilities
        lines.append("## Abilities")
        for category in ["Talents", "Skills", "Knowledges"]:
            lines.append(f"### {category}")
            abilities_in_cat = [a for a in self.abilities.keys() 
                              if self.get_ability_category(a) == category]
            for ability in sorted(abilities_in_cat):
                rating = self.abilities[ability]
                if rating > 0:
                    dots = "●" * rating + "○" * (5 - rating)
                    spec = ""
                    if ability in self.specialties:
                        spec = f" ({', '.join(self.specialties[ability])})"
                    lines.append(f"- **{ability}:** {dots}{spec}")
            lines.append("")
        
        # Gifts
        lines.append("## Gifts")
        for gift, level in sorted(self.gifts.items()):
            lines.append(f"- **{gift}** (Level {level})")
        lines.append("")
        
        # Backgrounds
        lines.append("## Backgrounds")
        for bg, rating in sorted(self.backgrounds.items()):
            if rating > 0:
                dots = "●" * rating + "○" * (5 - rating)
                lines.append(f"- **{bg}:** {dots}")
        lines.append("")
        
        # Core Traits
        lines.append("## Core Traits")
        rage_dots = "●" * self.rage + "○" * (10 - self.rage)
        gnosis_dots = "●" * self.gnosis + "○" * (10 - self.gnosis)
        will_dots = "●" * self.willpower + "○" * (10 - self.willpower)
        lines.append(f"- **Rage:** {rage_dots} (Current: {self.rage_current})")
        lines.append(f"- **Gnosis:** {gnosis_dots} (Current: {self.gnosis_current})")
        lines.append(f"- **Willpower:** {will_dots} (Current: {self.willpower_current})")
        lines.append("")
        
        # Renown
        lines.append("## Renown")
        lines.append(f"- **Rank:** {self.rank}")
        for renown_type in RENOWN_TYPES:
            rating = self.renown.get(renown_type, 0)
            if rating > 0:
                dots = "●" * rating + "○" * (10 - rating)
                lines.append(f"- **{renown_type}:** {dots}")
        lines.append("")
        
        # Forms
        lines.append("## Forms")
        for form_name, form_data in FORMS.items():
            lines.append(f"### {form_name}")
            lines.append(f"*{form_data['description']}*")
            lines.append(f"**Size:** {form_data['size']}")
            lines.append(f"**Shift Difficulty:** {form_data['shift_difficulty']}")
            modifiers = form_data['statistics_adjustment']
            mod_strs = []
            for attr, mod in modifiers.items():
                if mod != 0:
                    mod_strs.append(f"{attr}: {mod:+d}")
            if mod_strs:
                lines.append(f"**Modifiers:** {', '.join(mod_strs)}")
            if form_data.get('special'):
                lines.append(f"**Special:** {form_data['special']}")
            lines.append("")
        
        # Merits and Flaws
        if self.merits or self.flaws:
            lines.append("## Merits and Flaws")
            if self.merits:
                lines.append("### Merits")
                for merit, cost in sorted(self.merits.items()):
                    lines.append(f"- {merit} ({cost} pts)")
            if self.flaws:
                lines.append("### Flaws")
                for flaw, bonus in sorted(self.flaws.items()):
                    lines.append(f"- {flaw} ({bonus} pts)")
            lines.append("")
        
        # Experience
        lines.append("## Experience")
        lines.append(f"- **Total:** {self.experience_total}")
        lines.append(f"- **Spent:** {self.experience_spent}")
        lines.append(f"- **Available:** {self.experience_available}")
        lines.append("")
        
        # Notes
        if self.notes:
            lines.append("## Notes")
            lines.append(self.notes)
            lines.append("")
        
        return "\n".join(lines)
    
    @classmethod
    def load_from_markdown(cls, filepath: str) -> 'Character':
        """Load character from markdown file."""
        with open(filepath, 'r') as f:
            content = f.read()
        
        # Extract JSON data from hidden block
        import re
        match = re.search(r'<!-- CHARACTER_DATA\n(.*?)\nEND_CHARACTER_DATA -->', 
                         content, re.DOTALL)
        
        if match:
            json_data = json.loads(match.group(1))
            return cls.from_dict(json_data)
        
        # Fallback: create new character with just the name from title
        char = cls()
        title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
        if title_match:
            char.name = title_match.group(1)
        return char


