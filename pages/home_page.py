from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage

class HomePage(BasePage):
    """
    Класс для главной страницы сайта.
    Содержит действия: открытие, проверка логотипа, переход к разделу товаров.
    """

    # Локаторы
    LOGO = (By.CSS_SELECTOR, "a.logo")
    MEN_MENU = (By.LINK_TEXT, "Men")
    TOPS_MENU = (By.LINK_TEXT, "Tops")
    JACKETS_MENU = (By.LINK_TEXT, "Jackets")

    def open_home_page(self):
        """
        Открывает главную страницу магазина.
        """
        self.open("https://magento.softwaretestingboard.com/")

    def is_logo_displayed(self):
        """
        Проверяет наличие логотипа на странице.
        :return: True, если логотип найден, иначе False
        """
        try:
            self.find(*self.LOGO)
            return True
        except:
            return False

    def navigate_to_jackets(self):
        """
        Наводит курсор: Men → Tops → Jackets и кликает.
        """
        actions = ActionChains(self.driver)

        men = self.find(*self.MEN_MENU)
        actions.move_to_element(men).perform()

        # Появляется Tops после hover
        tops = self.wait.until(lambda d: d.find_element(*self.TOPS_MENU))
        actions.move_to_element(tops).perform()

        # Появляется Jackets → кликаем
        jackets = self.wait.until(lambda d: d.find_element(*self.JACKETS_MENU))
        actions.move_to_element(jackets).click().perform()
