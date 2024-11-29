import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from model.Altaivita_ui_main_page import Altaivita_ui_main_page
from model.Altaivita_ui_checkout_page import Altaivita_ui_checkout_page
from model.Altaivita_api import Altaivita_api


@pytest.fixture(scope="session")
def test_config():
    """Фикстура для передачи конфигурации."""
    import config
    return config


@pytest.fixture(scope="function")
def setup_driver(test_config):
    """Фикстура для настройки WebDriver."""
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )
    driver.get(test_config.base_url)
    driver.implicitly_wait(4)
    driver.maximize_window()

    """ Инициализация объектов """
    main_page_ui = Altaivita_ui_main_page(test_config)
    main_page_ui.set_driver(driver)

    checkout_page_ui = Altaivita_ui_checkout_page(test_config)
    checkout_page_ui.set_driver(driver)

    """ Возвращаем объекты и driver """
    yield main_page_ui, checkout_page_ui, driver

    driver.quit()


@pytest.fixture(scope="function")
def auth_api(test_config):
    """Фикстура для настройки клиента API авторизации."""

    return Altaivita_api(test_config.base_url_api)
