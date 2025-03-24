
import logging

import pandas as pd

logging.basicConfig(
    level=logging.DEBUG,
    filename="../logs/services.log",
    filemode="w",
    encoding="utf-8",
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
)

logger = logging.getLogger("get_transfers")


def get_transfers(file_path: str):
    '''Функция возвращает JSON со всеми транзакциями, которые относятся к переводам физлицам.'''
    logger.info("Читаем данные из файла Excel")
    df = pd.read_excel(file_path)

    logger.info('Ищем в столбце "Описание операции" имена физлиц с точкой')
    transfers_with_name = df[df["Описание"].str.contains(r"\b\w\.", case=False)]

    logger.info("Возвращаем результат в виде JSON-ответа")
    return transfers_with_name.to_dict(orient="records")
