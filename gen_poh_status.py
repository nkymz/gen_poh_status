# -*- coding: utf-8 -*-

import os
import time
import datetime

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
    # elm = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div[1]/ul[1]/li[3]/a[1]").click()
    elm = driver.find_element_by_xpath("//img[@alt='競走馬検索']/../..")
    print(elm.get_attribute("onclick"))
    elm.click()
    time.sleep(5)

if __name__ == "__main__":
    main()
