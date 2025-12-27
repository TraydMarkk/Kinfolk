#!/bin/bash
# Launch script for Kinfolk - Werewolf: The Apocalypse Character Creator

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Change to the script directory
cd "$SCRIPT_DIR" || exit 1

# Run the application
python3 -m kinfolk.gui "$@"

