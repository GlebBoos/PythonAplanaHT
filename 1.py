#Задание по курсу
#1.Открыть страницу http://google.com/ncr
#2.Выполнить поиск слова “selenide”
#3.Проверить, что первый результат – ссылка на сайт selenide.org.
#4.Перейти в раздел поиска изображений
#5.Проверить, что первое изображение неким образом связано с сайтом selenide.org.
#6.Вернуться в раздел поиска Все
#7.Проверить, что первый результат такой же, как и на шаге 3.

#designed by Boos Gleb


import unittest

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Search(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        # 1.Открыть страницу http://google.com/ncr
        self.driver.get("http://google.com/ncr")
    def test_search(self):
        self.driver.maximize_window()
        assert "Google" in self.driver.title
        elem = self.driver.find_element_by_name("q")
        elem.clear()

        # 2.Выполнить поиск слова “selenide”
        elem.send_keys("selenide")
        elem.send_keys(Keys.RETURN)

        # 3.Проверить, что первый результат – ссылка на сайт selenide.org.
        elem = self.driver.find_element_by_xpath("//*[@id='rso']/div[1]/div/div[1]/div/div/div[1]/div/div[1]/cite")
        if "selenide.org" in elem.text:
            print("Первая ссылка соответствует поисковому запросу")
        f1=self.driver.find_element_by_xpath("//*[@id='rso']/div[1]/div/div[1]/div/div/h3/a")
        t=f1.text;

        # 4.Перейти в раздел поиска изображений
        elem=self.driver.find_element_by_xpath("//*[@id='hdtb-msb-vis']/div[2]/a")
        elem.click();

        # 5.Проверить, что первое изображение неким образом связано с сайтом selenide.org.
        elem=self.driver.find_element_by_xpath("//*[@id='6E5nxbsENroDNM:']")
        elem.click();
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//*[text() = "selenide.org"]')))
        except TimeoutException:
            raise Exception('Unable to find text in this element after waiting 5 seconds')

        # 6.Вернуться в раздел поиска Все
        elem = self.driver.find_element_by_xpath("//*[@id='hdtb-msb-vis']/div[1]/a")
        elem.click();

        # 7.Проверить, что первый результат такой же, как и на шаге 3.
        elem = self.driver.find_element_by_xpath("//*[@id='rso']/div[1]/div/div[1]/div/div/div[1]/div/div[1]/cite")
        f2 = self.driver.find_element_by_xpath("//*[@id='rso']/div[1]/div/div[1]/div/div/h3/a")
        if ("selenide.org" in elem.text) and (t in f2.text):
            print("Ссылки после переключения вкладок одинаковые")

        assert "No results found." not in self.driver.page_source
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()

