import urllib.parse

# access
# ui
base_url = "https://altaivita.ru/"
# api
base_url_api = "https://altaivita.ru"

# variables
product_name = "Крем"
product_id = '2858'

data = {
    "product_id": 2858,
    "this_listId": "search_list",
    "LANG_key": "ru",
    "S_wh": 1,
    "S_CID": "3c9dad9cb4148b4f28956d0c4845e51f",
    "S_cur_code": "rub",
    "S_koef": 1,
    "quantity": 1,
    "S_hint_code": "",
    "S_customerID": ""
}

cookies = {
    "PHPSESSID": "giapbfcji5n6h28fc5n145qgl0",
    "CID": "3c9dad9cb4148b4f28956d0c4845e51f",
    "site_countryID": "247",
    "site_country_name": urllib.parse.quote("Россия"),  # URL-кодирование
    "_ga": "GA1.1.41664911.1732215498",
    "_ym_uid": "1732215498747649945",
    "_ym_d": "1732215498",
    "_ym_isad": "2",
    "_ym_visorc": "w",
    "_ga_2JB65Y3D22": "GS1.1.1732577665.11.1.1732578365.0.0.0",
}
