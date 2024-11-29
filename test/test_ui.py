import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


@pytest.mark.ui
@allure.epic("Cart functionality")
@allure.feature("UI testing")
@allure.story("Search, add, and remove products in the cart on the main page.")
@allure.severity("blocker")
def test_srch_add_del_main_page(setup_driver, test_config):
    with allure.step("Открыть сайт"):
        main_page_ui, _, driver = setup_driver

    with allure.step(
        "Проверить, что результаты поиска содержат список товаров"
    ):
        main_page_ui.search_product(test_config.product_name)
        product_list = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, 'div[class="category__list"]')
                )
        )
        assert len(product_list) > 0, "No products found for the search term"

    with allure.step("Проверить, что товар добавлен в корзину"):
        main_page_ui.add_product()
        cart_count = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'span.count.js-count-number.active')
                )
        ).text
        assert cart_count == '1', f"Expected 1 item in the cart, but got {cart_count}"

    with allure.step("Проверить, что количество товара в корзине увеличилось"):
        main_page_ui.add_more_product_to_cart()
        driver.refresh()
        cart_count = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'span.count.active.js-count-number')
                )
        ).text
        assert cart_count == '2', f"Expected 2 items in the cart, but got {cart_count}"

    with allure.step("Проверить, что в корзине пусто"):
        main_page_ui.clean_cart()
        driver.refresh()
        cart_clean = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'span.basket-price.js-total')
                )
        ).text
        assert cart_clean == '0 ₽', f"Expected '0 ₽' in the cart, but got {cart_clean}"


@pytest.mark.ui
@allure.epic("Cart functionality")
@allure.feature("UI testing")
@allure.story("Addition and removal of products on the checkout page")
@allure.severity("blocker")
def test_add_del_checkout_page(setup_driver, test_config):
    with allure.step("Открыть сайт"):
        main_page_ui, checkout_page_ui, driver = setup_driver

    with allure.step(
        "Найти продукт на главной странице. Проверить результаты поиска."
    ):
        main_page_ui.search_product(test_config.product_name)
        product_list = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, 'div[class="category__list"]')
                )
        )
        assert len(product_list) > 0, "No products found for the search term"

    with allure.step(
        "Добавить продукт на главной странице и проверить кол-ва в корзине."
    ):
        main_page_ui.add_product()
        cart_count = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'span.count.js-count-number.active')
                )
        ).text
        assert cart_count == '1', f"Expected 1 item in the cart, but got {cart_count}"

    with allure.step("Перейти на страницу оформления заказа."):
        checkout_page_ui.go_to_checkout_page()
    with allure.step("Закрыть всплывающее окно об акции."):
        checkout_page_ui.click_pop_up_window()
    with allure.step(
        "Добавить количество товара на странице оформления заказа и кол-ва товара."
    ):
        checkout_page_ui.add_more_product()
        driver.refresh()
        count_product = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'span.num'))
        ).text
        assert count_product == '2', f"Expected 2 items in the cart, but got {count_product}"

    with allure.step(
        "Удалить товар на странице оформления заказа. Проверить удалился ли товар."
    ):
        checkout_page_ui.delete_product_in_cart()
        driver.refresh()
        cart = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'span.js-total_products_amount')
                )
        ).text
        assert cart == '0 ₽', f"Expected '0 ₽' in the cart, but got {cart}"
