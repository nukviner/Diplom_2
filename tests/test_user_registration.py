import allure
import pytest
from data import Data
from helpers import Helper
from api_methods import ApiMethods


@allure.title('API тесты регистрации пользователя')
class TestUserRegistration:

    @allure.title('Проверка регистрации нового уникального пользователя')
    def test_new_user_registration(self):
        body = Helper.create_user()
        response = ApiMethods.create_user(body)
        headers = Helper.get_auth_token_to_create_header(response)
        delete_new_user = ApiMethods.delete_user(headers)

        assert (response.status_code == 200 and response.json()['user']['name'] == Data.USER_NAME and delete_new_user.status_code == 202)

    @allure.title('Проверка регистрации уже существующего пользователя')
    def test_existed_user_registration(self):
        body = Helper.create_user()
        response = ApiMethods.create_user(body)
        response_exist = ApiMethods.create_user(body)
        headers = Helper.get_auth_token_to_create_header(response)
        ApiMethods.delete_user(headers)

        assert response_exist.status_code == 403 and response_exist.json()['message'] == Data.TEXT_EXISTED_USER

    @pytest.mark.parametrize('body', Data.INCOMPLETE_DATA)
    @allure.title('Проверка невозможности регистрации нового пользователя без заполнения одного из обязательных полей')
    def test_new_user_with_incomplete_data(self, body):
        response = ApiMethods.create_user(body)

        assert (response.status_code == 403 and response.json()['message'] == Data.TEXT_NO_REQUIRED_DATA)