# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

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
    mysession = requests.Session()
    r = mysession.post("http://www.jra.go.jp/JRADB/accessR.html", data=DICT_POST_HDB)
    r = mysession.post("http://www.jra.go.jp/JRADB/accessR.html", data=DICT_SEARCH_FORM)
    soup = BeautifulSoup(r.content, "lxml")
    print(soup.prettify)


if __name__ == "__main__":
    main()
