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

from ppropkg.pproxls import POHorseList
from ppropkg.pprows import JRAHorseSearch

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
    jra_horse_search = JRAHorseSearch()
    poh_list = POHorseList()
    poh_status_list = []
    poh_name_list = poh_list.get_name_list()
    for poh in poh_name_list:
        horse_name, xlrow = poh[0], poh[1]
        if len(horse_name) >= 6 and horse_name[-5] == "の":
            continue
        print(horse_name + jra_horse_search.get_status(horse_name))


def main2():
    options = Options()
    # options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path=WEBDRIVERPATH, options=options)
    print(type(driver))

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
    driver.find_element_by_xpath("//a[@href='javascript:history.back()']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//td[contains(text(), '競走馬名')]/following-sibling::td[1]/input").clear()
    driver.find_element_by_xpath("//td[contains(text(), '競走馬名')]/following-sibling::td[1]/input").send_keys("サターン")
    driver.find_element_by_xpath("//td[contains(text(), '競走馬名')]/following-sibling::td[1]/a").click()
    time.sleep(1)
    driver.find_element_by_xpath("//a[contains(text(), 'サターン')]").click()
    if driver.find_elements_by_xpath("//td[contains(text(), '放牧')]"):
        print("放牧")
    else:
        print("放牧じゃない")

    # print(driver.find_elements_by_xpath("//a[contains(text(), 'ビーチサンバ')]/..")[1].text)
    # print(driver.find_elements_by_xpath("//a[contains(text(), '*ビーチサンバ')]/..")[1].text)
    # for i in driver.find_elements_by_xpath("//a/.."):
    #    print(i.text)
    # / html / body / table / tbody / tr / td / table[6] / tbody / tr / td / table[1] / tbody / tr[1] / td[3] / span / a
    # javascript: history.back()
    time.sleep(5)


if __name__ == "__main__":
    main()

# 中央未登録、中央登録、剤級、放牧、中央抹消、地方、海外

