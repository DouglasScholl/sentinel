import yaml

CONFIG_PATH = "config.yaml"

def load_config():
    """
    Lê as configurações do arquivo YAML e retorna como dicionário.
    Espera conter pelo menos:
    - collection_interval: tempo em segundos entre coletas
    - log_level: nível de log (INFO, DEBUG, etc.)
    """
    with open(CONFIG_PATH, "r") as file:
        return yaml.safe_load(file)
