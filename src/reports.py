import json
import logging
from datetime import datetime, timedelta
from typing import Optional

import pandas as pd
import os

program_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
absolute_json_file_path = os.path.join(program_dir, "report.log")
logging.basicConfig(
    level=logging.DEBUG,
    filename=absolute_json_file_path,
    filemode="w",
    encoding="utf-8",
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
)

logger = logging.getLogger("spending_by_category")


def wrapper(f):
    """Декоратор записывает результат в текстовый файл"""

    def inner(*args):
        program_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "report")
        absolute_json_file_path = os.path.join(program_dir, "report.txt")
        with open(absolute_json_file_path, "w", encoding="utf-8") as file:
            file.write(str(f(*args)))

    return inner


def spending_by_category(transactions: pd.DataFrame, category: str, date: Optional[str] = None) -> str:
    """Траты по категории"""

    logger.info("Читаем файл Excel с транзакциями и сохраняем его в DataFrame.")
    df = transactions

    logger.info("Если дата не передана, то установливаем текущую дату.")
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")
    if category == "":
        raise KeyError
    logger.info(
        "Делаем фильтрацию данных по указанной категории и датам за последние три месяца."
    )
    filter_date = (datetime.strptime(date, "%Y-%m-%d") - timedelta(days=90)).strftime(
        "%Y-%m-%d"
    )
    df_filtered = df[
        (df["Дата операции"] >= filter_date) & (df["Категория"] == category)
    ]

    logger.info(
        "Группируем данные по дате операции и считаем сумму транзакций для каждой группы."
    )
    df_grouped = (
        df_filtered.groupby("Дата операции")["Сумма операции"].sum().reset_index()
    )

    logger.info("Преобразовываем результат в JSON-формат.")
    result_json = json.dumps(
        df_grouped.to_dict(orient="records"), ensure_ascii=False, indent=4
    )

    return result_json
