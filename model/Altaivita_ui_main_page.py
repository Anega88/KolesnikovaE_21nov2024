from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Altaivita_ui_main_page:
    def __init__(self, test_config):
        self.test_config = test_config
        self._driver = None

    def set_driver(self, driver):
        self._driver = driver

    def search_product(self, product_name: str):
        """
        Запрос поиска товара с главной страницы сайта.
        """
        search_input = WebDriverWait(self._driver, 20).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'input[placeholder="Поиск товаров"]')
                )
            )
        search_input.clear()
        search_input.send_keys(product_name)
        self.click_search_button()

    def click_search_button(self):
        """
        Запрос на нажатие кнопки Поиск на главной странице сайта.
        """
        try:
            search_button_svg = WebDriverWait(self._driver, 20).until(
                 EC.presence_of_element_located(
                     (By.CSS_SELECTOR, 'div.searchpro__field-button-container > div')
                     )
                     )
            search_button_svg.click()
        except Exception as e:
            print(f"Error clicking main SVG search button: {e}")

    def add_product(self):
        """
        Запрос на добавление товара в корзину.
        """
        driver = self._driver
        driver.execute_script("window.scrollBy(0, 80);")
        add_to_cart_button = WebDriverWait(self._driver, 30).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '.product__buy .product__add_2_0 button span')
            )
        )
        add_to_cart_button.click()

        WebDriverWait(self._driver, 30).until(
         EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'button.more.js-plus_2_0')
            )
        )

    def add_more_product_to_cart(self):
        """
        Запрос на увеличение количества товара в корзине.
        """
        driver = self._driver
        driver.execute_script("window.scrollBy(0, 30);")
        plus_button = self._driver.find_element(
            By.CSS_SELECTOR, 'button.more.js-plus_2_0'
        )
        plus_button.click()

    def clean_cart(self):
        """
        Запрос на удаление товара из корзины.
        """
        driver = self._driver
        driver.execute_script("window.scrollBy(0, 30);")
        curt = self._driver.find_element(
            By.CSS_SELECTOR, 'i.fal.fa-shopping-bag'
        )
        curt.click()
        curt = self._driver.find_element(
            By.CSS_SELECTOR, 'button.dropdown-close.js-item-delete'
        )
        curt.click()
