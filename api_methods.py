import requests
import allure
from data import Urls, Endpoints


class ApiMethods:
    @staticmethod
    @allure.step('Cоздание пользователя')
    def create_user(body):
        return requests.post(f'{Urls.BASE_URL}{Endpoints.CREATE_USER}', json=body)

    @staticmethod
    @allure.step('Удаление пользователя')
    def delete_user(header):
        return requests.delete(f'{Urls.BASE_URL}{Endpoints.DELETE_USER}', headers=header)

    @staticmethod
    @allure.step('Авторизация пользователя')
    def login_user(body):
        return requests.post(f'{Urls.BASE_URL}{Endpoints.LOGIN}', json=body)

    @staticmethod
    @allure.step('Изменение данных авторизованного пользователя')
    def change_user_with_auth(header, body):
        return requests.patch(f'{Urls.BASE_URL}{Endpoints.CHANGE_OR_GET_USER}', headers=header, json=body)

    @staticmethod
    @allure.step('Изменения данных не авторизованного пользователя')
    def change_user_without_auth(body):
        return requests.patch(f'{Urls.BASE_URL}{Endpoints.CHANGE_OR_GET_USER}', json=body)

    @staticmethod
    @allure.step('Создание заказа авторизованного пользователя')
    def create_order_auth(header, body):
        return requests.post(f'{Urls.BASE_URL}{Endpoints.CREATE_ORDER}', headers=header, json=body)

    @staticmethod
    @allure.step('Создание заказа не авторизованного пользователя')
    def create_order_without_auth(body):
        return requests.post(f'{Urls.BASE_URL}{Endpoints.CREATE_ORDER}', json=body)

    @staticmethod
    @allure.step('Получение списка заказов авторизованного пользователя')
    def get_user_orders_with_auth(header):
        return requests.get(f'{Urls.BASE_URL}{Endpoints.GET_USER_ORDERS}', headers=header)

    @staticmethod
    @allure.step('Получение списка заказов не авторизованного пользователя')
    def get_user_orders_without_auth():
        return requests.get(f'{Urls.BASE_URL}{Endpoints.GET_USER_ORDERS}')
