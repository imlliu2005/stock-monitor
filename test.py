import tushare as ts


def get_stock_price(code):
    data = ts.get_realtime_quotes(code)
    price = float(data['price'])
    return price


print(get_stock_price('002252'))
