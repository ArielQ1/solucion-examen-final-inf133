import pytest
from datetime import datetime

@pytest.fixture
def customer_reservation_data():
    return {
        "user_id": 1,
        "restaurant_id": 1,
        "reservation_date": datetime.now().isoformat(),
        "num_guests": 4,
        "special_requests": "Window seat",
        "status": "pending"
    }

def test_customer_list_own_reservations(test_client, customer_auth_headers):
    response = test_client.get("/api/reservations", headers=customer_auth_headers)
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_customer_create_reservation(test_client, customer_auth_headers, customer_reservation_data):
    response = test_client.post("/api/reservations", json=customer_reservation_data, headers=customer_auth_headers)
    assert response.status_code == 201
    assert response.json["user_id"] == customer_reservation_data["user_id"]
    assert response.json["restaurant_id"] == customer_reservation_data["restaurant_id"]
    assert response.json["num_guests"] == customer_reservation_data["num_guests"]
    assert response.json["special_requests"] == customer_reservation_data["special_requests"]
    assert response.json["status"] == customer_reservation_data["status"]

def test_customer_get_own_reservation(test_client, customer_auth_headers, customer_reservation_data):
    # Primero crea una reserva
    response = test_client.post("/api/reservations", json=customer_reservation_data, headers=customer_auth_headers)
    assert response.status_code == 201
    reservation_id = response.json["id"]
    user_id = customer_reservation_data["user_id"]

    # Ahora obtén la reserva utilizando un parámetro de consulta
    response = test_client.get(f"/api/reservations/{reservation_id}?user_id={user_id}", headers=customer_auth_headers)
    assert response.status_code == 200
    assert response.json["user_id"] == customer_reservation_data["user_id"]
    assert response.json["restaurant_id"] == customer_reservation_data["restaurant_id"]
    assert response.json["num_guests"] == customer_reservation_data["num_guests"]
    assert response.json["special_requests"] == customer_reservation_data["special_requests"]
    assert response.json["status"] == customer_reservation_data["status"]

def test_customer_get_nonexistent_reservation(test_client, customer_auth_headers):
    response = test_client.get("/api/reservations/999?user_id=1", headers=customer_auth_headers)
    assert response.status_code == 404
    assert response.json["error"] == "Reserva no encontrada"

def test_customer_create_reservation_invalid_data(test_client, customer_auth_headers):
    data = {"user_id": 1}  # Faltan restaurant_id, reservation_date, num_guests, special_requests y status
    response = test_client.post("/api/reservations", json=data, headers=customer_auth_headers)
    assert response.status_code == 400
    assert response.json["error"] == "Faltan datos requeridos"

def test_customer_update_own_reservation(test_client, customer_auth_headers, customer_reservation_data):
    # Primero crea una reserva
    response = test_client.post("/api/reservations", json=customer_reservation_data, headers=customer_auth_headers)
    assert response.status_code == 201
    reservation_id = response.json["id"]
    user_id = customer_reservation_data["user_id"]

    # Ahora actualiza la reserva
    update_data = {
        "user_id": user_id,
        "restaurant_id": 1,
        "reservation_date": datetime.now().isoformat(),
        "num_guests": 5,
        "special_requests": "Near the bar",
        "status": "confirmed"
    }
    response = test_client.put(f"/api/reservations/{reservation_id}?user_id={user_id}", json=update_data, headers=customer_auth_headers)
    assert response.status_code == 200
    assert response.json["user_id"] == update_data["user_id"]
    assert response.json["restaurant_id"] == update_data["restaurant_id"]
    assert response.json["num_guests"] == update_data["num_guests"]
    assert response.json["special_requests"] == update_data["special_requests"]
    assert response.json["status"] == update_data["status"]

def test_customer_update_nonexistent_reservation(test_client, customer_auth_headers):
    update_data = {
        "user_id": 1,
        "restaurant_id": 1,
        "reservation_date": datetime.now().isoformat(),
        "num_guests": 5,
        "special_requests": "Near the bar",
        "status": "confirmed"
    }
    response = test_client.put("/api/reservations/999?user_id=1", json=update_data, headers=customer_auth_headers)
    assert response.status_code == 404
    assert response.json["error"] == "Reserva no encontrada"

def test_customer_delete_own_reservation(test_client, customer_auth_headers, customer_reservation_data):
    # Primero crea una reserva
    response = test_client.post("/api/reservations", json=customer_reservation_data, headers=customer_auth_headers)
    assert response.status_code == 201
    reservation_id = response.json["id"]
    user_id = customer_reservation_data["user_id"]

    # Ahora elimina la reserva utilizando un parámetro de consulta
    response = test_client.delete(f"/api/reservations/{reservation_id}?user_id={user_id}", headers=customer_auth_headers)
    assert response.status_code == 204

    # Verifica que la reserva ha sido eliminada
    response = test_client.get(f"/api/reservations/{reservation_id}?user_id={user_id}", headers=customer_auth_headers)
    assert response.status_code == 404
    assert response.json["error"] == "Reserva no encontrada"

def test_customer_delete_nonexistent_reservation(test_client, customer_auth_headers):
    response = test_client.delete("/api/reservations/999?user_id=1", headers=customer_auth_headers)
    assert response.status_code == 404
    assert response.json["error"] == "Reserva no encontrada"
