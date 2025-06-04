import pytest
import allure
import data
from methods_api import ApiMethods
from data import color_select


class TestOrderMethods:

    @allure.title('Проверка создания заказа')
    @allure.description('Отправка запроса на создание заказа. Получение сообщения об успешном создании заказа')
    @pytest.mark.parametrize('color', color_select)
    def test_creating_order(self, color):
        data.order_["color"] = color
        r = ApiMethods.order_create(data.order_)
        assert r.status_code == 201 and 'track' in r.json()
        ApiMethods.cancellation_order(r.json())





