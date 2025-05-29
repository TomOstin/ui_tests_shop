from pages.home_page import HomePage
from pages.product_page import ProductPage

def test_open_product_and_check_details(driver):
    """
    Проверка: можно открыть товар и увидеть его заголовок, цену и размеры.
    """
    home = HomePage(driver)
    home.open_home_page()
    home.navigate_to_jackets()

    product = ProductPage(driver)
    product.open_first_product()

    assert product.is_title_visible(), "Заголовок товара не найден"
    assert product.is_price_visible(), "Цена товара не найдена"
    assert product.is_size_selector_visible(), "Блок размеров не отображается"
