import logging
import os
from datetime import datetime
from pprint import pprint

import requests
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.DEBUG,
    filename=r"C:\Users\User\skypro_project1\logs\utils.log",
    filemode="w",
    encoding="utf-8",
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
)

logger = logging.getLogger("parser_stocs")
logger1 = logging.getLogger("parser_currency")
logger2 = logging.getLogger("analyze_transactions")
logger3 = logging.getLogger("date_func")

load_dotenv(".env")

API_KEY = os.getenv("API_KEY")
API_KEY2 = os.getenv("API_KEY2")


def parser_stocs():
    '''Парсит цены акций'''
    logger.info("Создаем список")
    json_file = []
    logger.info("Создаем словарь")
    dict_file = {}
    stocks = ["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"]
    logger.info("Проходимся в цикле по акциям")
    for i in stocks:
        api_url = f"https://api.api-ninjas.com/v1/stockprice?ticker={i}"
        response = requests.get(api_url, headers={"X-Api-Key": API_KEY})
        if response.status_code == requests.codes.ok:
            logger.info("Получаем стоимость каждой акции")
            json_file.append(response.json())
        else:
            logger.error(f"Ошибка: {response.status_code}")
            return f'"Error:", {response.status_code}, {response.text}'
    json_file1 = [{"stock": i["ticker"], "price": i["price"]} for i in json_file]
    dict_file["stock_prices"] = json_file1
    logger.info("Возвращаем словарь")
    logger.info("Завершение работы")
    return dict_file


def parser_currency():
    '''Парсит стоимость валюты'''
    currency = ["USD", "EUR"]
    logger1.info("Создаем список")
    json_file = []
    logger1.info("Создаем словарь")
    dict_file = {}
    logger1.info("Проходимся в цикле по названиям вылют")
    logger1.info("Получаем стоимость каждой валюты в рублях за 1 единицу")
    for i in currency:
        url = f"https://api.apilayer.com/currency_data/convert?to=RUB&from={i}&amount=1"
        response = requests.request("GET", url, headers={"apikey": API_KEY2})
        if response.status_code == requests.codes.ok:
            json_file.append(response.json())
        else:
            logger1.error(f"Ошибка: {response.status_code}")
            return f'"Error:", {response.status_code}, {response.text}'
    json_file1 = [
        {"currency": i["query"]["from"], "rate": i["result"]} for i in json_file
    ]
    dict_file["currency_rates"] = json_file1
    logger1.info("Возвращаем словарь")
    logger1.info("Завершение работы")
    return dict_file


def date_func():
    '''Возвращает приветствие в зависимости от часа дня'''
    logger3.info("Начало работы функции")
    dt_to = datetime.now()
    hour = dt_to.hour
    logger3.info("Создаем словарь куда будем записывать результат")
    dict_time = {}
    if hour in [23, 0, 1, 2, 3, 4]:
        logger3.info("Создаем словарь где значение 'Доброй ночи' и ключ 'greeting'")
        dict_time["greeting"] = "Доброй ночи"
    elif 5 <= hour < 11:
        logger3.info("Создаем словарь где значение 'Доброе утро' и ключ 'greeting'")
        dict_time["greeting"] = "Доброе утро"
    elif 11 <= hour < 17:
        logger3.info("Создаем словарь где значение 'Добрый день' и ключ 'greeting'")
        dict_time["greeting"] = "Добрый день"
    elif 17 <= hour < 23:
        logger3.info("Создаем словарь где значение 'Добрый вечер' и ключ 'greeting'")
        dict_time["greeting"] = "Добрый вечер"
    logger3.info("Возвращаем словарь")
    logger3.info("Завершение работы")
    return dict_time

