from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from parser_modul import Parser
from parser_book import BookExcel

def main() -> None:
    parser = Parser()
    book = BookExcel()
    parser.__start__(f"https://superakb.ru/catalogue/category/akkumuliatory-starternye_315/?filter=&amp;sort=&city=%D0%9A%D1%80%D0%B0%D1%81%D0%BD%D0%BE%D1%8F%D1%80%D1%81%D0%BA")
    time.sleep(10)
    book.__name_line__()
    iteration = 1
    iteration_too = 1
    iteration_line = 1
    
    try:
        while True:
            try:
                while True:
                    parser.__perebor__(iteration)
                    time.sleep(10)
                    header = parser.__name_product__()
                    price_full = parser.__price_full__()
                    price_sell = parser.__price_sell__()
                    book.__name_price__(header.text,price_full.text,price_sell.text,iteration_line)
                    print(header.text,price_full.text,price_sell.text)
                    try:
                        while True:
                            parameters = parser.__product__(iteration_too)
                            book.__with_book__(parameters.text,iteration_line,iteration_too)
                            book.__save_book__()
                            print(parameters.text)
                            iteration_too += 1
                    finally:
                        parser.__back__()
                        time.sleep(10)
                        iteration_too = 1
                        iteration+=1
                        iteration_line+=1
                        continue
            finally:
                parser.__next__()
                iteration = 1
                time.sleep(10)
                continue
            
    except Exception as ex:
        print(ex)
    finally:
        parser.__end__()



if __name__ == "__main__":
    main()