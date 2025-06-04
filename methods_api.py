import requests
from urls import Urls
import allure


class ApiMethods:

    @allure.step('Запрос на создание курьера')
    def create_courier(payload):
        return requests.post(f'{Urls.CREATE_COURIER}', data=payload)

    @allure.step('Запрос на удаление курьера')
    def delete_courier(id):
        return requests.delete(f'{Urls.DELETE_COURIER}{id}')

    @allure.step('Запрос на авторизацию курьера')
    def login_courier(login, password):
        return requests.post(f'{Urls.LOGIN_COURIER}', json={"login": login, "password": password})

    @allure.step('Запрос на создание заказа')
    def order_create(order):
        return requests.post(f'{Urls.CREATE_ORDER}', json=order)

    @allure.step('Запрос на получения списка заказов')
    def get_order_list():
        return requests.get(f'{Urls.GET_ORDER}')

    @allure.step('Запрос на принятие заказа')
    def acceptance_order(id, id_courier):
        return requests.put(f'{Urls.ACCEPT_ORDER}{id}?courierId={id_courier}')

    @allure.step('Получение id заказа по track')
    def get_id_order(t):
        return requests.get(f'{Urls.GET_ORDER_TRACK}?t={t}')

    @allure.step('Отмена заказа')
    def cancellation_order(track):
        return requests.put(f'{Urls.CANCEL_ORDER}', json={"track": track})