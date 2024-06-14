from flask import Blueprint, request, jsonify
from app.models.reserva_model import Reservation
from app.views.reserva_view import render_reservation_detail, render_reservation_list
from app.utils.decorators import jwt_required, role_required
from datetime import datetime

reservation_bp = Blueprint("reservation", __name__)


@reservation_bp.route("/reservations", methods=["GET"])
@jwt_required
@role_required("admin", "customer")
def get_reservations():
    reservations = Reservation.get_all()
    return jsonify(render_reservation_list(reservations))

@reservation_bp.route("/reservations/<int:id>", methods=["GET"])
@jwt_required
@role_required("admin", "customer")
def get_reservation(id):
    reservation = Reservation.get_by_id(id)
    if reservation:
        return jsonify(render_reservation_detail(reservation))
    return jsonify({"error":"Reserva no encontrada"}), 404

@reservation_bp.route("/reservations", methods=["POST"])
@jwt_required
@role_required("admin", "customer")
def create_reservation():
    data = request.json
    user_id = data.get("user_id")
    restaurant_id = data.get("restaurant_id")
    if data.get("reservation_date") is not None: 
        reservation_date = datetime.fromisoformat(data.get("reservation_date").replace('Z', '+00:00'))
    num_guests = data.get("num_guests")
    special_requests = data.get("special_requests")
    status = data.get("status")

    if not user_id or not restaurant_id or not num_guests or not special_requests or not status or not reservation_date:
        return jsonify({"error":"Faltan datos requeridos"}), 400
       

    reservation = Reservation(user_id=user_id, restaurant_id=restaurant_id, reservation_date=reservation_date, num_guests=num_guests, special_requests=special_requests, status=status)
    reservation.save()
    return jsonify(render_reservation_detail(reservation)), 201


@reservation_bp.route("/reservations/<int:id>", methods=["PUT"])
@jwt_required
@role_required("admin", "customer")
def update_reserva(id):
    reservation = Reservation.get_by_id(id)
    if not reservation:
        return jsonify({"error":"Reserva no encontrada"}), 404
    
    data = request.json
    user_id = data.get("user_id")
    restaurant_id = data.get("restaurant_id")
    reservation_date = datetime.fromisoformat(data.get("reservation_date").replace('Z', '+00:00'))
    num_guests = data.get("num_guests")
    special_requests = data.get("special_requests")
    status = data.get("status")

    reservation.update(user_id=user_id, restaurant_id=restaurant_id, reservation_date=reservation_date, num_guests=num_guests,special_requests=special_requests, status=status)
    return jsonify(render_reservation_detail(reservation))

@reservation_bp.route("/reservations/<int:id>", methods=["DELETE"])
@jwt_required
@role_required("admin", "customer")
def delete_reservation(id):
    reservation = Reservation.get_by_id(id)
    if not reservation:
        return jsonify({"error":"Reserva no encontrada"}),404
    
    reservation.delete()

    return "", 204