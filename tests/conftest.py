import pytest
import os
# Forzamos una variable de entorno para que el factory no busque Postgres
os.environ['DATABASE_URL'] = 'sqlite:///:memory:'

from app import create_app, db

@pytest.fixture
def client():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "SQLALCHEMY_TRACK_MODIFICATIONS": False
    })

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.drop_all()