import datetime

import unittest
import pandas as pd

from src.views import analyze_transactions, date_func


class TestDateFunc(unittest.TestCase):
    def test_date_func(self):
        date = datetime.datetime.now()
        result = date_func()
        if 5 <= date.hour < 11:
            self.assertEqual(result["greeting"], 'Доброе утро')
        elif 11 <= date.hour < 17:
            self.assertEqual(result["greeting"], 'Добрый день')
        elif 17 <= date.hour < 23:
            self.assertEqual(result["greeting"], 'Добрый вечер')
        else:
            self.assertEqual(result["greeting"], 'Доброй ночи')


class TestAnalyzeTransactions(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            "Номер карты": [1234, 5678],
            "Дата операции": ["2022-01-01", "2022-01-02"],
            "Сумма операции с округлением": [100.0, 200.0]
        })


    def test_analyze_transactions_empty_df(self):
        df = pd.DataFrame(columns=["Номер карты", "Дата операции", "Сумма операции с округлением"])
        result = analyze_transactions("2022-01-01")
        self.assertEqual(result['cards'], [])
        self.assertEqual(result['top_transactions'], [])

if __name__ == '__main__':
    unittest.main()