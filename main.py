

from src.utils import date_func, parser_currency, parser_stocs
from src.views import analyze_transactions




def main():
    date = input('Здраствуйте введите дату ввиде YYYY-MM-DD HH:MM:SS ')
    result_date = date_func()
    print(result_date["greeting"])
    dict_f = {}
    dict_f.update(parser_currency())
    dict_f.update(parser_stocs())
    dict_f.update(analyze_transactions(date))
    dict_f.update(date_func())

    print(dict_f)



if __name__ == "__main__":
    main()