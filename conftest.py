import pytest
from helpers import Helper
from api_methods import ApiMethods


@pytest.fixture
def headers_after_login():
    create_body = Helper.create_user()
    ApiMethods.create_user(create_body)
    login_body = Helper.get_login_body(create_body)
    login_response = ApiMethods.login_user(login_body)
    headers = Helper.get_auth_token_to_create_header(login_response)
    yield headers
    ApiMethods.delete_user(headers)

@pytest.fixture
def headers_after_create():
    create_body = Helper.create_user()
    create_response = ApiMethods.create_user(create_body)
    headers = Helper.get_auth_token_to_create_header(create_response)
    yield headers
    ApiMethods.delete_user(headers)
