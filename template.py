import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')

project_name='textSummarizer'

list_of_files=[
    ".github/workflow/.gitkeep"
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/init.py",
    f"src/{project_name}/config/init.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "app.py",
    "main.py",
    "dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb"

]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir, filename= os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==o):
        with open(filepath,'w') as f:
            pass
        logging.info(f"creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")
