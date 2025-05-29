from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    """
    Класс для страницы входа.
    Содержит действия: переход, ввод email/пароля, нажатие кнопки входа и проверка ошибки.
    """

    # Локаторы
    SIGN_IN_LINK = (By.LINK_TEXT, "Sign In")
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "pass")
    SIGN_IN_BUTTON = (By.ID, "send2")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "div[data-ui-id='message-error']")

    def go_to_login_page(self):
        """
        Переход на страницу логина по ссылке "Sign In".
        """
        self.click(*self.SIGN_IN_LINK)

    def login(self, email, password):
        """
        Вводит логин и пароль, нажимает кнопку входа.
        :param email: почта пользователя
        :param password: пароль
        """
        self.type(*self.EMAIL_INPUT, text=email)
        self.type(*self.PASSWORD_INPUT, text=password)
        self.click(*self.SIGN_IN_BUTTON)

    def get_error_message(self):
        """
        Получает сообщение об ошибке при неудачном входе.
        :return: текст ошибки
        """
        return self.get_text(*self.ERROR_MESSAGE)
