from selenium import webdriver
from selenium.webdriver.common.by import By
from config import CONFIG

class Login:

    SMTB_LOGIN_ID = CONFIG['userId']
    SMTB_PASSWORD = CONFIG['password']

    def smtbLoginFlow(self, driver: webdriver):
        #ユーザ名入力
        userid = driver.find_element(by=By.NAME, value="kaiinNo")
        userid.send_keys(self.SMTB_LOGIN_ID)
        #パスワード入力
        password = driver.find_element(by=By.NAME, value="ibpassword")
        password.send_keys(self.SMTB_PASSWORD)
        driver.find_element(by=By.CSS_SELECTOR, value="td:nth-child(3) > .button-choco > input").click()
    