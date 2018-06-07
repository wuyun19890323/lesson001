class BaseAction:
    def __init__(self,driver):
        self.driver = driver

    # 连接网站
    def get_url(self, url):
        self.driver.get(url)

    # 最大化，隐性等待
    def maxi_wait(self, loc):
        self.driver.maximize_window()
        self.driver.implicitly_wait(loc)
