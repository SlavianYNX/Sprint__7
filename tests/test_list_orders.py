import pytest
import allure
from methods_api import ApiMethods


class TestGetOrder:

    @allure.title('Проверка получения списка заказов ')
    @allure.description('Отправка запроса на получения списка заказов')
    def test_get_list_order(self):
        r = ApiMethods.get_order_list()
        assert r.status_code == 200 and 'orders' in r.json()
