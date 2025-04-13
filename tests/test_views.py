import pytest
from src.views import analyze_transactions
import pandas as pd




def test_analyze_transactions_invalid_date():
    with pytest.raises(ValueError):
        analyze_transactions("Invalid date")


def test_analyze_transactions_invalid_excel_file():
    with pytest.raises(FileNotFoundError):
        analyze_transactions(
            "2022-01-20",
            df=pd.read_excel(r"C:\Users\User\skypro_project1\data\.operations.xlsx"),
        )


def test_an():
    assert isinstance(analyze_transactions("2020-05-20"), str)
    assert 'top_transactions' in analyze_transactions("2020-05-20")


