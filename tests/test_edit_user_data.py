import allure
from data import Data
from helpers import Helper
from api_methods import ApiMethods


@allure.title('API тесты изменения данных пользователя')
class TestChangeUser:

    @allure.title('Проверка изменения данных авторизованного пользователя')
    def test_change_user_success(self, headers_after_login):
        change_body = Helper.create_user()
        response = ApiMethods.change_user_with_auth(headers_after_login, change_body)

        assert (response.status_code == 200 and response.json()['user']['name'] == change_body['name'] and response.json()['user']['email'] == change_body['email'])

    @allure.title('Проверка невозможности изменения данных не авторизованного пользователя')
    def test_change_user_without_auth(self, headers_after_create):
        change_body = Helper.create_user()
        response = ApiMethods.change_user_without_auth(change_body)

        assert response.status_code == 401 and response.json()['message'] == Data.TEXT_NOT_AUTHORISED
