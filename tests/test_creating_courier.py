import pytest
import allure
from conftest import courier, courier_delete, create_courier
from methods_api import ApiMethods
from data import TestMessages


class TestCourierMethods:

    @allure.title('Проверка создания нового курьера')
    @allure.description('Отправка запроса на создание курьера. Получение сообщения об успешном создании курьера')
    def test_creating_courier(self, courier, create_courier, courier_delete):
        r = create_courier
        assert r.status_code == 201 and r.json() == TestMessages.COURIER_SUCCESSFUL_CREATION


    @allure.title('Проверка получения сообщения об ошибке при создания двух одинаковых курьеров')
    @allure.description('Отправка запроса на создание двух курьеров с одинаковыми логинами, получение сообщения об ошибке')
    def test_two_creating_courier(self, courier, create_courier, courier_delete):
        w = ApiMethods.create_courier(courier)
        assert w.status_code == 409 and w.json() == TestMessages.COURIER_LOGIN_ALREADY_IN_USE


    @allure.title('Проверка создания курьера при пустом поле "login"')
    @allure.description('Отправка запроса на создание курьера без заполнения поля login, получение сообщения об ошибке ')
    def test_creating_courier_no_login(self, courier, create_courier):
        courier["login"] = ""
        r = ApiMethods.create_courier(courier)
        assert r.status_code == 400 and r.json() == TestMessages.COURIER_NOT_ENOUGH_REGISTER_DATA

    @allure.title('Проверка создания курьера при пустом поле "password"')
    @allure.description('Отправка запроса на создание курьера без заполнения поля password, получение сообщения об ошибке')
    def test_creating_courier_no_password(self, courier):
        courier["password"] = ""
        r = ApiMethods.create_courier(courier)
        assert r.status_code == 400 and r.json() == TestMessages.COURIER_NOT_ENOUGH_REGISTER_DATA

    @allure.title('Проверка создания курьера при пустом поле "firstName"')
    @allure.description('Отправка запроса на создание курьера без заполнения поля "firstName"')
    def test_creating_courier_no_firstname(self, courier):
        courier["firstName"] = ""
        r = ApiMethods.create_courier(courier)
        assert r.status_code == 201 and r.json() == TestMessages.COURIER_SUCCESSFUL_CREATION
