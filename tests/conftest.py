import pandas as pd
import pytest

from src.services import simple_search

@pytest.fixture
def data():
    return simple_search('Супермаркеты')

@pytest.fixture
def data1():
    return simple_search(4354554)

@pytest.fixture
def df():
    data = {
        'Дата операции': ['31.12.2021 16:44:00', '31.12.2021 16:42:04', '31.12.2021 16:39:04'],
        'Номер карты': ['*7197', '*7197', '*7197'],
        'Сумма операции': ['-160,89', '-64,00', '-118,12'],
        'Описание': ['Супермаркеты Колхоз 3,00', 'Супермаркеты Колхоз 1,00', 'Супермаркеты Магнит 2,00']
    }
    return pd.DataFrame(data)


@pytest.fixture
def df_without_match():
    data = {
        'Дата операции': ['31.12.2021 16:44:00', '31.12.2021 16:42:04'],
        'Номер карты': ['*7197', '*7197'],
        'Сумма операции': ['-160,89', '-64,00'],
        'Описание': ['Колхоз 3,00', 'Магнит 2,00']
    }
    return pd.DataFrame(data)


@pytest.fixture
def analyze_transactions():
    return {
    "cards": [
        {
            "last_digits": "7197",
            "total_spent": 135.0,
            "cashback": 1.35
        },
        {
            "last_digits": "7197",
            "total_spent": 114.6,
            "cashback": 1.15
        },
        {
            "last_digits": "7197",
            "total_spent": 52.9,
            "cashback": 0.53
        }
    ],
    "top_transactions": [
        {
            "date": "23.05.2020",
            "amount": 135.0,
            "category": "Супермаркеты",
            "description": "Колхоз"
        },
        {
            "date": "23.05.2020",
            "amount": 114.6,
            "category": "Супермаркеты",
            "description": "Магнит"
        },
        {
            "date": "23.05.2020",
            "amount": 52.9,
            "category": "Супермаркеты",
            "description": "Магнит"
        }
    ],
    "greeting": "Добрый вечер",
    "stock_prices": [
        {
            "stock": "AAPL",
            "price": 198.53
        },
        {
            "stock": "AMZN",
            "price": 184.145
        },
        {
            "stock": "GOOGL",
            "price": 157.16
        },
        {
            "stock": "MSFT",
            "price": 388.39
        },
        {
            "stock": "TSLA",
            "price": 248.65
        }
    ],
    "currency_rates": [
        {
            "currency": "USD",
            "rate": 84.405467
        },
        {
            "currency": "EUR",
            "rate": 95.500739
        }
    ]
}