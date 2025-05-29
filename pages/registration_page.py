from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RegistrationPage(BasePage):
    """
    Страница регистрации нового пользователя.
    """

    FIRST_NAME = (By.ID, "firstname")
    LAST_NAME = (By.ID, "lastname")
    EMAIL = (By.ID, "email_address")
    PASSWORD = (By.ID, "password")
    CONFIRM_PASSWORD = (By.ID, "password-confirmation")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[title='Create an Account']")

    def open_registration_page(self):
        self.open("https://magento.softwaretestingboard.com/customer/account/create/")

    def fill_registration_form(self, first_name, last_name, email, password):
        self.type(*self.FIRST_NAME, text=first_name)
        self.type(*self.LAST_NAME, text=last_name)
        self.type(*self.EMAIL, text=email)
        self.type(*self.PASSWORD, text=password)
        self.type(*self.CONFIRM_PASSWORD, text=password)
