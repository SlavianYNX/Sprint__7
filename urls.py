class Urls:

    MAIN_SITE = 'https://qa-scooter.praktikum-services.ru'
    LOGIN_COURIER = MAIN_SITE + '/api/v1/courier/login'
    CREATE_COURIER = MAIN_SITE + '/api/v1/courier'
    DELETE_COURIER = MAIN_SITE + '/api/v1/courier/'
    CREATE_ORDER = MAIN_SITE + '/api/v1/orders'
    GET_ORDER = MAIN_SITE + '/api/v1/orders'
    ACCEPT_ORDER = MAIN_SITE + '/api/v1/orders/accept/'
    ACCEPT_ORDER_TRACK = MAIN_SITE + '/api/v1/orders/accept/track'
    GET_ORDER_TRACK = MAIN_SITE + '/api/v1/orders/track'
    CANCEL_ORDER = MAIN_SITE + '/api/v1/orders/cancel'