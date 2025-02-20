import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

lists_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/triels.ipynb"
]

for filepath in lists_of_files:
    filepath = Path(filepath)  # Convert to Path object
    filedir, filename = os.path.split(filepath)  # Get directory and file name
    
    # Create directory if it doesn't exist
    if filedir:
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")
    
    # Create the file if it does not exist
    if not filepath.exists():
        with open(filepath, "w") as f:
            pass  # Create an empty file
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
