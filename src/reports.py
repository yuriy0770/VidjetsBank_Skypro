from datetime import datetime, timedelta
from typing import Optional

import pandas as pd


def wrapper(f):
    def inner(*args):
        with open(
            r"C:\Users\User\skypro_project1\report\report.txt", "w", encoding="utf-8"
        ) as file:
            file.write(str(f(*args)))

    return inner


@wrapper
def spending_by_category(file_path: str, category: str, date: Optional[str] = None) -> pd.DataFrame:
    '''Функция возвращает траты по заданной категории за последние три месяца (от переданной даты).'''
    try:
        df = pd.read_excel(file_path)
        if date is None:
            current_date = datetime.today()
        else:
            current_date = pd.to_datetime(date).date()
        start_date = current_date - timedelta(days=90)
        filtered_transactions = df[
            (df["Категория"] == category)
            & (df["Дата операции"] >= start_date.strftime("%Y-%m-%d"))
            & (df["Дата операции"] <= current_date.strftime("%Y-%m-%d"))
        ]

        grouped_transactions = (
            filtered_transactions.groupby(["Дата операции", "Сумма платежа"])
            .sum()
            .reset_index()
        )

        total_spending = grouped_transactions["Сумма платежа"].sum()

        return pd.DataFrame(
            {"Категория": [category], "Общая сумма трат": [total_spending]}
        )

    except Exception as e:
        print(f"Ошибка: {e}")
        return None


file_path = "../data/operations.xlsx"
category = "Покупки"
date = None

result = spending_by_category(file_path, category, date)
print(result)
