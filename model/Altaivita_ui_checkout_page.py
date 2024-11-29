from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


class Altaivita_ui_checkout_page:
    def __init__(self, test_config):
        self.test_config = test_config
        self._driver = None

    def set_driver(self, driver):
        self._driver = driver

    def go_to_checkout_page(self):
        """
        Запрос на переход на страницу оформления заказа.
        """
        curt = WebDriverWait(self._driver, 20).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR,
                 'a.header__basket-link.ga_link_to_cart.grid_container_mobile_menu.pdd_cart')
                )
        )
        curt.click()

        checkout = WebDriverWait(self._driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, '//a[text()="Оформить заказ"]')
                )
        )
        checkout.click()

    from selenium.common.exceptions import TimeoutException

    def click_pop_up_window(self):
        """
        Закрывает оповещение о скидке, если оно есть.
        """
        try:
            button = WebDriverWait(self._driver, 5).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "button.swal2-confirm")
                    )
            )
            button.click()
            print("Всплывающее окно закрыто.")
        except TimeoutException:
            print("Всплывающее окно отсутствует, шаг пропущен.")

    def add_more_product(self):
        """
        Запрос на увеличение количества товара перед оформлением.
        """
        add = WebDriverWait(self._driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'i.fal.fa-plus'))
        )
        add.click()

    def delete_product_in_cart(self):
        """
        Запрос на удаление товара из корзины перед оформлением.
        """
        delete = WebDriverWait(self._driver, 20).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'div.basket__delete.js-item-delete')
                )
        )
        delete.click()
