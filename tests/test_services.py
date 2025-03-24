import unittest
from unittest.mock import patch
import pandas as pd
from src.services import get_transfers


class TestGetTransfers(unittest.TestCase):
    @patch('pandas.read_excel')
    def test_get_transfers(self, mock_read_excel):
        data = {
            'Описание': ['Иван Иванов.', 'Петр Петров', 'Семен Семенович'],
            'Количество': [10, 20, 30]
        }
        df = pd.DataFrame(data)

        mock_read_excel.return_value = df

        file_path = '../data/operations.xlsx'
        result = get_transfers(file_path)

        self.assertIsInstance(result, list)

        for item in result:
            self.assertEqual(set(item.keys()), {'Описание', 'Количество'})

    @patch('pandas.read_excel')
    def test_get_transfers_empty(self, mock_read_excel):
        mock_read_excel.return_value = pd.DataFrame(columns=['Описание'])

        file_path = '../data/operations.xlsx'
        result = get_transfers(file_path)

        self.assertEqual(result, [])

    @patch('pandas.read_excel')
    def test_get_transfers_invalid_file(self, mock_read_excel):
        mock_read_excel.side_effect = pd.errors.EmptyDataError

        file_path = '../data/operations.xlsx'
        with self.assertRaises(pd.errors.EmptyDataError):
            get_transfers(file_path)




if __name__ == '__main__':
    unittest.main()