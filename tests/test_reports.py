from unittest.mock import patch, MagicMock

from src.reports import spending_by_category, wrapper
import unittest


class TestSpendingByCategory(unittest.TestCase):
    def test_spending_by_category(self):
        file_path = 'test_operations.xlsx'
        category = ''
        date = None
        result = spending_by_category(file_path, category, date)
        self.assertIsNone(result)

    def test_spending_by_category_invalid_date(self):
        file_path = 'test_operations.xlsx'
        category = 'Покупки'  # неверное написание категории, чтобы проверить поведение функции при ошибке
        date = '2022-01-32'  # неверная дата, чтобы проверить поведение функции при ошибке
        result = spending_by_category(file_path, category, date)
        self.assertIsNone(result)


class TestWrapper(unittest.TestCase):
    @patch('builtins.open')
    def test_wrapper(self, mock_open):
        # Mock функцию, которую мы хотим декорировать
        mock_function = MagicMock(return_value="Mock result")

        # Декорируем функцию и вызываем ее
        with patch.object(type(mock_function), '__call__', return_value=None):
            decorated_function = wrapper(mock_function)
            decorated_function()

        # Проверяем, что файл был открыт для записи
        mock_open.assert_called_once_with(r"C:\Users\User\skypro_project1\report\report.txt", "w", encoding="utf-8")

        # Получаем значение, которое было записано в файл
        file_mock = mock_open.return_value.__enter__.return_value

        # Проверяем, что содержимое файла равно строке 'None'
        self.assertEqual(file_mock.write.call_args_list[0][0][0], str(None))



