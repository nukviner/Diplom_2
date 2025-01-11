class Urls:

    BASE_URL = 'https://stellarburgers.nomoreparties.site'

class Endpoints:

    CREATE_USER = '/api/auth/register'
    DELETE_USER = '/api/auth/user'
    LOGIN = '/api/auth/login'
    CHANGE_OR_GET_USER = '/api/auth/user'
    GET_USER_ORDERS = '/api/orders'
    CREATE_ORDER = '/api/orders'

class Data:

    USER_NAME = "TestUser"
    TEXT_EXISTED_USER = "User already exists"
    TEXT_NO_REQUIRED_DATA = "Email, password and name are required fields"
    TEXT_INCORRECT_LOGIN_DATA = "email or password are incorrect"
    TEXT_EXISTED_EMAIL = "User with such email already exists"
    TEXT_NOT_AUTHORISED = "You should be authorised"
    TEXT_NO_INGREDIENTS = "Ingredient ids must be provided"
    TEXT_INCORRECT_IDC = "One or more ids provided are incorrect"
    TEXT_NOT_AUTHORISED_GET_ORDER = "You should be authorised"
    INGREDIENT_HASH = ['61c0c5a71d1f82001bdaaa73', '61c0c5a71d1f82001bdaaa6f']
    INCORRECT_INGREDIENT_HASH = ['99c0c5a71d1f82001bdaaa73', '99c0c5a71d1f82001bdaaa6f']
    ORDER_WITHOUT_INGREDIENTS = {"ingredients": []}
    INCOMPLETE_DATA = [{'email': '', 'password': 'somepass', 'name': 'Имя'},
                       {'email': 'testmail01@ya.ru', 'password': '', 'name': 'Тожеимя'},
                       {'email': 'testmail02@ya.ru', 'password': 'anotherpass', 'name': ''}]
