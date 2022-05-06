import pytest
from selenium.webdriver.common.by import By
from pom_pages.hr_login_page import LoginPage


class TestLogin:

    # def setup_class(self):
    #     self.login_page = LoginPage()
    #     self.browser = self.login_page.get_driver_instance()

    @pytest.fixture
    def setup(self, pytestconfig):
	print('SETUP')
        browser_name = pytestconfig.getoption("browser_name")
        print('Browser ', browser_name)
        self.login_page = LoginPage()
        self.browser = self.login_page.get_driver_instance(browser_name)

    def teardown_class(self):
	print('teardown')
        self.browser.quit()

    def test_login(self, setup):
        print("LOGIN")
        self.login_page.hr_login('admin', 'password')
        assert self.browser.title == 'OrangeHRM'
    #
    # def test_invalid_user_login(self):
    #     self.login_page.hr_login('xadmin', 'password')
    #     text = self.browser.find_element(By.XPATH, '//*[@id="spanMessage"]').text
    #     assert text == 'Invalid credentials'
    #
    # def test_invalid_pw_login(self):
    #     self.login_page.hr_login('admin', 'pw')
    #     text = self.browser.find_element(By.XPATH, '//*[@id="spanMessage"]').text
    #     assert text == 'Invalid credentials'
