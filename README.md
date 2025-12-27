# Kinfolk

**Werewolf: The Apocalypse 20th Anniversary Edition Character Creator**

A native GTK4/Adwaita application for Arch Linux to create and manage Werewolf: The Apocalypse 20th Anniversary Edition characters.

## Author

**TraydMarkk**

## Features

- **Three-Panel Layout**
  - Left sidebar: Character file browser for saved characters
  - Center panel: Full character editor with all traits
  - Right sidebar: Progress tracker with dot/point counters

- **Three Character Creation Modes**
  - **Creation Mode**: Initial character creation with dot distribution tracking
  - **Freebie Point Mode**: Spend freebie points to customize your character
  - **XP Mode**: Track and spend experience points for character advancement

- **Complete W20 Character Sheet Support**
  - Breed selection (Homid, Metis, Lupus) with breed-specific traits
  - Auspice selection (Ragabash, Theurge, Philodox, Galliard, Ahroun) with starting Rage and Renown
  - Tribe selection (all 13 tribes) with tribe-specific Gifts
  - Comprehensive Gift lists with descriptions (Breed, Auspice, and Tribe Gifts)
  - Forms section showing all five forms (Homid, Glabro, Crinos, Hispo, Lupus) with attribute modifiers
  - Core traits: Rage, Gnosis, Willpower, Renown, Rank
  - Full Backgrounds, Merits, and Flaws support

- **Forms Section**
  - Detailed information about all five werewolf forms
  - Attribute modifiers for each form displayed clearly
  - Form descriptions and special abilities

- **Gift Tooltips**
  - All Gifts include detailed descriptions for tooltips
  - Gifts organized by Breed, Auspice, and Tribe
  - Additional Gifts from wyrmfoe.com included

- **Save/Load System**
  - Characters saved as readable Markdown (.md) files
  - Automatic character discovery in save folder
  - Export to plain text (.txt) for printing

## Requirements

- Arch Linux (or other Linux distribution)
- Python 3.10+
- GTK4
- libadwaita

## Installation

### Install Dependencies (Arch Linux)

```bash
sudo pacman -S python gtk4 libadwaita python-gobject
```

### Run the Application

```bash
cd /path/to/Kinfolk
python -m kinfolk.gui
```

Or install as a package:

```bash
pip install -e .
kinfolk
```

## Usage

1. **New Character**: Click "New Character" in the left sidebar
2. **Select Breed, Auspice, and Tribe**: Choose your character's fundamental traits
3. **Fill in Details**: Use the center panel to set all character traits
4. **Track Progress**: The right sidebar shows remaining dots/points
5. **Set Priorities**: Assign primary/secondary/tertiary for Attributes and Abilities
6. **Select Gifts**: Choose starting Gifts from your Breed, Auspice, and Tribe lists
7. **View Forms**: Check the Forms section to see attribute modifiers for each form
8. **Advance Modes**: Click "Advance to Freebie Mode" when creation dots are spent
9. **Save**: Click "Save" to store your character as a .md file
10. **Export**: Click "Export TXT" to create a printable text file

## Character Storage

Characters are saved to: `characters/` folder in the directory where Kinfolk is run from.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

This is a fan-made tool for use with the Werewolf: The Apocalypse tabletop roleplaying game. Werewolf: The Apocalypse is © Paradox Interactive.





