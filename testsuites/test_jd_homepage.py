# -*- coding:utf-8 -*-
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.jd_homepage import JdHomePage


class TestJdHomePage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        cls.driver.quit()

    def test_jd_search(self):
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        :return:
        """
        jd_homepage = JdHomePage(self.driver)
        jd_homepage.type_search('VR')
        jd_homepage.click_search_btn() 
        time.sleep(3)      
        jd_homepage.click_search_in_result_box() 
        jd_homepage.move_by_offset_and_click(-1000, 0)
        time.sleep(8)


if __name__ == '__main__':
    unittest.main()

