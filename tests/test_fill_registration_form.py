from pages.registration_page import RegistrationPage

def test_fill_registration_form(driver):
    """
    Проверка: можно заполнить все поля формы регистрации.
    """
    reg = RegistrationPage(driver)
    reg.open_registration_page()

    reg.fill_registration_form(
        first_name="Ivan",
        last_name="Ivanov",
        email="ivanov_test_001@example.com",
        password="TestPassword123!"
    )
