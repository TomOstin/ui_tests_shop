from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """
    Базовый класс для всех страниц. Содержит общие действия над элементами.
    """

    def __init__(self, driver, timeout=10):
        """
        :param driver: экземпляр WebDriver
        :param timeout: максимальное время ожидания элементов на странице
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
        """
        Открывает указанный URL в браузере.
        """
        self.driver.get(url)

    def find(self, by, locator):
        """
        Ожидает появления элемента в DOM и возвращает его.
        :param by: метод поиска (например, By.ID, By.CSS_SELECTOR)
        :param locator: локатор элемента
        :return: WebElement
        """
        return self.wait.until(EC.presence_of_element_located((by, locator)))

    def click(self, by, locator):
        """
        Кликает по элементу.
        """
        element = self.find(by, locator)
        element.click()

    def type(self, by, locator, text):
        """
        Вводит текст в элемент (очищая его перед этим).
        """
        element = self.find(by, locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, by, locator):
        """
        Получает текст элемента.
        """
        element = self.find(by, locator)
        return element.text

    def is_visible(self, by, locator):
        """
        Проверяет, виден ли элемент на странице (без исключений при отсутствии).
        :return: True, если элемент виден, иначе False
        """
        try:
            self.wait.until(EC.visibility_of_element_located((by, locator)))
            return True
        except:
            return False
