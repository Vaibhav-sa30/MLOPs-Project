#This is to always create the folder structure without spending time in creating folders and files manually

#python script

import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "MLOPs_project_using_MLFlow"

list_of_files = [
    ".github/workflows/.gitkeep", # Placeholder file for CI/CD deployment using GitHub Actions
    f"src/{project_name}/__init__.py",  # Init file for the main project module
    f"src/{project_name}/components/__init__.py", #Init file for the components module
    f"src/{project_name}/utils/__init__.py",  # Init file for the utils module
    f"src/{project_name}/utils/common.py",  # Common utility functions used in the project
    f"src/{project_name}/config/__init__.py",  # Init file for the configuration module
    f"src/{project_name}/config/configuration.py", ## Configuration settings for the project
    f"src/{project_name}/pipeline/__init__.py",  # Init file for the pipeline module
    f"src/{project_name}/entity/__init__.py",  # Init file for the entity module
    f"src/{project_name}/entity/config_entity.py",  # Entity class for project configuration
    f"src/{project_name}/constant/__init__.py",# Init file for the constants module
    
    #"dvc.yaml",
   # List of important project files:
# ---------------------------------
    "config/config.yaml", # File containing configuration settings for the project. Here we keep all the configuration of my project.
    "params.yaml",          # Configuration parameters for the project
    "schema.yaml",          # Schema or structure definition for data used in the project
    "main.py",              # Main Python script that orchestrates the project's execution
    "app.py",               # Python script for running the project's web application
    "Dockerfile",           # Instructions for building a Docker container for the project
    "requirements.txt",     # List of Python packages and their versions required for the project
    "setup.py",             # Setup script for packaging and distribution of the project
    "research/trials.ipynb",# Jupyter Notebook containing research trials and experiments
    "templates/index.html"  # HTML template for the project's web application

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    

    else:
        logging.info(f"{filename} is already exists")


