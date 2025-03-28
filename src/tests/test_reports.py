import pytest
import pandas as pd
from datetime import datetime, timedelta
import json

from src.reports import spending_by_category, spending_by_weekday


data = {
    "Категория": ["Продукты", "Продукты", "Транспорт", "Транспорт", "Продукты"],
    "Дата операций": [
        datetime(2022, 1, 1),
        datetime(2022, 1, 15),
        datetime(2022, 1, 20),
        datetime(2022, 1, 25),
        datetime(2022, 2, 1)
    ],
    "Сумма платежа": [100.0, 200.0, 300.0, 400.0, 500.0]
}


df = pd.DataFrame(data)



def test_spending_by_category():
    result = spending_by_category(df, 'Транспорт')
    expected_result = 'null'
    assert json.dumps(result) == expected_result

def test_spending_by_category_with_date():
    date = datetime(2022, 1, 20).strftime("%Y-%m-%d")
    result = spending_by_category(df, date)
    expected_result = 'null'
    assert json.dumps(result) == expected_result

def test_spending_by_weekday():
    result = spending_by_weekday(df)
    expected_result = 'null'
    assert json.dumps(result) == expected_result

def test_spending_by_weekday_with_date():
    date = datetime(2022, 1, 20).strftime("%Y-%m-%d")
    result = spending_by_weekday(df, date)
    expected_result = 'null'
    assert json.dumps(result) == expected_result

