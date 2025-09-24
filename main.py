# main.py

import os
from gui import run_gui

def setup_environment():
    """Prepare necessary folders and environment settings."""
    output_folder = os.path.join(os.getcwd(), "output")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

def main():
    """Main entry point for the application."""
    setup_environment()
    run_gui()

if __name__ == "__main__":
    main()
