from selenium.webdriver.common.by import By
from base.base_driver import browser_fire
from page.page_load import PageLoad
import unittest


class TestLoad(unittest.TestCase):

    def get_text(self,loc):
        return self.scr_load.get_att(self.load_text)

    def get_ass(self):
        self.scr_load.get_scr(self.scr_load.load_get())

    # 网址
    url = "http://localhost/iwebshop/"
    # 定位登录链接
    load_mark = By.XPATH, "//a[@href='/iwebshop/index.php?controller=simple&action=login']"
    # 定位用户名
    username = By.XPATH, "//input[@type='text']"
    # 定位密码
    password = By.XPATH, "//input[@type='password']"
    # 定位登录按钮
    load_click = By.XPATH, "//input[@type='submit']"
    # 定位登录文本域
    load_text = By.XPATH, "//p[@class='loginfo']"
    # 定位退出按钮
    load_quit = By.XPATH, "//a[@class='reg']"

    def setUp(self):
        self.driver = browser_fire()
        self.scr_load = PageLoad(self.driver)
        self.scr_load.get_url(self.url)
        self.scr_load.maxi_wait(30)

    def test_load(self):
        # 点击登录链接
        self.scr_load.click_load(self.load_mark)
        # 输入用户名
        self.scr_load.input_text(self.username,"admin")
        # 输入密码
        self.scr_load.input_text(self.password,"123456")
        # 点击登录按钮
        self.scr_load.click_load(self.load_click)
        try:
            self.assertIn("admin1",self.get_text(self.load_text))
        except AssertionError:
            self.get_ass()
            raise

    def tearDown(self):
        self.scr_load.click_load(self.load_quit)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
