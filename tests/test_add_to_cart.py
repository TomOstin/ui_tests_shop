from pages.home_page import HomePage
from pages.product_page import ProductPage

def test_add_product_to_cart(driver):
    """
    Проверка: товар успешно добавляется в корзину.
    """
    home = HomePage(driver)
    home.open("https://magento.softwaretestingboard.com/")
    home.navigate_to_jackets()

    product = ProductPage(driver)
    product.open_first_product()
    product.add_to_cart()

    success = product.get_success_message()
    print("Сообщение:", success)

    assert "You added" in success and "to your shopping cart." in success, "Ожидалось сообщение об успешном добавлении"
