import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import os

def pytest_addoption(parser):
    """
    Добавляет опцию командной строки '--headed' для запуска браузера с GUI.
    По умолчанию тесты запускаются в headless-режиме.
    """
    parser.addoption("--headed", action="store_true", help="Открыть браузер с GUI (отключить headless)")

@pytest.fixture
def driver(request):
    """
    Фикстура инициализирует WebDriver для каждого теста.
    Запускается в headless-режиме, если не указан флаг --headed.
    В случае падения теста делает скриншот и сохраняет его в папку /screenshots.
    """
    headed = request.config.getoption("--headed")

    # ChromeDriver будет найден, если добавлен в системный PATH
    service = Service()

    options = Options()
    if not headed:
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    options.add_argument("--window-size=1920,1080")
    options.add_argument("--log-level=3")

    driver = webdriver.Chrome(service=service, options=options)
    yield driver

    # Если тест упал — сохраняем скриншот
    if request.node.rep_call.failed:
        time_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"screenshots/FAIL_{request.node.name}_{time_str}.png"
        os.makedirs("screenshots", exist_ok=True)
        driver.save_screenshot(filename)
        print(f"\nСкриншот при ошибке сохранён: {filename}")

    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Хук pytest: сохраняет объект результата выполнения теста,
    чтобы можно было узнать статус изнутри фикстур (например, для скриншота).
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
