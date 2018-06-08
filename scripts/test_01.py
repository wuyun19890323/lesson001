from selenium.webdriver.common.by import By
from base.base_driver import browser_fire
from page.page_load import PageLoad
import unittest


class TestLoad(unittest.TestCase):

    # def get_text(self,loc):
    #     return self.scr_load.get_att(self.load_text)

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
    # 定位登录后文本域
    load_text = By.XPATH, "//p[@class='loginfo']"
    # 定位退出按钮
    load_quit = By.XPATH, "//a[@class='reg']"
    # 定位登录前账户或错误提示
    load_wrong = By.XPATH, "//div[@class ='prompt']"
    # 定位登录前账户为空是提示填写用户名或邮箱
    load_username_null = By.XPATH, "//tbody/tr[1]/td/label[@class='invalid-msg']"
    # 定位登录前密码为空是提示填写密码
    load_password_null = By.XPATH, "//tbody/tr[2]/td/label[@class='invalid-msg']"

    def setUp(self):
        self.driver = browser_fire()
        self.scr_load = PageLoad(self.driver)
        self.scr_load.get_url(self.url)
        self.scr_load.maxi_wait(30)

    # 正确账户正确密码
    def test_load001(self):
        # 点击登录链接
        self.scr_load.click_load(self.load_mark)
        # 输入用户名
        self.scr_load.input_text(self.username, "admin")
        # 输入密码
        self.scr_load.input_text(self.password, "123456")
        # 点击登录按钮
        self.scr_load.click_load(self.load_click)
        try:
            self.assertIn("admin", self.scr_load.get_att(self.load_text))
        except AssertionError:
            self.get_ass()
            raise
        self.scr_load.click_load(self.load_quit)

    def tearDown(self):
        self.driver.quit()

    # 正确账户错误密码
    def test_load002(self):
        # 点击登录链接
        self.scr_load.click_load(self.load_mark)
        # 输入用户名
        self.scr_load.input_text(self.username, "admin")
        # 输入密码
        self.scr_load.input_text(self.password, "1234567")
        # 点击登录按钮
        self.scr_load.click_load(self.load_click)
        try:
            self.assertIn("用户名和密码不匹配", self.scr_load.get_att(self.load_wrong))
        except AssertionError:
            self.get_ass()
            raise

    # 正确账户密码为空
    def test_load003(self):
        # 点击登录链接
        self.scr_load.click_load(self.load_mark)
        # 输入用户名
        self.scr_load.input_text(self.username, "admin")
        # 输入密码
        self.scr_load.input_text(self.password, "")
        # 点击登录按钮
        self.scr_load.click_load(self.load_click)
        try:
            self.assertIn("填写密码", self.scr_load.get_att(self.load_password_null))
        except AssertionError:
            self.get_ass()
            raise

    # 错误账户正确密码
    def test_load004(self):
        # 点击登录链接
        self.scr_load.click_load(self.load_mark)
        # 输入用户名
        self.scr_load.input_text(self.username, "admin1")
        # 输入密码
        self.scr_load.input_text(self.password, "123456")
        # 点击登录按钮
        self.scr_load.click_load(self.load_click)
        try:
            self.assertIn("用户名和密码不匹配", self.scr_load.get_att(self.load_wrong))
        except AssertionError:
            self.get_ass()
            raise

    # 错误账户错误密码
    def test_load005(self):
        # 点击登录链接
        self.scr_load.click_load(self.load_mark)
        # 输入用户名
        self.scr_load.input_text(self.username, "admin1")
        # 输入密码
        self.scr_load.input_text(self.password, "1234567")
        # 点击登录按钮
        self.scr_load.click_load(self.load_click)
        try:
            self.assertIn("用户名和密码不匹配", self.scr_load.get_att(self.load_wrong))
        except AssertionError:
            self.get_ass()
            raise

    # 错误账户密码为空
    def test_load006(self):
        # 点击登录链接
        self.scr_load.click_load(self.load_mark)
        # 输入用户名
        self.scr_load.input_text(self.username, "admin1")
        # 输入密码
        self.scr_load.input_text(self.password, "")
        # 点击登录按钮
        self.scr_load.click_load(self.load_click)
        try:
            self.assertIn("填写密码", self.scr_load.get_att(self.load_password_null))
        except AssertionError:
            self.get_ass()
            raise

    # 空账户正确密码
    def test_load007(self):
        # 点击登录链接
        self.scr_load.click_load(self.load_mark)
        # 输入用户名
        self.scr_load.input_text(self.username, "")
        # 输入密码
        self.scr_load.input_text(self.password, "123456")
        # 点击登录按钮
        self.scr_load.click_load(self.load_click)
        try:
            self.assertIn("填写用户名或邮箱", self.scr_load.get_att(self.load_username_null))
        except AssertionError:
            self.get_ass()
            raise

    # 空账户错误密码
    def test_load008(self):
        # 点击登录链接
        self.scr_load.click_load(self.load_mark)
        # 输入用户名
        self.scr_load.input_text(self.username, "")
        # 输入密码
        self.scr_load.input_text(self.password, "1234567")
        # 点击登录按钮
        self.scr_load.click_load(self.load_click)
        try:
            self.assertIn("填写用户名或邮箱", self.scr_load.get_att(self.load_username_null))
        except AssertionError:
            self.get_ass()
            raise

    # 空账户空密码
    def test_load009(self):
        # 点击登录链接
        self.scr_load.click_load(self.load_mark)
        # 输入用户名
        self.scr_load.input_text(self.username, "")
        # 输入密码
        self.scr_load.input_text(self.password, "")
        # 点击登录按钮
        self.scr_load.click_load(self.load_click)
        try:
            self.assertIn("填写用户名或邮箱", self.scr_load.get_att(self.load_username_null))
        except AssertionError:
            self.get_ass()
            raise


if __name__ == '__main__':
    unittest.main()
