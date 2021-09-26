import time
import util

# 股票代码或者名称列表
codes = ['002252', '002603', '000725']


def monitor():
    # 获取当天日期
    today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    # 判断是否是交易日
    trade_day = util.is_trade_day(today)
    trade_time = util.is_trade_time()
    if trade_day and trade_time:
        sales = []
        for code in codes:
            price = float(util.get_stock_price(code))
            # 上海莱士
            if code == '002252':
                if price >= 7.50:
                    msg = code + ' 上海莱士 ' + str(price) + '\n'
                    sales.append(msg)
            # 以岭药业
            if code == '002603':
                if price >= 20.50:
                    msg = code + ' 以岭药业 ' + str(price) + '\n'
                    sales.append(msg)
            # 京东方A
            if code == '000725':
                if price >= 6.60:
                    msg = code + ' 京东方A ' + str(price) + '\n'
                    sales.append(msg)
        if len(sales) > 0:
            msg = ''
            for ele in sales:
                msg += ele
            util.send_mail(msg)


def run():
    while True:
        monitor()
        # 延时60s
        time.sleep(10)


run()
