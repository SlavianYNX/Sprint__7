import pytest
from helpers import RegGenMethod


@pytest.fixture
def courier():
    courier = RegGenMethod()
    payload = courier.register_new_courier_and_return_login_password()
    yield payload

