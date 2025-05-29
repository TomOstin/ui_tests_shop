from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage

class CatalogPage(BasePage):
    SORT_DROPDOWN = (By.ID, "sorter")
    PRODUCT_PRICES = (By.CSS_SELECTOR, ".price-wrapper .price")

    def sort_by(self, option_text):
        dropdown = self.wait.until(EC.element_to_be_clickable(self.SORT_DROPDOWN))
        select = Select(dropdown)
        select.select_by_visible_text(option_text)

    def get_all_prices(self):
        self.wait.until(EC.presence_of_all_elements_located(self.PRODUCT_PRICES))
        price_elements = self.driver.find_elements(*self.PRODUCT_PRICES)
        prices = []
        for elem in price_elements:
            raw = elem.text.replace("$", "").replace(",", "").strip()
            try:
                prices.append(float(raw))
            except ValueError:
                continue
        return prices
