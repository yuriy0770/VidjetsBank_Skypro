import os
from datetime import datetime


from src.utils import date_func, parser_stocs, parser_currency

from unittest.mock import Mock, patch
import requests
from dotenv import load_dotenv

load_dotenv(".env")

API_KEY = os.getenv("API_KEY")
API_KEY2 = os.getenv("API_KEY2")

def test_parser_stocks_error():
    # Имитация логирования
    logger = Mock()

    # Имитация HTTP-запроса с ошибкой
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 404

        result = parser_stocs()

        # Проверяем, что функция возвращает строку с ошибкой
        assert isinstance(result, str)
        assert 'Error:' in result


def test_parser_stocks_empty_response():
    # Имитация логирования
    logger = Mock()

    # Имитация HTTP-запроса без ответа
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 500

        result = parser_stocs()

        # Проверяем, что функция возвращает строку с ошибкой
        assert isinstance(result, str)


def get_AAPL(q):
    api_url = f"https://api.api-ninjas.com/v1/stockprice?ticker={q}"
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    return response.json()


@patch("requests.get")
def test_parser_stocs(stocs):
    stocs.return_value.json.return_value = {"ticker": "AAPL","name": "Apple Inc.","price": 192.42,"exchange": "NASDAQ",
    "updated": 1706302801,
    "currency": "USD"}
    assert get_AAPL('AAPL') ==  {"ticker": "AAPL","name": "Apple Inc.","price": 192.42,"exchange": "NASDAQ","updated": 1706302801,
    "currency": "USD"}


def test_parser_currency():
    # Имитация логирования
    logger1 = Mock()

    # Имитация HTTP-запроса
    with patch('requests.request') as mock_request:
        mock_request.return_value.status_code = 200
        mock_request.return_value.json.return_value = {
            "query": {"from": "USD"},
            "result": 1.23
        }

        result = parser_currency()

        # Проверяем, что функция возвращает словарь с курсами валют
        assert isinstance(result, dict)
        assert 'currency_rates' in result

        # Проверяем, что словарь содержит правильные данные
        currency_rates = result['currency_rates']
        assert len(currency_rates) == 2
        for currency_rate in currency_rates:
            assert 'currency' in currency_rate
            assert 'rate' in currency_rate


def test_parser_currency_error():
    # Имитация логирования
    logger1 = Mock()

    # Имитация HTTP-запроса с ошибкой
    with patch('requests.request') as mock_request:
        mock_request.return_value.status_code = 404

        result = parser_currency()

        # Проверяем, что функция возвращает строку с ошибкой
        assert isinstance(result, str)
        assert 'Error:' in result


def test_parser_currency_empty_response():
    # Имитация логирования
    logger1 = Mock()

    # Имитация HTTP-запроса без ответа
    with patch('requests.request') as mock_request:
        mock_request.return_value.status_code = 500

        result = parser_currency()

        # Проверяем, что функция возвращает строку с ошибкой
        assert isinstance(result, str)


def test_date_func():
    result = datetime.now()
    result_hour = result.hour
    if result_hour in [23, 0, 1, 2, 3, 4]:
        assert date_func() == {"greeting": "Доброй ночи"}
    elif 5 <= result_hour < 11:
        assert date_func() == {"greeting": "Доброе утро"}
    elif 11 <= result_hour < 17:
        assert date_func() == {"greeting": "Добрый день"}
    elif 17 <= result_hour < 23:
        assert date_func() == {"greeting": "Добрый вечер"}