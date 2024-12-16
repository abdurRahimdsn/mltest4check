import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name = "mltest4"

list_of_files=[
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/component/__init__py.",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/model_tranier.py",
    f"src/{project_name}/components/model_monitering.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/traning_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "app.py",
    "dockerfile.py",
    "requirement.txt",
    "setup.py",
    "main.py"

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filemane = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creatin directory:{filedir} for the file{filemane}")

        if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
            with open (filepath,'w')as f:
                pass
                logging.info(f"Creaating empty file: {filepath}")

        else:
            logging.info(f"{filename} is already exits")
