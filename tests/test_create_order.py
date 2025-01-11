import allure
from data import Data
from helpers import Helper
from api_methods import ApiMethods


@allure.title('API тесты создания заказа')
class TestCreateOrder:

    @allure.title('Проверка создания заказа авторизованным пользователем')
    def test_create_order_with_auth(self, headers_after_login):
        body = Helper.create_body_for_order()
        response = ApiMethods.create_order_auth(headers_after_login, body)

        assert response.status_code == 200 and response.json()['order']['status'] == 'done' and response.json()['order']['number'] is not None

    @allure.title('Проверка создания заказа не авторизованным пользователем')
    def test_create_order_without_auth(self, headers_after_create):
        body = Helper.create_body_for_order()
        response = ApiMethods.create_order_without_auth(body)

        assert response.status_code == 200

    @allure.title('Проверка невозможности создания заказа без ингредиентов авторизованным пользователем')
    def test_create_order_with_auth_without_ingredients(self, headers_after_login):
        body = Data.ORDER_WITHOUT_INGREDIENTS
        response = ApiMethods.create_order_auth(headers_after_login, body)

        assert (response.status_code == 400 and response.json()['message'] == Data.TEXT_NO_INGREDIENTS)

    @allure.title('Проверка невозможности создания заказа без ингредиентов не авторизованным пользователем')
    def test_create_order_without_auth_and_without_ingredients(self, headers_after_create):
        body = Data.ORDER_WITHOUT_INGREDIENTS
        response = ApiMethods.create_order_without_auth(body)

        assert (response.status_code == 400 and response.json()['message'] == Data.TEXT_NO_INGREDIENTS)

    @allure.title('Проверка создания заказа авторизованным пользователем с некорректным хешем ингредиентов')
    def test_create_order_with_false_hash(self, headers_after_login):
        body = Helper.create_incorrect_body_for_order()
        response = ApiMethods.create_order_auth(headers_after_login, body)

        assert (response.status_code == 400 and response.json()['message'] == Data.TEXT_INCORRECT_IDC)
