import pytest
from pages.home_page import HomePage

@pytest.mark.ui
def test_home_page_logo_displayed(driver):
    """
    Проверка, что логотип отображается на главной странице.
    """
    page = HomePage(driver)
    page.open_home_page()

    assert page.is_logo_displayed(), "Логотип не отображается на главной странице"
