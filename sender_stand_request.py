import configuration
import requests
import data 


def create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=body)


def get_order(track_number):
    url_order = f"{configuration.URL_SERVICE}/api/v1/orders/track?t={track_number}"
    return requests.get(url_order)
