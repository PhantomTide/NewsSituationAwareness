# -*- coding:utf-8 -*-

"""
eastmoney_guba_spider 东方财富股吧
"""

import time
from selenium import webdriver


def main():
    """
    main()
    :return:
    """
    print()
    driver = webdriver.Chrome("D:\soft\chromedriver\chromedriver_win32\chromedriver.exe")
    driver.get("http://guba.eastmoney.com/")
    # 登录账号
    # 沪市个股
    url = "http://guba.eastmoney.com/remenba.aspx?type=1&tab=1"
    # 深市个股
    url = "http://guba.eastmoney.com/remenba.aspx?type=1&tab=2"

    time.sleep(5)


if __name__ == '__main__':
    main()