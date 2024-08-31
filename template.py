import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name = "mlproject"



list_of_file = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_monitoring.py",
    f"src/{project_name}/piplines/__init__.py",
    f"src/{project_name}/piplines/training_pipeline.py",
    f"src/{project_name}/piplines/prediction_pipeline.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirement.txt",
    "setup.py"
       


]

for files in list_of_file:
    filepath = Path(files)
    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok= True)
        logging.info(f"creating directories:{filedir} for the {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as  f:
            pass
            logging.info(f"creating empty file: {filepath}")
    else:
        logging.info(f"{filename}is already exists")