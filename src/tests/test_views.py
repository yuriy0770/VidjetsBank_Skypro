import pytest
from src.views import analyze_transactions
import pandas as pd


def test_analyze_transactions():
    date_str = "2022-01-20"
    result = analyze_transactions(date_str)
    assert isinstance(result, dict)
    assert "cards" in result
    assert "top_transactions" in result

def test_analyze_transactions_cards():
    date_str = "2022-01-20"
    result = analyze_transactions(date_str)
    cards = result["cards"]
    for card in cards:
        assert "last_digits" in card
        assert "total_spent" in card
        assert "cashback" in card

def test_analyze_transactions_top_transactions():
    date_str = "2022-01-20"
    result = analyze_transactions(date_str)
    top_transactions = result["top_transactions"]
    for transaction in top_transactions:
        assert isinstance(transaction, dict)

def test_analyze_transactions_invalid_date():
    with pytest.raises(ValueError):
        analyze_transactions("Invalid date")



def test_analyze_transactions_invalid_excel_file():
    # Создаем не существующий файл excel для тестирования
    with pytest.raises(FileNotFoundError):
        analyze_transactions("2022-01-20", df=pd.read_excel(r"C:\Users\User\skypro_project1\data\.operations.xlsx"))