import pytest

@pytest.fixture
def new_customer():
    return {
        "name": "Test User",
        "email": "test@example.com",
        "password": "testpassword",
        "phone": "1234567890",
        "role": "customer",
    }


def test_register_user(test_client, new_customer):
    response = test_client.post("/api/register", json=new_customer)
    assert response.status_code == 201
    assert response.json["message"] == "Usuario creado exitosamente"


def test_register_duplicate_user(test_client, new_customer):

    # Intentar registrar el mismo usuario de nuevo
    response = test_client.post("/api/register", json=new_customer)
    assert response.status_code == 400
    assert response.json["error"] == "El correo electrónico ya está en uso"


def test_login_user(test_client, new_customer):
    # Ahora intentar iniciar sesión
    login_credentials = {
        "email": new_customer["email"],
        "password": new_customer["password"],
    }
    response = test_client.post("/api/login", json=login_credentials)
    assert response.status_code == 200
    assert response.json["access_token"]


def test_login_invalid_user(test_client, new_customer):
    # Intentar iniciar sesión sin registrar al usuario
    login_credentials = {
        "email": "nouser@example.com",
        "password": new_customer["password"],
    }
    response = test_client.post("/api/login", json=login_credentials)
    assert response.status_code == 401
    assert response.json["error"] == "Credenciales inválidas"


def test_login_wrong_password(test_client, new_customer):
    # Intentar iniciar sesión con una contraseña incorrecta
    login_credentials = {"email": new_customer["email"], "password": "wrongpassword"}
    response = test_client.post("/api/login", json=login_credentials)
    assert response.status_code == 401
    assert response.json["error"] == "Credenciales inválidas"

def test_register_admin_user(test_client):
    new_admin = {
        "name": "Admin User",
        "email": "admin@example.com",
        "password": "adminpassword",
        "phone": "9876543210",
        "role": "admin",
    }
    response = test_client.post("/api/register", json=new_admin)
    assert response.status_code == 201
    assert response.json["message"] == "Usuario creado exitosamente"


def test_admin_login_user(test_client):
    # Ahora intentar iniciar sesión como administrador
    admin_credentials = {
        "email": "admin@example.com",
        "password": "adminpassword",
    }
    response = test_client.post("/api/login", json=admin_credentials)
    assert response.status_code == 200
    assert response.json["access_token"]

