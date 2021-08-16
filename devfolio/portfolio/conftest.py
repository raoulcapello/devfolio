import pytest
from django.contrib.auth import get_user_model
from selenium import webdriver

User = get_user_model()


# Fixture for Chrome
@pytest.fixture(scope="class")
def chrome_driver_init(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    chrome_driver = webdriver.Chrome(
        "node_modules/chromedriver/bin/chromedriver", options=options
    )
    request.cls.driver = chrome_driver
    yield
    chrome_driver.close()


# @pytest.fixture
# def authenticated_user(client):
#     # Create user
#     username = 'user1'
#     password = 'Eomeib4d'
#     user = User.objects.create_user(username, password)
#     # Log user in
#     client.login(username=username, password=password)
#     return user
