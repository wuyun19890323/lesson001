import sys
import time
from base.base_action import BaseAction


class PageLoad(BaseAction):

    def find_element(self,loc):
        return self.driver.find_element(loc[0],loc[1])

    def click_load(self,loc):
        self.find_element(loc).click()

    def input_text(self,loc,text):
        self.find_element(loc).send_keys(text)

    def get_att(self,loc):
        return self.find_element(loc).text

    def get_scr(self,loc):
        self.driver.get_screenshot_as_file(loc)

    def load_get(self):
        loading_start = "../Image/"
        now_time = time.strftime("%Y_%m_%d %H_%M_%S")
        loading_end = "--" + str(sys.exc_info()[1]) + ".jpg"
        loading_file = loading_start + now_time + loading_end
        return loading_file


