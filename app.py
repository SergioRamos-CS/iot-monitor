from flask import Flask, request, jsonify, render_template, Response
from models import db, SensorData
from datetime import datetime
import csv

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

# 🔧 ROTA POST COM HORÁRIO LOCAL
@app.route("/api/data", methods=["POST"])
def receive_data():
    data = request.json

    sensor = SensorData(
        temperature=data["temperature"],
        humidity=data["humidity"],
        created_at=datetime.now()  # 👈 HORÁRIO LOCAL
    )

    db.session.add(sensor)
    db.session.commit()

    return jsonify({"message": "Data received"}), 201

@app.route("/api/data", methods=["GET"])
def get_data():
    data = SensorData.query.order_by(SensorData.created_at.desc()).limit(20).all()
    return jsonify([
        {
            "temperature": d.temperature,
            "humidity": d.humidity,
            "created_at": d.created_at.strftime("%Y-%m-%d %H:%M:%S")
        } for d in data
    ])

# 🔽 EXPORTAÇÃO CSV COM FILTRO DE DATA/HORA
@app.route("/export/csv")
def export_csv():
    inicio = request.args.get("inicio")
    fim = request.args.get("fim")

    inicio = datetime.fromisoformat(inicio)
    fim = datetime.fromisoformat(fim)

    dados = SensorData.query.filter(
        SensorData.created_at.between(inicio, fim)
    ).all()

    def gerar_csv():
        yield "Temperatura,Umidade,Data/Hora\n"
        for d in dados:
            yield f"{d.temperature},{d.humidity},{d.created_at.strftime('%Y-%m-%d %H:%M:%S')}\n"

    return Response(
        gerar_csv(),
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment; filename=relatorio_iot.csv"}
    )

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)