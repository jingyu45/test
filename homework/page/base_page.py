class BasePage:
    def __init__(self,driver: WebDriver =None):
        if driver is None:
            self._driver = webdriver.Chrome()
            self._driver.implicitly_wait(2)
            self._driver.get("https://work.weixin.qq.com/")
        else:
            self._driver = driver
    def close(self):
        sleep(20)
        self._driver.quit()