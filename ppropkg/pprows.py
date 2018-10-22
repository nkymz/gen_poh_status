# -*- coding: utf-8 -*-

import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import pprint

NEXT_RACE_INFO_URL = "http://pog-info.com/archives/category/pog/news"
NEXT_RACE_ARTICLE_URL = "http://pog-info.com/archives/{}"
WEBDRIVERPATH = r"C:\Selenium\chromedriver.exe"
JRA_DF_URL = "http://www.jra.go.jp/datafile/"


class JRAHorseSearch:

    def __init__(self):
        options = Options()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(executable_path=WEBDRIVERPATH, options=options)
        time.sleep(1)
        self.driver.get(JRA_DF_URL)
        time.sleep(1)
        self.driver.find_element_by_xpath("//img[@alt='競走馬検索']/../..").click()

    def get_status(self, horse_name):
        time.sleep(1)
        self.driver.find_element_by_xpath("//td[contains(text(), '競走馬名')]/following-sibling::td[1]/input").clear()
        self.driver.find_element_by_xpath("//td[contains(text(), '競走馬名')]/following-sibling::td[1]/input")\
            .send_keys(horse_name)
        self.driver.find_element_by_id("iv_hmaskbn1").click()
        self.driver.find_element_by_xpath("//td[contains(text(), '競走馬名')]/following-sibling::td[1]/a").click()
        time.sleep(1)
        try:
            self.driver.find_element_by_xpath("//a[contains(text(), '" + horse_name + "')]").click()
        except NoSuchElementException:
            return "未登録"
        if self.driver.find_elements_by_xpath("//td[contains(text(), '放牧')]"):
            self.driver.find_element_by_xpath("//a[@href='javascript:history.back()']").click()
            return "放牧"
        else:
            self.driver.find_element_by_xpath("//a[@href='javascript:history.back()']").click()
            return "非放牧"

    def quit(self):
        self.driver.quit()


class Soup:

    def __init__(self, target_url, parser, seconds):
        self.target_url = target_url
        self.parser = parser
        self.seconds = seconds

    def get(self):
        time.sleep(self.seconds)
        r = requests.get(self.target_url)
        if r.status_code == requests.codes.ok:
            return BeautifulSoup(r.content, self.parser)
        else:
            return None


def get_next_race_info_id():
    soup = Soup(NEXT_RACE_INFO_URL, "lxml", 1)
    html = soup.get()
    return html.find("article").get("id").split("-")[1]


def get_next_race_info(article_id):
    soup = Soup(NEXT_RACE_ARTICLE_URL.format(article_id), "lxml", 1)
    next_race_content = soup.get().find("div", class_="single-entry-content")
    return next_race_content


def main():
    pass


if __name__ == "__main__":
    main()
