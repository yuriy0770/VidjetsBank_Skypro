
from pprint import pprint

from src.utils import date_func, parser_currency, parser_stocs
from src.views import analyze_transactions




def main():
    date = input('Здраствуйте введите дату ввиде YYYY-MM-DD HH:MM:SS ')
    result_date = date_func()
    print(result_date["greeting"])

    print(parser_stocs())
    print(parser_currency())
    print(analyze_transactions(date))



if __name__ == "__main__":
    main()