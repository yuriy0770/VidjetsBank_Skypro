import json
import logging
from datetime import datetime, timedelta
from typing import Optional

import pandas as pd

logging.basicConfig(
    level=logging.DEBUG,
    filename=r"C:\Users\User\skypro_project1\logs/reports.log",
    filemode="w",
    encoding="utf-8",
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
)

logger = logging.getLogger("spending_by_category")


def wrapper(f):
    def inner(*args):
        with open(r"C:\Users\User\skypro_project1\report\report.txt", "w", encoding="utf-8") as file:
            file.write(str(f(*args)))

    return inner



def spending_by_category(transactions: pd.DataFrame, category: str, date: Optional[str] = None) -> str:
    '''Траты по категории'''
    try:
        logger.info(f"Используются данные из файла operations.xlsx строк.")

        if date is None:
            current_date = datetime.today()
        else:
            current_date = datetime.strptime(date, "%Y-%m-%d").date()

        start_date = current_date - timedelta(days=90)

        filtered_transactions = transactions[
            (transactions["Категория"] == category)
            & (transactions["Дата операции"].dt.date >= start_date)
            & (transactions["Дата операцией"].dt.date <= current_date)
        ]

        total_spending = filtered_transactions['Сумма платежа'].sum()

        result_json = {
            "category": category,
            "total_spending": total_spending
        }

        logger.info(f"Возвращаем результат: {result_json}")

        return json.dumps(result_json)

    except Exception as e:
        print(f"Ошибка: {e}")
        return None




logger1 = logging.getLogger("spending_by_weekday")

def spending_by_weekday(transactions: pd.DataFrame, date: Optional[str] = None) -> dict:
    '''Траты по дням недели'''
    try:
        logger1.info(f"Используются данные из файла operations.xlsx строк.")

        if date is None:
            current_date = datetime.today()
        else:
            current_date = datetime.strptime(date, "%Y-%m-%d").date()

        start_date = current_date - timedelta(days=90)

        filtered_transactions = transactions[
            (transactions["Дата операции"].dt.date >= start_date)
            & (transactions["Дата операцией"].dt.date <= current_date)
        ]

        # Разделим транзакции по дням недели
        weekday_spending = filtered_transactions.groupby(filtered_transactions['Дата операций'].dt.dayofweek)['Сумма платежа'].sum().reset_index()

        # Добавим названия дней недели
        weekday_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        weekday_spending['День недели'] = weekday_names[weekday_spending['Дата операций'].dt.dayofweek]

        # Создадим json-объект с данными по средним тратам
        result_json = [
            {
                "День недели": day,
                "Средняя сумма платежа": spending / 3 if i == len(weekday_spending) - 1 else spending
            }
            for i, (day, spending) in enumerate(zip(weekday_spending['День недели'], weekday_spending['Сумма платежа']))
        ]

        logger1.info(f"Возвращаем результат: {result_json}")

        return json.dumps(result_json)

    except Exception as e:
        print(f"Ошибка: {e}")
        return None