from selenium import webdriver
from selenium.webdriver.common.by import By

class Parser:
    def __init__(self) -> None:
        self.browser = webdriver.Edge()
        self.browser.maximize_window()

    def __start__(self, url:str) ->None:
        self.browser.get(url=url)

    def __end__(self) -> None:
        self.browser.quit()

    def __back__(self) -> None:
        self.browser.back()

    def __cookies__ (self) -> None:
        self.browser.find_element(By.CLASS_NAME,"btn btn-пкун btn-gradient btn-sm").click()

    def __next__(self) -> None:
        self.browser.find_element(By.LINK_TEXT,"След.").click()

    def __perebor__(self, iteration) -> None:
        window = self.browser.find_element(By.CSS_SELECTOR,(f"body > section:nth-child(9) > div:nth-child(1) > div:nth-child(4) > div:nth-child(11) > div:nth-child(3) > div:nth-child(1) > div:nth-child({iteration}) > div:nth-child(1)"))
        window.find_element(By.CLASS_NAME,"lazyload").click()

    def __name_product__ (self):
        header = self.browser.find_element(By.CSS_SELECTOR,".h3")
        return header

    def __price_full__ (self):
        price_full = self.browser.find_element(By.CSS_SELECTOR,"div[class='_old'] span")
        return price_full

    def __price_sell__(self):
        price_sell = self.browser.find_element(By.CSS_SELECTOR,"._price")
        return price_sell

    def __product__(self,iteration):
        header = self.browser.find_element(By.CSS_SELECTOR,".h3")
        description_all = self.browser.find_element(By.CSS_SELECTOR,".col-sm-12.col-md-7")
        description_parameters = description_all.find_element(By.CSS_SELECTOR,"div[class='col-sm-12 col-md-6'] ul[class='attributes-list']")
        parameter = description_parameters.find_element(By.XPATH,(f"/html[1]/body[1]/section[3]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[{iteration}]"))
        return parameter