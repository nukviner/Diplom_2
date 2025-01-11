import allure
from data import Data
from helpers import Helper
from api_methods import ApiMethods


@allure.title('API тесты получения списка заказов конкретного пользователя')
class TestGetUserOrders:

    @allure.title('Проверка получения списка заказов авторизованного пользователя')
    def test_get_user_orders(self, headers_after_login):
        order_1 = Helper.create_body_for_order()
        ApiMethods.create_order_auth(headers_after_login, order_1)
        order_2 = Helper.create_body_for_order()
        ApiMethods.create_order_auth(headers_after_login, order_2)
        response = ApiMethods.get_user_orders_with_auth(headers_after_login)

        assert response.status_code == 200 and len(response.json()['orders']) == 2

    @allure.title('Проверка получения списка заказов не авторизованного пользователя')
    def test_get_user_orders_without_auth(self):
        response = ApiMethods.get_user_orders_without_auth()

        assert (response.status_code == 401 and response.json()['message'] == Data.TEXT_NOT_AUTHORISED_GET_ORDER)
