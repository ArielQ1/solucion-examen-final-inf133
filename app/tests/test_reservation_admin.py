import pytest
from datetime import datetime

def test_get_reservations(test_client, admin_auth_headers):
    response = test_client.get("/api/reservations", headers=admin_auth_headers)
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_create_reservation(test_client, admin_auth_headers):
    data = {
        "user_id": 1,
        "restaurant_id": 1,
        "reservation_date": datetime.now().isoformat(),
        "num_guests": 4,
        "special_requests": "Window seat",
        "status": "pending"
    }
    response = test_client.post("/api/reservations", json=data, headers=admin_auth_headers)
    assert response.status_code == 201
    assert response.json["user_id"] == 1
    assert response.json["restaurant_id"] == 1
    assert response.json["num_guests"] == 4
    assert response.json["special_requests"] == "Window seat"
    assert response.json["status"] == "pending"

def test_get_reservation(test_client, admin_auth_headers):
    # Primero crea una reserva
    data = {
        "user_id": 1,
        "restaurant_id": 1,
        "reservation_date": datetime.now().isoformat(),
        "num_guests": 4,
        "special_requests": "Window seat",
        "status": "pending"
    }
    response = test_client.post("/api/reservations", json=data, headers=admin_auth_headers)
    assert response.status_code == 201
    reservation_id = response.json["id"]

    # Ahora obtén la reserva
    response = test_client.get(f"/api/reservations/{reservation_id}", headers=admin_auth_headers)
    assert response.status_code == 200
    assert response.json["user_id"] == 1
    assert response.json["restaurant_id"] == 1
    assert response.json["num_guests"] == 4
    assert response.json["special_requests"] == "Window seat"
    assert response.json["status"] == "pending"

def test_get_nonexistent_reservation(test_client, admin_auth_headers):
    response = test_client.get("/api/reservations/999", headers=admin_auth_headers)
    assert response.status_code == 404
    assert response.json["error"] == "Reserva no encontrada"

def test_create_reservation_invalid_data(test_client, admin_auth_headers):
    data = {"user_id": 1}  # Faltan restaurant_id, reservation_date, num_guests, special_requests y status
    response = test_client.post("/api/reservations", json=data, headers=admin_auth_headers)
    assert response.status_code == 400
    assert response.json["error"] == "Faltan datos requeridos"

def test_update_reservation(test_client, admin_auth_headers):
    # Primero crea una reserva
    data = {
        "user_id": 1,
        "restaurant_id": 1,
        "reservation_date": datetime.now().isoformat(),
        "num_guests": 4,
        "special_requests": "Window seat",
        "status": "pending"
    }
    response = test_client.post("/api/reservations", json=data, headers=admin_auth_headers)
    assert response.status_code == 201
    reservation_id = response.json["id"]

    # Ahora actualiza la reserva
    update_data = {
        "user_id": 1,
        "restaurant_id": 1,
        "reservation_date": datetime.now().isoformat(),
        "num_guests": 5,
        "special_requests": "Near the bar",
        "status": "confirmed"
    }
    response = test_client.put(f"/api/reservations/{reservation_id}", json=update_data, headers=admin_auth_headers)
    assert response.status_code == 200
    assert response.json["user_id"] == 1
    assert response.json["restaurant_id"] == 1
    assert response.json["num_guests"] == 5
    assert response.json["special_requests"] == "Near the bar"
    assert response.json["status"] == "confirmed"

def test_update_nonexistent_reservation(test_client, admin_auth_headers):
    update_data = {
        "user_id": 1,
        "restaurant_id": 1,
        "reservation_date": datetime.now().isoformat(),
        "num_guests": 5,
        "special_requests": "Near the bar",
        "status": "confirmed"
    }
    response = test_client.put("/api/reservations/999", json=update_data, headers=admin_auth_headers)
    assert response.status_code == 404
    assert response.json["error"] == "Reserva no encontrada"

def test_delete_reservation(test_client, admin_auth_headers):
    # Primero crea una reserva
    data = {
        "user_id": 1,
        "restaurant_id": 1,
        "reservation_date": datetime.now().isoformat(),
        "num_guests": 4,
        "special_requests": "Window seat",
        "status": "pending"
    }
    response = test_client.post("/api/reservations", json=data, headers=admin_auth_headers)
    assert response.status_code == 201
    reservation_id = response.json["id"]

    # Ahora elimina la reserva
    response = test_client.delete(f"/api/reservations/{reservation_id}", headers=admin_auth_headers)
    assert response.status_code == 204

    # Verifica que la reserva ha sido eliminada
    response = test_client.get(f"/api/reservations/{reservation_id}", headers=admin_auth_headers)
    assert response.status_code == 404
    assert response.json["error"] == "Reserva no encontrada"

def test_delete_nonexistent_reservation(test_client, admin_auth_headers):
    response = test_client.delete("/api/reservations/999", headers=admin_auth_headers)
    assert response.status_code == 404
    assert response.json["error"] == "Reserva no encontrada"
