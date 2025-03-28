import json
import logging

from pprint import pprint
from typing import Dict, List, Any

import pandas as pd

from src.utils import date_func, parser_currency, parser_stocs

logging.basicConfig(
    level=logging.DEBUG,
    filename=r"C:\Users\User\skypro_project1\logs\views.log",
    filemode="w",
    encoding="utf-8",
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
)

logger = logging.getLogger("analyze_transactions")


def analyze_transactions(date_str: str) -> list[dict[str, list[dict[str, str | Any]] | Any] | Any]:
    """Выводит данные по переданной дате"""
    logger.info("Читаем данные из файла operations.xlsx в DataFrame")
    df = pd.read_excel(r"C:\Users\User\skypro_project1\data\operations.xlsx")

    df["Дата операции"] = df["Дата операции"].apply(
        lambda x: pd.to_datetime(x, dayfirst=True)
    )
    logger.info("Преобразуем дату в формат YYYY-MM-DD HH:MM:SS")
    date = pd.to_datetime(date_str)
    logger.info("Выбираем строки с датой операций после указанной даты")
    start_date = date.replace(hour=0, minute=0, second=0)
    end_date = start_date + pd.DateOffset(days=1) - pd.DateOffset(seconds=1)
    df_filtered = df.loc[
        (df["Дата операции"] >= start_date) & (df["Дата операции"] < end_date)
        ]
    top_transactions = df_filtered.nlargest(5, "Сумма операции с округлением")
    top_transactions_dict = top_transactions.to_dict(orient="records")
    logger.info("Создаем список словарей из данных в DataFrame")
    result_list = []
    dict_tr = {}
    for index, row in df_filtered.iterrows():
        last_digits = str(row["Номер карты"])[-4:]
        total_spent = round(row["Сумма операции с округлением"], 2)
        cashback = round(total_spent * 0.01, 2)  # Кешбэк на 1% от общей суммы
        result_list.append(
            {
                "last_digits": last_digits,
                "total_spent": total_spent,
                "cashback": cashback,
            }
        )
    dict_tr["cards"] = result_list
    dict_tr["top_transactions"] = top_transactions_dict

    logger.info("Возвращаем словарь")
    logger.info("Завершение работы")

    return dict_tr


