import os

import pandas as pd

from src.reports import spending_by_category
from src.services import simple_search
from src.utils import date_func
from src.views import analyze_transactions


def main():
    result_date = date_func()
    print(result_date["greeting"])
    while True:
        date = input("Здраствуйте введите дату ввиде YYYY-MM-DD ")
        if (
            date[:4].isdigit()
            and date[:4] in ["2018", "2019", "2020", "2021"]
            and date[5:7].isdigit()
            and date[-2:].isdigit()
        ):
            break
        else:
            print("Нужно ввести дату ввиде YYYY-MM-DD!!!!!!!!!!")

    print(analyze_transactions(date))
    word = input("Нужен поиск по определенному слову(да/нет) ")
    if word == "да":
        cat1 = input("Введите слово: ")
        print(simple_search(cat1))
    else:
        print("Как хотите")
    cat = input("Нужны данные по тратам по заданной категории (да/нет) ")
    if cat == "да":
        cat2 = input("Введите категорию: ")
        program_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
        absolute_json_file_path = os.path.join(program_dir, "operations.xlsx")
        transactions = pd.read_excel(absolute_json_file_path)
        result_json = spending_by_category(transactions, cat2)
        print(result_json)

    else:
        print("Как хотите")


if __name__ == "__main__":
    main()
