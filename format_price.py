import argparse

ERROR_MESSAGE = 'Ошибка'


def format_price(price):
    price = price.replace(',', '.')
    try:
        price = float(price)
    except ValueError:
        return ERROR_MESSAGE
    if price.is_integer():
        return '{0:,.0f}'.format(price).replace(',', ' ')
    else:
        return '{0:,.2f}'.format(price).replace(',', ' ')


if __name__ == '__main__':
    argparser = argparse.ArgumentParser(description='Форматирование записи цены')
    argparser.add_argument('price', type=str, help='строка с ценой')
    args = argparser.parse_args()
    print(format_price(args.price))
