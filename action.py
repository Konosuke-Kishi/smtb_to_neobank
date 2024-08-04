from selenium import webdriver
from selenium.webdriver.common.by import By
from config import CONFIG
import time
import sys

class Action:
  
    MONEY = CONFIG['amountOfMoney']

    def executeTransfer(self, driver: webdriver):
        # 支店選択
        args = sys.argv
        if args[1] == "t":
            for i in range(0, 25):
                driver.find_element(by=By.CSS_SELECTOR, value="td:nth-child(3) > form > a > img").click()
                time.sleep(0.5)
                driver.find_element(by=By.CSS_SELECTOR, value=".mcp-btn-hutuuu-hurikomi > input").click()
                time.sleep(0.5)
                driver.find_element(by=By.CSS_SELECTOR, value="#hurikomisaki_jizen tr:nth-child(4) input").click()
                time.sleep(0.5)
                driver.find_element(by=By.NAME, value="kingakuDisp").send_keys(self.MONEY)
                driver.find_element(by=By.CSS_SELECTOR, value="td:nth-child(3) > .button-choco > input").click()
                time.sleep(0.5)
                myScript = ''
                with open("script.js") as f:
                    myScript = f.read()
                driver.execute_script(myScript)
                driver.find_element(by=By.CSS_SELECTOR, value="td:nth-child(3) > .button-choco > input").click()
                time.sleep(0.5)
                driver.find_element(by=By.CSS_SELECTOR, value="td:nth-child(3) > .button-choco > input").click()
                time.sleep(0.5)
        else:
            for i in range(0, 25):
                driver.find_element(by=By.CSS_SELECTOR, value="td:nth-child(3) > form > a > img").click()
                time.sleep(0.5)
                driver.find_element(by=By.CSS_SELECTOR, value=".mcp-btn-hutuuu-hurikomi > input").click()
                time.sleep(0.5)
                driver.find_element(by=By.CSS_SELECTOR, value="#hurikomisaki_jizen tr:nth-child(3) input").click()
                time.sleep(0.5)
                driver.find_element(by=By.NAME, value="kingakuDisp").send_keys(self.MONEY)
                driver.find_element(by=By.CSS_SELECTOR, value="td:nth-child(3) > .button-choco > input").click()
                time.sleep(0.5)
                myScript = ''
                with open("script.js") as f:
                    myScript = f.read()
                driver.execute_script(myScript)
                driver.find_element(by=By.CSS_SELECTOR, value="td:nth-child(3) > .button-choco > input").click()
                time.sleep(0.5)
                driver.find_element(by=By.CSS_SELECTOR, value="td:nth-child(3) > .button-choco > input").click()
                time.sleep(0.5)
