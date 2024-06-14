def render_reservation_detail(reservation):
    return {
        'id': reservation.id,
        'user_id': reservation.user_id,
        'restaurant_id': reservation.restaurant_id,
        'reservation_date': reservation.reservation_date,
        'num_guests': reservation.num_guests,
        'special_requests': reservation.special_requests,
        'status': reservation.status,
    }

def render_reservation_list(reservations):
    return [
        {
            'id': reservation.id,
            'user_id': reservation.user_id,
            'restaurant_id': reservation.restaurant_id,
            'reservation_date': reservation.reservation_date,
            'num_guests': reservation.num_guests,
            'special_requests': reservation.special_requests,
            'status': reservation.status,
        }
        for reservation in reservations
    ]