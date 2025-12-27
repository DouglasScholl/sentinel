import os
import sys
import yaml


def get_base_path():
    # Quando estiver rodando como executável (PyInstaller)
    if getattr(sys, "frozen", False):
        return sys._MEIPASS

    # Quando estiver rodando como script normal
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_config(filename="config.yaml"):
    base_path = get_base_path()
    config_path = os.path.join(base_path, filename)

    with open(config_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)
