import pytest
from helpers import RegGenMethod
from methods_api import ApiMethods


@pytest.fixture
def courier():
    courier = RegGenMethod()
    payload = courier.register_new_courier_and_return_login_password()
    yield payload

@pytest.fixture
def courier_delete(courier):
    yield courier
    login_response = ApiMethods.login_courier(courier["login"], courier["password"])
    courier_id = login_response.json()["id"]
    ApiMethods.delete_courier(courier_id)

@pytest.fixture()
def create_courier(courier):
    response = ApiMethods.create_courier(courier)
    yield response

@pytest.fixture()
def login_courier(courier, create_courier):
    response = ApiMethods.login_courier(courier['login'], courier['password'])
    yield response