from fastapi.testclient import TestClient
import pytest
from app.main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import get_db, Base
from fastapi import Depends
from app import models
from app.oauth2 import create_access_token

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:1Jossilene%40@localhost/fastapi_test"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture
def test_user2(session, client):
    user_data = {"email":"joelsabonete@gmail.com", "password": "123456"}
    res = client.post("/users/", json=user_data)

    assert res.status_code == 201
    new_user= res.json()
    new_user["password"] = user_data["password"]
    return new_user



@pytest.fixture
def test_user(session, client):
    user_data = {"email":"joelalsmim@gmail.com", "password": "123456"}
    res = client.post("/users/", json=user_data)

    assert res.status_code == 201
    new_user= res.json()
    new_user["password"] = user_data["password"]
    return new_user



@pytest.fixture()
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()



@pytest.fixture()
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)  


@pytest.fixture
def token(test_user):
    return create_access_token({"user_id": test_user['id']})  # Retorne o token gerado

@pytest.fixture
def authorized_client(client, token):
    client.headers = {
        **client.headers,
        "Authorization": f"Bearer {token}"
    }

    return client

@pytest.fixture
def test_post(test_user, session, test_user2):
    post_data = [
        {
            "title": "Meu primeiro post",
            "content": "Este é o conteúdo do meu primeiro post",
            "owner_id": test_user['id']
        },
        {
            "title": "Segundo post",
            "content": "Aqui vai o conteúdo do meu segundo post",
            "owner_id": test_user['id']
        },
        {
            "title": "Terceiro post",
            "content": "Este é o conteúdo do terceiro post",
            "owner_id": test_user['id']
        },
        {
            "title": "Quarto post",
            "content": "Este é o conteúdo do terceiro post",
            "owner_id": test_user2['id']
        },


    ]

    # Criar os posts no banco de dados
from fastapi.testclient import TestClient
import pytest
from app.main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import get_db, Base
from fastapi import Depends
from app import models
from app.oauth2 import create_access_token

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:1Jossilene%40@localhost/fastapi_test"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture
def test_user2(session, client):
    user_data = {"email":"joelsabonete@gmail.com", "password": "123456"}
    res = client.post("/users/", json=user_data)

    assert res.status_code == 201
    new_user= res.json()
    new_user["password"] = user_data["password"]
    return new_user



@pytest.fixture
def test_user(session, client):
    user_data = {"email":"joelalsmim@gmail.com", "password": "123456"}
    res = client.post("/users/", json=user_data)

    assert res.status_code == 201
    new_user= res.json()
    new_user["password"] = user_data["password"]
    return new_user



@pytest.fixture()
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()



@pytest.fixture()
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)  


@pytest.fixture
def token(test_user):
    return create_access_token({"user_id": test_user['id']})  # Retorne o token gerado

@pytest.fixture
def authorized_client(client, token):
    client.headers = {
        **client.headers,
        "Authorization": f"Bearer {token}"
    }

    return client

@pytest.fixture
def test_post(test_user, session, test_user2):
    post_data = [
        {
            "title": "Meu primeiro post",
            "content": "Este é o conteúdo do meu primeiro post",
            "owner_id": test_user['id']
        },
        {
            "title": "Segundo post",
            "content": "Aqui vai o conteúdo do meu segundo post",
            "owner_id": test_user['id']
        },
        {
            "title": "Terceiro post",
            "content": "Este é o conteúdo do terceiro post",
            "owner_id": test_user['id']
        },
        {
            "title": "Quarto post",
            "content": "Este é o conteúdo do terceiro post",
            "owner_id": test_user2['id']
        },


    ]

    # Criar os posts no banco de dados
    session.add_all([
    models.Post(title="Meu primeiro post", content="Este é o conteúdo do meu primeiro post", owner_id=test_user['id']),
    models.Post(title="Segundo post", content="Aqui vai o conteúdo do meu segundo post", owner_id=test_user['id']),
    models.Post(title="Terceiro post", content="Este é o conteúdo do terceiro post", owner_id=test_user['id']),
    models.Post(title="Quarto post", content="Este é o conteúdo do quarto post", owner_id=test_user2['id'])  # Novo post
    ])
    session.commit()

    # Retornar os posts para uso nos testes
    posts = session.query(models.Post).all()
    return posts
    return posts
    # Retornar os posts para uso nos testes
    posts = session.query(models.Post).all()
    return posts
    return posts
