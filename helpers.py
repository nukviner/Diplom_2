import random
import allure
from data import Data


class Helper:

    @staticmethod
    @allure.title('Генерация email')
    def generate_email():
        return f"generated_email_{random.randint(100, 999)}@yandex.ru"

    @staticmethod
    @allure.title('Генерация пароля')
    def generate_password():
        return f"QWE{random.randint(10, 99)}-{random.randint(10, 99)}"

    @staticmethod
    @allure.title('Создание пользователя')
    def create_user():
        email = Helper.generate_email()
        password = Helper.generate_password()
        body = {
            "email": email,
            "password": password,
            "name": Data.USER_NAME
        }
        return body

    @staticmethod
    @allure.title('Получение токена авторизации для создания заголовков')
    def get_auth_token_to_create_header(response):
        user_token = response.json()['accessToken']
        headers = {'Authorization': f'{user_token}'}
        return headers

    @staticmethod
    @allure.title('Получение тела запроса')
    def get_login_body(create_body):
        email = create_body['email']
        password = create_body['password']
        login_body = {
            "email": email,
            "password": password,
        }
        return login_body

    @staticmethod
    @allure.title('Создание некорректного тела запроса')
    def create_incorrect_login_body():
        email = Helper.generate_password()
        password = Helper.generate_email()
        body = {
            "email": email,
            "password": password,
        }
        return body

    @staticmethod
    @allure.title('Создание тела запроса для авторизации без email')
    def create_login_body_without_email():
        password = Helper.generate_password()
        body = {
            "email": "",
            "password": password,
        }
        return body

    @staticmethod
    @allure.title('Создание тела запроса для авторизации без пароля')
    def create_login_body_without_password():
        email = Helper.generate_email()
        body = {
            "email": email,
            "password": "",
        }
        return body

    @staticmethod
    @allure.title('Создание корректного тела запроса для оформления заказа')
    def create_body_for_order():
        body = {"ingredients": Data.INGREDIENT_HASH}
        return body

    @staticmethod
    @allure.title('Создание некорректного тела запроса для оформления заказа')
    def create_incorrect_body_for_order():
        body = {"ingredients": Data.INCORRECT_INGREDIENT_HASH}
        return body
