from pages.login_page import LoginPage

def test_invalid_login_shows_error(driver):
    """
    Проверка: при неверных данных входа отображается сообщение об ошибке.
    """
    login_page = LoginPage(driver)
    login_page.open("https://magento.softwaretestingboard.com/")
    login_page.go_to_login_page()
    login_page.login("fake@example.com", "wrongpass123")

    error = login_page.get_error_message()
    print("Ошибка отображается:", error)

    assert "The account sign-in was incorrect" in error
