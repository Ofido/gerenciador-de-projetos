import logging
from os import listdir

from genericpath import isdir

logging.getLogger().setLevel(logging.WARN)

def verify_item_in_project(item, local=None):
    if item not in projects:
        logging.info("not in projects")
        if local:
            here = f"{local}\\{item}"
        else:
            here = f"{item}"
        list_dir(here, item)

def verify_itens_in_dir(dir, local):
    for item in dir:
        logging.info(f"item: {item}")
        if isdir(item):
            logging.info("not file")
            if local:
                here = f"{local}\\{item}"
            else:
                here = f"{item}"
            list_dir(local=here)
            verify_item_in_project(item, local)
            continue

def list_dir(local = None, item = None):
    if not str(local).split("\\")[-1].startswith("."):
        logging.info(f"local: {local}, item: {item}")
        dir = listdir(local)
        logging.info(f"dir: {dir}")
        if item and (".git" in dir):
            logging.info("have git")
            projects.append(item)
            return
        verify_itens_in_dir(dir, local)

logging.info("segunda")
try:
    projects = [line.strip() for line in open('.config', 'r')]
except:
    projects = []

list_dir()
logging.warning(projects)

with open('.config', 'w') as f:
    for project in projects:
        f.write(project + "\n")
