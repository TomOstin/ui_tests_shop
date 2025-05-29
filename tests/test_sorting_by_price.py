import pytest
from pages.home_page import HomePage
from pages.catalog_page import CatalogPage

@pytest.mark.ui
def test_sorting_by_price(driver):
    """
    Проверка: товары сортируются по возрастанию цены.
    """
    home = HomePage(driver)
    home.open_home_page()
    home.navigate_to_jackets()

    catalog = CatalogPage(driver)
    catalog.sort_by("Price")

    prices = catalog.get_all_prices()
    assert prices == sorted(prices), f"Цены отсортированы неверно: {prices}"
