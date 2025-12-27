# Sentinel Monitor

## Português

Sentinel Monitor é um programa em Python que coleta métricas do sistema em tempo real, como CPU, Memória e Disco, e exibe essas informações em uma interface gráfica usando Tkinter. Além disso, mantém histórico das métricas e permite exportar para CSV.

### Funcionalidades

- Coleta métricas do sistema em tempo real
- Exibição em tabela legível na GUI
- Atualização automática a cada intervalo configurável
- Histórico de métricas armazenado em memória
- Exportação do histórico para CSV (UTF-8)
- Configuração de intervalos via arquivo YAML

### Requisitos

- Python 3.x
- Tkinter (já incluso no Python)
- Dependências do projeto: ver `requirements.txt` (opcional, se você gerar)

### Como rodar

1. Ative o ambiente virtual (caso tenha criado):

(no terminal)
# Windows
.\venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
Instale dependências (se houver):


pip install -r requirements.txt
Execute o programa:

python main.py

Na janela:

Veja CPU, Memória e Disco atualizados em tempo real

Use o botão Exportar CSV para salvar o histórico

Use o botão Sair para fechar o programa

## English
Sentinel Monitor is a Python program that collects real-time system metrics such as CPU, Memory, and Disk usage, and displays them in a graphical interface using Tkinter. It also keeps a history of metrics and allows exporting them to a CSV file.

Features
Collects real-time system metrics

Displays metrics in a readable table in the GUI

Auto-updates every configurable interval

Stores metrics history in memory

Export history to CSV (UTF-8)

Configurable interval via YAML file

Requirements
Python 3.x

Tkinter (included with Python)

Project dependencies: see requirements.txt (optional, if generated)

How to run
Activate the virtual environment (if created):

(PowerShell)
# Windows
.\venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
Install dependencies (if any):

pip install -r requirements.txt
Run the program:

python main_tk.py
In the window:

See CPU, Memory, and Disk usage updated in real time

Use the Export CSV button to save the history

Use the Exit button to close the program
