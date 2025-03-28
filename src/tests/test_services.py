import pandas as pd
from unittest.mock import patch, MagicMock
import json
import logging.config

from src.services import get_transfers

logging_config = {
    "version": 1,
    "formatters": {
        "verbose": {"format": "%(asctime)s %(name)s %(levelname)s %(message)s"},
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {"level": "DEBUG", "handlers": ["console"]},
}

logging.config.dictConfig(logging_config)

def test_get_transfers_with_empty_file():
    file_path = 'empty.xlsx'
    with patch('pandas.read_excel') as mock_read_excel:
        mock_read_excel.return_value = pd.DataFrame(columns=['Описание'])
        result = get_transfers(file_path)
        assert result == []

def test_get_transfers_with_no_matches():
    file_path = 'no_matches.xlsx'
    data = {
        "Описание": ["Описание1", "Описание2", "Описание3"]
    }
    df = pd.DataFrame(data)
    with patch('pandas.read_excel') as mock_read_excel:
        mock_read_excel.return_value = df
        result = get_transfers(file_path)
        assert result == []


def test_get_transfers_logging():
    file_path = 'test.xlsx'
    with patch('pandas.read_excel') as mock_read_excel, patch.object(logging.getLogger("get_transfers"), 'info') as mock_info:
        mock_read_excel.return_value = pd.DataFrame({
            "Описание": ["Иванов.", "Петров."]
        })
        get_transfers(file_path)
        assert mock_info.call_count == 3

def test_get_transfers_json():
    file_path = 'test.xlsx'
    data = {
        "Описание": ["Иванов.", "Петров."]
    }
    df = pd.DataFrame(data)
    with patch('pandas.read_excel') as mock_read_excel:
        mock_read_excel.return_value = df
        result = get_transfers(file_path)
        assert isinstance(result, list)
        for item in result:
            assert isinstance(item, dict)