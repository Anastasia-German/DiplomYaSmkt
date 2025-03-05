# Анастасия Герман, 27а когорта — Финальный проект. Инженер по тестированию расширенный
import sender_stand_request
import data


def test_polychit_dannie_o_zakaze_po_treky():
    response = sender_stand_request.create_order(data.order_body)
    track_number = response.json()["track"]
    order_response = sender_stand_request.get_order(track_number)
    assert order_response.status_code == 200