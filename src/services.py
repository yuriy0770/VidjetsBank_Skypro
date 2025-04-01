import os
import re
import logging

import pandas as pd

program_dir = os.path.join(os.path.dirname(__file__), "logs")
absolute_json_file_path = os.path.join(program_dir, "services.log")
logging.basicConfig(
    level=logging.DEBUG,
    filename=absolute_json_file_path,
    filemode="w",
    encoding="utf-8",
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
)

logger = logging.getLogger("get_transfers")


def get_transfers():
    """Функция возвращает JSON со всеми транзакциями, которые относятся к переводам физлицам."""
    logger.info("Читаем данные из файла Excel")
    program_dir = os.path.join(os.path.dirname(__file__), "data")
    file_path = os.path.join(program_dir, "operations.xlsx")
    df = pd.read_excel(file_path)

    logger.info("Ищем имена физлиц с точкой")
    names_pattern = r"\b\w\."
    transfers_with_name = df[df["Описание"].str.contains(names_pattern, case=False)]

    logger.info("Возвращаем результат в виде JSON-ответа")
    return transfers_with_name.to_dict(orient="records")
