from flask import Flask, request, jsonify, render_template
from models import db, SensorData # <--- Importando do seu novo arquivo models.py

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o banco de dados com as configurações do app
db.init_app(app)

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/api/data", methods=["POST"])
def receive_data():
    data = request.json
    sensor = SensorData(
        temperature=data["temperature"],
        humidity=data["humidity"]
    )
    db.session.add(sensor)
    db.session.commit()
    return jsonify({"message": "Data received"}), 201

@app.route("/api/data", methods=["GET"])
def get_data():
    # Pega os últimos 20 registros
    data = SensorData.query.order_by(SensorData.created_at.desc()).limit(20).all()
    return jsonify([
        {
            "temperature": d.temperature,
            "humidity": d.humidity,
            "created_at": d.created_at.strftime("%H:%M:%S")
        } for d in data
    ])

if __name__ == "__main__":
    with app.app_context():
        db.create_all() # Cria o arquivo database.db se não existir
    app.run(debug=True)