from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from login import Login
from action import Action

class Main:

  def main():
    login = Login()
    action = Action()
    options = Options()
    ## ヘッドレス設定
    options.add_argument("--headless=new")
    service = Service(executable_path="/usr/local/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://direct.smtb.jp/ap1/ib/login.do")
    login.smtbLoginFlow(driver)
    action.executeTransfer(driver)

    driver.quit()
    
  if __name__ == "__main__":
      main()
  
