import pytest
import sys
import os

# Adiciona a raiz do projeto ao PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import app
from models import db


@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

    with app.app_context():
        db.create_all()

        with app.test_client() as client:
            yield client

        db.drop_all()