from urllib import request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import io
import os
import requests
from PIL import Image

class Parser:
    def __init__(self) -> None:
        self.browser = webdriver.Edge()
        self.browser.maximize_window()

    def __start_parsing__ (self, url:str) -> None:
        max_size = 2
        self.browser.get(url=url)
        time.sleep(2)
        try:
            os.mkdir ("картинки")
        finally:
            stroks = []
            with open ("проверка шк.txt",'r',encoding='utf-8') as file:
                print("чтение файла: 'проверка шк.txt'")
                while True:
                    strok = file.readline().replace("\n", "")
                    if strok == "":
                        break
                    stroks.append(strok)
            for line in stroks:
                try:
                    self.__parsing__(line,max_size)
                except:
                    continue
            print("Скрипт выполнен, хорошего вам дня/вечера/ночи")
            self.browser.quit()

    def __parsing__ (self, line:str,max_size:int) -> None:
        print(f"поиск: {line}")
        self.browser.get("https://www.google.ru/")
        self.browser.find_element(By.CSS_SELECTOR, "input[title='Поиск']").send_keys(line)
        self.browser.find_element(By.CSS_SELECTOR, "input[title='Поиск']").send_keys(Keys.ENTER)
        time.sleep(3)
        self.browser.find_element(By.LINK_TEXT,"Картинки").click()
        time.sleep(3)
        img_urls = set()
        img_class_name = self.browser.find_elements(By.CLASS_NAME,"Q4LuWd")

        for img_name in img_class_name[len(img_urls):max_size]:
            try:
                img_name.click()
                time.sleep(3)
            except:
                continue
            imgs = self.browser.find_elements(By.CLASS_NAME,"KAlRDb")
            for img in imgs:

                    if img.get_attribute('src') in img_urls:
                        break

                    if img.get_attribute('src') and 'http'  in img.get_attribute('src'):
                        img_urls.add(img.get_attribute('src'))
                        print (f"Найдено картинок: {len(img_urls)}")

            urls = img_urls

            for i, url in enumerate (urls):
                try:
                    print(f"попытка сохранения картинки: {line} номер: {i+1} в формате JPEG")
                    image_content = requests.get(url).content
                    image_file = io.BytesIO(image_content)
                    image = Image.open(image_file)

                    with open(f"картинки/{line}_{i+1}.jpg", "wb") as f:
                        image.save(f, "JPEG")
                        print(f"картинка: {line} номер: {i+1} в формате JPEG сохранена")

                except Exception as ex:
                    print(f"ОШИБКА сохранения в формате JPEG::{ex}")
                    print(f"удаление неудачной записи")
                    os.remove(f"картинки/{line}_{i+1}.jpg")
                    print(f"попытка сохранения картинки: {line} номер: {i+1} в формате PNG")
                    image_content = requests.get(url).content
                    image_file = io.BytesIO(image_content)
                    image = Image.open(image_file)

                    with open(f"картинки/{line}_{i+1}.png", "wb") as f:
                        image.save(f, "PNG")
                        print(f"картинка: {line} номер: {i+1} в формате PNG сохранена")