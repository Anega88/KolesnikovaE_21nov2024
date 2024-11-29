import pytest
import config
import allure


@pytest.mark.api
@allure.epic("Cart functionality")
@allure.feature("API testing")
@allure.story("Search, add, and remove products in the cart.")
@allure.severity("blocker")
def test_search_add_product_to_cart(auth_api):
    with allure.step("Отправить запрос на поиск товара"):
        search_response = auth_api.search_product(
            config.product_name, config.cookies
            )
        with allure.step("Проверить, что ответ не пустой"):
            assert search_response is not None, "Ответ на запрос поиска продукта пустой"
        with allure.step("Проверить, что в ответе есть ключ request"):
            assert "request" in search_response, "Список продуктов не найден в ответе"
            request = search_response["request"]
        with allure.step("Проверить, что в списке есть хотя бы один продукт"):
            if "request" in search_response:
                request = search_response["request"]
                assert len(request) > 0, "Список продуктов пустой"

    with allure.step("Отправить запрос на добавление товара в корзину"):
        add_response = auth_api.add_product_to_cart(
            config.data, config.cookies
            )
        with allure.step("Проверить ответ на добавление товара в корзину"):
            assert add_response is not None, "Ответ на запрос добавления товара в корзину пустой"
        with allure.step(
            "Используем 'new_quantity' для проверки успешного добавления товара в корзину"
        ):
            assert 'new_quantity' in add_response, "Поле 'new_quantity' отсутствует в ответе"
            assert add_response[
                'new_quantity'
                ] > 0, f"Количество товаров в корзине должно быть больше 0, но оказалось {add_response[
                    'new_quantity']}"

    with allure.step("Отправить запрос на удаление товара из корзины"):
        auth_api.delete_product_from_cart(config.product_id, config.cookies)


@pytest.mark.api
@allure.epic("Cart functionality")
@allure.feature("API testing")
@allure.story("Add and remove products in the cart.")
@allure.severity("blocker")
def test_more_product_and_delete(auth_api):
    with allure.step("Отправить запрос на поиск товара"):
        auth_api.search_product(config.product_name, config.cookies)

    with allure.step("Отправить запрос на добавление товара в корзину"):
        add_product_response = auth_api.add_product_to_cart(
            config.data, config.cookies
            )
        with allure.step("Проверить, что ответ на добавление товара не пустой"):
            assert add_product_response is not None, "Ответ на добавление товара пустой"

    with allure.step("Отправить запрос на добавление больше товара в корзину"):
        add_more_response = auth_api.add_more_product(
            config.product_id, config.cookies
            )
        with allure.step("Проверить, что запрос на добавление товара прошел успешно"):
            assert add_more_response.status_code == 200, "Ошибка при добавлении количества товара."
        with allure.step("Проверить, что в ответе есть нужный текст в new_quantity"):
            response_json = add_more_response.json()
            assert response_json.get(
                'id'
                ) == config.product_id, f"Ожидалось значение {config.product_id}, но получено {
                    response_json.get('id')}"

    with allure.step("Отправить запрос на удаление товара из корзины"):
        delete_response = auth_api.delete_product_from_cart(
            config.product_id, config.cookies
            )
        with allure.step("Проверить, что что delete_response не None"):
            assert delete_response is not None, "Ответ на удаление товара пустой"
        with allure.step("Проверить статус ответа"):
            response_json = delete_response.json()
            assert response_json.get(
                'status'
                ) == 'ok', f"Ожидался статус 'ok', но получен {
                    response_json.get('status')}"
        with allure.step("Проверить, что был удален один товар"):
            assert response_json.get(
                'quantity_to_delete'
                ) == '1', f"Ожидалась удаленная единица товара '1', но получено {
                    response_json.get('quantity_to_delete')}"
        with allure.step("Проверить сумму товаров в корзине после удаления"):
            assert response_json.get(
                'sum_quantity'
                ) == '0', f"Ожидалась сумма количества товаров в корзине '0', но получена {
                    response_json.get('sum_quantity')}"
