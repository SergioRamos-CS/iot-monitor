# 🌐 IoT Monitor Web – Sistema de Monitoramento Simulado

Este projeto é um sistema de monitoramento de sensores IoT desenvolvido em **Python (Flask)**. Ele simula a coleta de dados de temperatura e umidade, armazena em um banco de dados relacional e exibe as informações em um dashboard com gráficos em tempo real.

---

## 🚀 Funcionalidades

- **API REST:** Recebe dados de sensores via JSON (Endpoint `/api/data`).
- **Banco de Dados:** Persistência de dados utilizando SQLite e SQLAlchemy.
- **Dashboard Real-time:** Gráficos dinâmicos utilizando **Chart.js**.
- **Simulador IoT:** Script autônomo que gera e envia dados aleatórios para simular hardware físico.
- **Interface Responsiva:** Visual focado em legibilidade e monitoramento técnico.

---

## 🛠️ Tecnologias Utilizadas

- **Backend:** [Flask](https://flask.palletsprojects.com/) (Python)
- **Banco de Dados:** SQLite (SQLAlchemy ORM)
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **Gráficos:** [Chart.js](https://www.chartjs.org/)
- **Ambiente:** GitHub Codespaces / Git

---

## 📂 Estrutura do Projeto

```text
iot-monitor/
├── app.py               # Servidor Flask e rotas da API
├── models.py            # Definição do banco de dados
├── requirements.txt     # Dependências do projeto
├── iot_simulator.py     # Script que simula o sensor IoT
├── static/
│   └── script.js        # Lógica de atualização do gráfico
├── templates/
│   └── dashboard.html   # Interface do usuário
└── tests/
    └── test_api.py      # Testes básicos de integração
```
