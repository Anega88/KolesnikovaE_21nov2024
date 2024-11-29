import requests
import config


class Altaivita_api:
    def __init__(self, base_url_api: str):
        self.base_url = base_url_api

    def search_product(self, data: dict, cookies: dict):
        """
        Выполняет запрос Поиск товара.

        :param data: Данные для отправки в запросе.
        :param cookies: Куки для авторизации и контекста.
        :return: Ответ в виде JSON или текстовый ответ, если JSON недоступен.
        """
        url = f"{self.base_url}/engine/ajax/ajax_ecommerce/ajax_ecommerce.php"
        headers = {
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9,ru;q=0.8",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "https://altaivita.ru",
            "Referer": "https://altaivita.ru/search/?query=%D0%BA%D1%80%D0%B5%D0%BC",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"'
        }

        response = requests.post(
            url, headers=headers, data=data, cookies=cookies
        )
        try:
            return response.json()
        except ValueError:
            return response.text

    def add_product_to_cart(self, data: dict, cookies: dict):
        """
        Выполняет запрос Добавление продукта в корзину.

        :param data: Данные для отправки в запросе (product_id, quantity и т.д.).
        :param cookies: Куки для авторизации и контекста.
        :return: Ответ в виде JSON или текстовый ответ, если JSON недоступен.
        """
        url = f"{self.base_url}/engine/cart/add_products_to_cart_from_preview.php"
        headers = {
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9,ru;q=0.8",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "https://altaivita.ru",
            "Referer": "https://altaivita.ru/search/?query=%D0%BC%D0%B0%D0%B7%D1%8C",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin"
        }

        response = requests.post(
            url, headers=headers, data=data, cookies=cookies
            )
        try:
            return response.json()
        except ValueError:
            return response.text

    def add_more_product(
            self, product_id: str, cookies: dict
            ):
        """
        Выполняет запрос Добавление больше продукта в корзину.

        :param data: Данные для отправки в запросе (product_id, quantity и т.д.).
        :param cookies: Куки для авторизации и контекста.
        :return: Ответ в виде JSON.
        """
        url = f"{self.base_url}/engine/ajax/ajax_ecommerce/ajax_ecommerce.php"

        headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': '; '.join([f'{key}={value}' for key, value in cookies.items()]),
            'Origin': 'https://altaivita.ru',
            'Referer': 'https://altaivita.ru/search/?query=%D0%BA%D1%80%D0%B5%D0%BC',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        data = {
            'action': 'ecom_link_products_cart',
            'productID': config.product_id,
            'LANG_key': 'ru',
            'S_wh': '1',
            'S_CID': '3c9dad9cb4148b4f28956d0c4845e51f',
            'S_cur_code': 'rub',
            'S_koef': '1',
            'S_hint_code': '',
            'S_customerID': '',
        }

        response = requests.post(
            url, headers=headers, data=data, cookies=cookies
            )
        return response

    def delete_product_from_cart(self, product_id: str, cookies: dict):
        """
        Выполняет запрос Удалить товар из корзины.

        :param data: Данные для отправки в запросе (product_id, quantity и т.д.).
        :param cookies: Куки для авторизации и контекста.
        :return: Ответ в виде JSON.
        """
        url = f"{self.base_url}/engine/cart/delete_products_from_cart_preview.php"

        headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': '; '.join([f'{key}={value}' for key, value in cookies.items()]),
            'Origin': 'https://altaivita.ru',
            'Referer': 'https://altaivita.ru/search/?query=%D0%BA%D1%80%D0%B5%D0%BC',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        data = {
            'product_id': product_id,
            'LANG_key': 'ru',
            'S_wh': '1',
            'S_CID': cookies.get('CID', ''),
            'S_cur_code': 'rub',
            'S_koef': '1',
            'S_hint_code': '',
            'S_customerID': '',
        }

        try:
            response = requests.post(
                url, headers=headers, data=data
            )

            if response.status_code == 200:
                print(f"Запрос прошел успешно. Статус: {response.status_code}")
                return response
            else:
                print(
                    f"Ошибка запроса. Статус: {response.status_code}, Тело ответа: {response.text}"
                )
                return None
        except requests.RequestException as e:
            print(f"Ошибка при отправке запроса: {e}")
            return None
