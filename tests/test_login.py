import allure
from data import Data
from helpers import Helper
from api_methods import ApiMethods


@allure.title('API тесты логина пользователя')
class TestLogin:

    @allure.title('Проверка успешной авторизации под существующим пользователем')
    def test_correct_user_login(self):
        create_body = Helper.create_user()
        ApiMethods.create_user(create_body)
        login_body = Helper.get_login_body(create_body)
        login_response = ApiMethods.login_user(login_body)
        headers = Helper.get_auth_token_to_create_header(login_response)
        ApiMethods.delete_user(headers)

        assert login_response.status_code == 200 and login_response.json()['success'] == True

    @allure.title('Проверка невозможности авторизации с некорректным логином и паролем')
    def test_login_with_incorrect_login_and_password(self):
        body = Helper.create_incorrect_login_body()
        response = ApiMethods.login_user(body)

        assert response.status_code == 401 and response.json()['message'] == Data.TEXT_INCORRECT_LOGIN_DATA

    @allure.title('Проверка невозможности авторизации с пустым email')
    def test_login_without_email(self):
        body = Helper.create_login_body_without_email()
        response = ApiMethods.login_user(body)

        assert response.status_code == 401 and response.json()['message'] == Data.TEXT_INCORRECT_LOGIN_DATA

    @allure.title('Проверка невозможности авторизации с пустым паролем')
    def test_login_without_password(self):
        body = Helper.create_login_body_without_password()
        response = ApiMethods.login_user(body)

        assert response.status_code == 401 and response.json()['message'] == Data.TEXT_INCORRECT_LOGIN_DATA