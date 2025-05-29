import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import os

def pytest_addoption(parser):
    # Если пользователь передал --headed, то отключаем headless
    parser.addoption("--headed", action="store_true", help="Открыть браузер с GUI (отключить headless)")

@pytest.fixture
def driver(request):
    headed = request.config.getoption("--headed")

    chrome_driver_path = r"E:\Program Files\chromedriver-win64\chromedriver.exe"
    service = Service(executable_path=chrome_driver_path)

    options = Options()

    if not headed:
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")

    options.add_argument("--window-size=1920,1080")
    options.add_argument("--log-level=3")

    driver = webdriver.Chrome(service=service, options=options)
    yield driver

    if request.node.rep_call.failed:
        time_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"screenshots/FAIL_{request.node.name}_{time_str}.png"
        os.makedirs("screenshots", exist_ok=True)
        driver.save_screenshot(filename)
        print(f"\n📸 Скриншот при ошибке сохранён: {filename}")

    driver.quit()

# Хук для фиксации результатов и передачи в фикстуру
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
