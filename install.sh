#!/bin/bash

exit_on_error(){
    echo "Error: $1"
    exit 1
}

# Ensure sudo
if [ "$(id -u)" -ne 0 ]; then
    echo "This script requires sudo permissions. Please run with 'sudo ./install.sh'"
    exit 1
fi

# Check if venv exists if ! setup
if [ ! -d "/Al/.venv" ]; then
    echo ">>> Creating /Al"
    mkdir /Al || exit_on_error "Failed to create in root. Check permissions"
    echo ">>> Ownership and Permissions" 
    chown -R al:al /Al || exit_on_error "Failed to set ownership."
    chmod -R 755 /Al || exit_on_error "Failed to set permissions."

    echo ">>> Creating Virtual Environment"
    python3 -m venv /Al/.venv || exit_on_error "Failed to create venv. Check permissions"
fi

if [ ! -d "/Al/.venv" ]; then
    echo ">>> Verifying installation"
    exit_on_error "Virtual environment not set up. Please check installation."
fi

# Activate venv and update with requirements.txt
echo ">>> Installing dependencies"
source /Al/.venv/bin/activate || exit_on_error "Failed to activate venv. Check installation"
pip --version
pip install -r requirements.txt || exit_on_error "Failed to isntall requirements.txt. Check installation"

# Confirm all set and dandy
echo ">>> Virtual environment and dependencies setup complete"