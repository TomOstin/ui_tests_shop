from pages.home_page import HomePage
from pages.product_page import ProductPage

def test_cart_redirect(driver):
    """
    Проверка: добавление товара в корзину и переход в корзину через ссылку.
    """
    home = HomePage(driver)
    home.open_home_page()
    home.navigate_to_jackets()

    product = ProductPage(driver)
    product.open_first_product()
    product.add_to_cart()

    assert product.is_success_message_visible(), "Сообщение об успешном добавлении отсутствует"

    product.click_shopping_cart_link()

    assert "checkout/cart" in driver.current_url, "Не произошёл переход на страницу корзины"
