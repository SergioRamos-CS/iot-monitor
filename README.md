# 🌡️ IoT Monitor – Monitoramento de Temperatura e Umidade

Projeto acadêmico desenvolvido no âmbito do **Projeto Integrador**, com o objetivo de implementar um sistema web para **monitoramento de dados ambientais simulados por sensores IoT**, permitindo visualização em tempo real, armazenamento em banco de dados e exportação de relatórios.

---

## 📌 Objetivo do Projeto

Desenvolver uma aplicação web capaz de:
- Receber dados de sensores IoT simulados
- Armazenar dados ambientais (temperatura e umidade)
- Exibir gráficos dinâmicos em um dashboard responsivo
- Destacar faixas ideais de operação
- Exportar relatórios em formato CSV
- Garantir confiabilidade por meio de testes automatizados

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.12**
- **Flask** – backend e API REST
- **Flask-SQLAlchemy** – ORM
- **SQLite** – banco de dados
- **HTML5 / CSS3**
- **JavaScript**
- **Chart.js** – gráficos
- **Pytest** – testes automatizados
- **Git/GitHub** – controle de versão

---

## 📂 Estrutura do Projeto

```text
iot-monitor/
│
├── app.py
├── models.py
├── database.db
├── iot_simulator.py
├── requirements.txt
│
├── templates/
│   └── dashboard.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── dashboard.js
│
├── tests/
│   ├── conftest.py
│   └── test_api.py
│
└── README.md