from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Criamos o objeto db aqui, mas ele será vinculado ao app depois
db = SQLAlchemy()

class SensorData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float)
    humidity = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)