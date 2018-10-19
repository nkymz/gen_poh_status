# -*- coding: utf-8 -*-

import os
import time
import datetime
import re

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import openpyxl


POGPATH = os.getenv("HOMEDRIVE", "None") + os.getenv("HOMEPATH", "None") + "/Dropbox/POG/"
WBPATH = (POGPATH + "POG_HorseList.xlsx").replace("\\", "/")
HTMLPATH = (POGPATH + "next_race_list.html").replace("\\", "/")
WEBDRIVERPATH = r"C:\Selenium\chromedriver.exe"

JRA_DF_URL = "http://www.jra.go.jp/datafile/"

mytoday = datetime.date.today()


HDB_URL = "http://www.jra.go.jp/JRADB/accessR.html"
DICT_POST_HDB = {"cname": "pw02uliD19999"}
DICT_SEARCH_FORM = {
    "iv_h_name": "ビーチサンバ",
    "iv_method": "0",
    "iv_belong": "0",
    "iv_sex": "0",
    "iv_hmaskbn": "1"
}


def main():
    options = Options()
    # options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path=WEBDRIVERPATH, options=options)

    time.sleep(1)
    driver.get(JRA_DF_URL)
    time.sleep(1)
    driver.find_element_by_xpath("//img[@alt='競走馬検索']/../..").click()
    time.sleep(1)
    driver.find_element_by_xpath("//td[contains(text(), '競走馬名')]/following-sibling::td[1]/input").send_keys("ビーチサンバ")
    driver.find_element_by_xpath("//td[contains(text(), '競走馬名')]/following-sibling::td[1]/a").click()
    time.sleep(1)
    driver.find_element_by_xpath("//a[contains(text(), 'ビーチサンバ')]").click()
    time.sleep(1)
    if driver.find_elements_by_xpath("//td[contains(text(), '放牧')]"):
        print("放牧")
    else:
        print("放牧じゃない")
    # print(driver.find_elements_by_xpath("//a[contains(text(), 'ビーチサンバ')]/..")[1].text)
    # print(driver.find_elements_by_xpath("//a[contains(text(), '*ビーチサンバ')]/..")[1].text)
    # for i in driver.find_elements_by_xpath("//a/.."):
    #    print(i.text)


    time.sleep(5)

if __name__ == "__main__":
    main()

# 中央未登録、中央登録、剤級、放牧、中央抹消、地方、海外

