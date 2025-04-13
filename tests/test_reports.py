from src.reports import logger
import os
import pytest
import pandas as pd
from datetime import datetime, timedelta
import json
from src.reports import spending_by_category, wrapper


def test_wrapper_empty_arg():
    @wrapper
    def example_function(arg):
        return f"Результат: {arg}"

    example_function("")

    program_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "report")
    absolute_json_file_path = os.path.join(program_dir, "report.txt")
    with open(absolute_json_file_path, "r", encoding="utf-8") as file:
        content = file.read()
        assert content == "Результат: "


def test_wrapper_report_file_not_writable():
    @wrapper
    def example_function(arg):
        return f"Результат: {arg}"

    example_function("тест")
    program_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "report")
    absolute_json_file_path = os.path.join(program_dir, "report.txt")
    with open(absolute_json_file_path, "r", encoding='utf-8') as f:
        q = f.read()
        assert 'Результат: тест' == q

program_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
absolute_json_file_path = os.path.join(program_dir, "operations.xlsx")

def test_spending_by_category_no_date():
    transactions = pd.read_excel(absolute_json_file_path)
    result_json = spending_by_category(transactions, 'Супермаркеты')
    assert isinstance(result_json, str)

def test_spending_by_category_with_date():
    date = datetime.now().strftime("%Y-%m-%d")
    transactions = pd.read_excel(absolute_json_file_path)
    result_json = spending_by_category(transactions, 'Супермаркеты', date)
    assert isinstance(result_json, str)

def test_spending_by_category_empty_category():
    transactions = pd.read_excel(absolute_json_file_path)
    with pytest.raises(KeyError):
        spending_by_category(transactions, '')


def test_spending_by_category_invalid_date_format():
    transactions = pd.read_excel(absolute_json_file_path)
    with pytest.raises(ValueError):
        spending_by_category(transactions, 'Супермаркеты', 'invalid-date')

def test_spending_by_category_invalid_transactions_type():
    transactions = 'not-a-dataframe'
    with pytest.raises(TypeError):
        spending_by_category(transactions, 'Супермаркеты')
