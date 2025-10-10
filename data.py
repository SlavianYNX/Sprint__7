class TestMessages:

    COURIER_SUCCESSFUL_CREATION = {'ok': True}
    COURIER_LOGIN_ALREADY_IN_USE = {"code": 409 , "message": "Этот логин уже используется. Попробуйте другой."}
    COURIER_NOT_ENOUGH_REGISTER_DATA = {"code": 400, "message": "Недостаточно данных для создания учетной записи"}
    COURIER_SUCCESSFUL_AUTHORIZATION = {"code": 200, "message": None}
    COURIER_NOT_ENOUGH_AUTHORIZATION_DATA = {"code": 400, "message": "Недостаточно данных для входа"}
    COURIER_ACCOUNT_NOT_FOUND = {"code": 404, "message": "Учетная запись не найдена"}
    COURIER_DELETE = {'ok': True}
    ORDER_SUCCESSFUL_CREATION = {"code": 201, "message": "track"}
    ORDER_GET_LIST_OF_ORDERS = {"code": 200, "message": "orders"}
    COURIER_NOT_IN_LIST = {"code": 404, "message": "Курьера с таким id нет."}
    COURIER_NOT_DATA_ID = {"code": 400, "message": "Недостаточно данных для удаления курьера"}
    ORDER_ACCEPT_NOT_COURIER = {"code": 404, "message": "Курьера с таким id не существует"}
    ORDER_ACCEPT_NOT_ID = {"code": 400, "message": "Недостаточно данных для поиска"}
    ORDER_ACCEPT_OK = {'ok': True}
    ORDER_CANCEL = {'ok': True}


order_ = {
    "firstName": "Анатолий",
    "lastName": "Чубайс",
    "address": "Москва, ул. Тверская, 45",
    "metroStation": 4,
    "phone": "+79129998877",
    "rentTime": 5,
    "deliveryDate": "2025-05-27",
    "comment": "Вход со двора",
    "color":"",
}

color_select =  [
            [],
            ["BLACK"],
            ["GREY"],
            ["BLACK", "GREY"]
        ]
