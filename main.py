import tkinter as tk
from tkinter import ttk, messagebox
import time
import threading
import csv
from sentinel.collector import collect_metrics
from sentinel.config import load_config

class SentinelGUI:
    def __init__(self, root, interval):
        self.root = root
        self.root.title("Sentinel Monitor")
        self.interval = interval
        self.history = []

        # Cria tabela usando Treeview
        columns = ("timestamp", "cpu", "memory", "disk")
        self.tree = ttk.Treeview(root, columns=columns, show="headings")
        self.tree.heading("timestamp", text="Timestamp")
        self.tree.heading("cpu", text="CPU (%)")
        self.tree.heading("memory", text="Memória (%)")
        self.tree.heading("disk", text="Disco (%)")

        # Largura das colunas
        self.tree.column("timestamp", width=180)
        self.tree.column("cpu", width=80)
        self.tree.column("memory", width=80)
        self.tree.column("disk", width=80)

        self.tree.pack(padx=10, pady=10)

        # Botões
        self.btn_frame = tk.Frame(root)
        self.btn_frame.pack(pady=5)
        tk.Button(self.btn_frame, text="Exportar CSV", command=self.export_csv).pack(side=tk.LEFT, padx=5)
        tk.Button(self.btn_frame, text="Sair", command=self.close).pack(side=tk.LEFT, padx=5)

        # Inicia atualização em thread
        self.running = True
        threading.Thread(target=self.update_metrics, daemon=True).start()

    def update_metrics(self):
        while self.running:
            metrics = collect_metrics()
            self.history.append(metrics)
            # Insere nova linha na tabela
            self.tree.insert("", "end", values=(
                metrics["timestamp"],
                f"{metrics['cpu']:.1f}%",
                f"{metrics['memory']:.1f}%",
                f"{metrics['disk']:.1f}%"
            ))
            time.sleep(self.interval)

    def export_csv(self):
        try:
            with open("metrics.csv", "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["Timestamp", "CPU (%)", "Memória (%)", "Disco (%)"])
                for m in self.history:
                    writer.writerow([
                        m["timestamp"],
                        f"{m['cpu']:.1f}",
                        f"{m['memory']:.1f}",
                        f"{m['disk']:.1f}"
                    ])
            messagebox.showinfo("Exportar CSV", "Histórico exportado para metrics.csv")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def close(self):
        self.running = False
        self.root.destroy()

if __name__ == "__main__":
    config = load_config()
    root = tk.Tk()
    app = SentinelGUI(root, interval=config["collection_interval"])
    root.mainloop()
