from selenium import webdriver
import threading
import time
driver = webdriver.Chrome("./chromedriver")
driver.get("https://cpstest.org/")
my_button = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[3]/div[1]/div[2]/div[1]/button")
my_button.click()
my_div = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[3]/div[1]/div[2]/div[1]")

def clicking():
        for _ in range(1000):
                my_div.click()
threads = []
for _ in range(1000):
        t = threading.Thread(target=clicking)
        t.daemon = True
        threads.append(t)
for i in range(1000):
        threads[i].start()
for i in range(1000):
        threads[i].join()

time.sleep(3)