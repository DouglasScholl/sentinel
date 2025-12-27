import sqlite3
from pathlib import Path
import logging

# Caminho absoluto do DB a partir da raiz do projeto
BASE_DIR = Path(__file__).resolve().parent.parent  # raiz do projeto
DB_DIR = BASE_DIR / "data"
DB_PATH = DB_DIR / "sentinel.db"

# Cria pasta "data" se não existir
DB_DIR.mkdir(exist_ok=True)

def init_db():
    """Cria a tabela metrics se não existir"""
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS metrics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                cpu REAL,
                memory REAL,
                disk REAL
            )
        """)
        conn.commit()
        logging.info(f"Tabela metrics inicializada em {DB_PATH}")
    except Exception as e:
        logging.error(f"Erro ao inicializar o DB: {e}")
    finally:
        conn.close()

def insert_metrics(metrics: dict):
    """Insere coleta no banco, garantindo valores corretos"""
    # Confere se o dicionário tem todas as chaves
    timestamp = str(metrics.get("timestamp", None))
    cpu = float(metrics.get("cpu", 0))
    memory = float(metrics.get("memory", 0))
    disk = float(metrics.get("disk", 0))

    if timestamp is None:
        logging.error("Timestamp ausente, coleta não inserida")
        return

    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("""
            INSERT INTO metrics (timestamp, cpu, memory, disk)
            VALUES (?, ?, ?, ?)
        """, (timestamp, cpu, memory, disk))
        conn.commit()
        logging.info("Métricas salvas no banco")
    except Exception as e:
        logging.error(f"Erro ao inserir no banco: {e}")
    finally:
        conn.close()
