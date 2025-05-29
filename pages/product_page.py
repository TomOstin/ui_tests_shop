from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class ProductPage(BasePage):
    """
    Страница товара: открытие, добавление в корзину, проверка заголовка, цены и уведомлений.
    """

    FIRST_PRODUCT = (By.CSS_SELECTOR, "li.product-item a.product-item-link")
    SIZE_OPTION = (By.CSS_SELECTOR, "div.swatch-attribute.size div[option-label]")
    COLOR_OPTION = (By.CSS_SELECTOR, "div.swatch-attribute.color div[option-label]")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button#product-addtocart-button")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.message-success.success.message")
    SUCCESS_CART_LINK = (By.CSS_SELECTOR, "div.message-success.success.message a")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "span.base")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "span.price")
    SIZE_SELECTOR = (By.CSS_SELECTOR, "div.swatch-attribute.size")

    def open_first_product(self):
        """Открывает первый товар из каталога."""
        self.click(*self.FIRST_PRODUCT)

    def add_to_cart(self):
        """Выбирает размер, цвет и добавляет товар в корзину."""
        self.click(*self.SIZE_OPTION)
        self.click(*self.COLOR_OPTION)
        self.click(*self.ADD_TO_CART_BUTTON)

    def get_success_message(self):
        """Возвращает текст сообщения об успешном добавлении в корзину."""
        element = self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE))
        return element.text

    def is_success_message_visible(self):
        """Проверяет наличие сообщения об успешном добавлении в корзину."""
        try:
            return self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE)).is_displayed()
        except:
            return False

    def click_shopping_cart_link(self):
        """Кликает по ссылке в сообщении и переходит в корзину."""
        self.click(*self.SUCCESS_CART_LINK)

    def is_title_visible(self):
        """Проверяет, отображается ли заголовок товара."""
        try:
            return self.wait.until(EC.visibility_of_element_located(self.PRODUCT_TITLE)).is_displayed()
        except:
            return False

    def is_price_visible(self):
        """Проверяет, отображается ли цена товара."""
        try:
            return self.wait.until(EC.visibility_of_element_located(self.PRODUCT_PRICE)).is_displayed()
        except:
            return False

    def is_size_selector_visible(self):
        """Проверяет, отображается ли блок выбора размера."""
        try:
            return self.wait.until(EC.visibility_of_element_located(self.SIZE_SELECTOR)).is_displayed()
        except:
            return False
