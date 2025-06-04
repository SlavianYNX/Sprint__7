import pytest
import allure
from conftest import courier
from methods_api import ApiMethods
from data import TestMessages


class TestLoginMethods:


    @allure.title('Проверка авторизации и получение id курьера')
    @allure.description('Отправка запроса на авторизацию существующего курьера и получение его id. Удаление курьера из базы')
    def test_login_get_courier_id(self, courier):
        ApiMethods.create_courier(courier)
        r = ApiMethods.login_courier(courier['login'], courier['password'])
        p = ApiMethods.delete_courier(r.json()['id'])
        assert r.status_code == 200 and 'id' in r.json()
        assert p.status_code == 200 and p.json() == TestMessages.COURIER_DELETE

    @allure.title('Проверка авторизации при пустом поле "password"')
    @allure.description('Отправка запроса на авторизацию при пустом поле "password"')
    def test_login_none_password(self, courier):
        courier['password'] = ""
        r = ApiMethods.login_courier(courier['login'], courier['password'])
        assert r.status_code == 400 and r.json()== TestMessages.COURIER_NOT_ENOUGH_AUTHORIZATION_DATA


    @allure.title('Проверка авторизации с несуществующим паролем')
    @allure.description('Отправка запроса на авторизацию под несуществующим паролем')
    def test_login_fake_user(self, courier):
        ApiMethods.create_courier(courier)
        r = ApiMethods.login_courier(courier['login'], courier['password'][:-2])
        assert r.status_code == 404 and r.json() == TestMessages.COURIER_ACCOUNT_NOT_FOUND
