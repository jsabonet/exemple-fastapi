from app import schemas
# from tests.database import client, session
from jose import jwt
import pytest
from app.oauth2 import SECRET_KEY, ALGORITHM




def test_create_user(client):
    res = client.post("/users/", json={"email": "joel@gmail.com", "password": "123456"})

    new_user = schemas.UserOut(**res.json())
    assert res.status_code == 201
    assert new_user.email == "joel@gmail.com"

def test_login_user(client, test_user):
    res = client.post("/login", data={"username": test_user["email"], "password": test_user["password"]})
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, SECRET_KEY, algorithms=[ALGORITHM])
    id = payload.get("user_id")
    assert int(id) == test_user['id']
    assert login_res.token_type == "bearer"
    assert res.status_code == 200


@pytest.mark.parametrize("email, password, status_code", [
    ("wrong@gmail.com" ,"passwsghdsg", 403),
    ("joel@gmail.com",  "svsgvgd", 403),
    ("wrongSosbh@gmail.com", "whentud", 403),
    (None, '123456', 403),
    ("joel@gmail.com" , None, 403)

])
def test_incorrect_login(test_user, client, email, password, status_code):
    res = client.post("/login", data={"username": email, "password": password})

    assert res.status_code == status_code
    # assert res.json().get('detail') == 'Invalid Credentials'