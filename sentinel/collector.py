import psutil
from datetime import datetime

def collect_metrics():
    """
    Coleta métricas do sistema:
    - Timestamp em UTC
    - Percentual de CPU
    - Percentual de memória usada
    - Percentual de disco usado
    Retorna um dicionário com esses valores.
    """
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "cpu": float(psutil.cpu_percent(interval=1)),
        "memory": float(psutil.virtual_memory().percent),
        "disk": float(psutil.disk_usage('/').percent)
    }
