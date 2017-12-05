# -*- coding:utf-8 -*-
from framework.base_page import BasePage


class JdHomePage(BasePage):
    search_box = "xpath=>//input[@accesskey='s']"
    search_btn = "xpath=>//button[@class='button']"
    search_in_result_box = "xpath=>//input[@value='在结果中搜索']"

    def type_search(self, text):
        self.type(self.search_box, text)

    def click_search_btn(self):
        self.click(self.search_btn)

    def click_search_in_result_box(self):
        self.click(self.search_in_result_box)