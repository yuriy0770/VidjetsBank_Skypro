import os
import logging

import pandas as pd
import json

program_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
absolute_json_file_path = os.path.join(program_dir, "services.log")
logging.basicConfig(
    level=logging.DEBUG,
    filename=absolute_json_file_path,
    filemode="w",
    encoding="utf-8",
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
)

logger = logging.getLogger("simple_search")


def simple_search(query):
    program_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
    absolute_json_file_path = os.path.join(program_dir, "operations.xlsx")
    logger.info("Читаем данные из excel файла")
    df = pd.read_excel(absolute_json_file_path)
    results = []
    logger.info(
        "Проверяем, содержит ли строка для поиска (query) в описании или категории транзакции."
    )
    try:
        for index, row in df.iterrows():
            if (
                query.lower() in str(row["Описание"]).lower()
                or query.lower() in str(row["Категория"]).lower()
            ):
                result = {
                    "Дата операции": row["Дата операции"],
                    "Номер карты": row["Номер карты"],
                    "Сумма операции": row["Сумма операции"],
                    "Описание": row["Описание"],
                }
                results.append(result)
    except AttributeError as e:
        return f"Не правильно передан параметр"
    logger.info("Возвращаем JSON ответ")
    return json.dumps(results, ensure_ascii=False, indent=4)
