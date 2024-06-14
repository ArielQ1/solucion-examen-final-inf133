def test_customer_get_restaurants(test_client, customer_auth_headers):
    response = test_client.get("/api/restaurants", headers=customer_auth_headers)
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_customer_get_restaurant(test_client, customer_auth_headers, admin_auth_headers):
    # Primero crea un restaurante como admin para que el cliente pueda verlo
    admin_data = {
        "name": "Burger Palace",
        "address": "456 Elm Street",
        "city": "Shelbyville",
        "phone": "555-5678",
        "description": "The best burgers in town.",
        "rating": 4.2
    }
    admin_response = test_client.post("/api/restaurants", json=admin_data, headers=admin_auth_headers)
    assert admin_response.status_code == 201
    restaurant_id = admin_response.json["id"]

    # Ahora obtén el restaurante como cliente
    response = test_client.get(f"/api/restaurants/{restaurant_id}", headers=customer_auth_headers)
    assert response.status_code == 200
    assert response.json["name"] == "Burger Palace"
    assert response.json["address"] == "456 Elm Street"
    assert response.json["city"] == "Shelbyville"
    assert response.json["phone"] == "555-5678"
    assert response.json["description"] == "The best burgers in town."
    assert response.json["rating"] == 4.2

def test_customer_get_nonexistent_restaurant(test_client, customer_auth_headers):
    response = test_client.get("/api/restaurants/999", headers=customer_auth_headers)
    assert response.status_code == 404
    assert response.json["error"] == "Restaurante no encontrado"

def test_customer_create_restaurant(test_client, customer_auth_headers):
    data = {
        "name": "Gourmet Plaza",
        "address": "123 Main Street",
        "city": "Springfield",
        "phone": "555-1234",
        "description": "A fine dining experience.",
        "rating": 4.5
    }
    response = test_client.post("/api/restaurants", json=data, headers=customer_auth_headers)
    assert response.status_code == 403
    assert response.json["error"] == "No tiene permiso para realizar esta acción"

def test_customer_update_restaurant(test_client, customer_auth_headers):
    update_data = {
        "name": "Pizza Haven",
        "address": "789 Oak Street",
        "city": "Evergreen",
        "phone": "555-6789",
        "description": "The best pizza in town.",
        "rating": 4.5
    }
    response = test_client.put("/api/restaurants/1", json=update_data, headers=customer_auth_headers)
    assert response.status_code == 403
    assert response.json["error"] == "No tiene permiso para realizar esta acción"

def test_customer_delete_restaurant(test_client, customer_auth_headers):
    response = test_client.delete("/api/restaurants/1", headers=customer_auth_headers)
    assert response.status_code == 403
    assert response.json["error"] == "No tiene permiso para realizar esta acción"
