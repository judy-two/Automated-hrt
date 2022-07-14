# coding=utf-8
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from page.searchPage import SearchPage
import time
import unittest
from page.searchPage import *
from selenium.webdriver.common.by import By


class TestEnterprise(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = SearchPage.enterprise_url
        self.driver.maximize_window()
        self.page = SearchPage(self.driver)
        self.page.get(self.url)

    def tearDown(self):
        self.driver.close()

    def test_Login(self):
        self.page.user=self.page.search_username
        self.page.password=self.page.search_password
        self.page.search_btn.click()
        time.sleep(5)
        if self.page.pop:
            self.page.pop_ac.click()
        else:
            time.sleep(2)
        ##弹窗确认
        # self.alert=self.driver.switch_to.alert
        # time.sleep(2)
        # if self.alert:
        #     print(self.alert.text)
        #     self.alert.accept()
        # else:
        #     time.sleep(2)
        time.sleep(2)
        self.assertIn(self.page.search_content_assert_phone, self.driver.page_source)
        print("登录OK")

        self.page.username.click()
        time.sleep(2)
        self.assertIn(self.page.search_content_assert_title1, self.driver.page_source)
        self.assertIn(self.page.search_content_assert_title2, self.driver.page_source)
        self.assertIn(self.page.search_content_assert_title3, self.driver.page_source)
        print("基本资料OK")


        self.page.aut.click()
        time.sleep(2)
        self.assertIn(self.page.search_content_assert_aut,self.driver.page_source)
        print("实名认证OK")

        self.page.ser.click()
        time.sleep(2)
        self.page.qin.click()
        time.sleep(2)
        self.assertIn(self.page.search_content_assert_but,self.driver.page_source)
        print("我的青创贷OK")

        self.page.ren1.click()
        time.sleep(2)
        self.page.ren2.click()
        time.sleep(2)
        self.assertIn(self.page.search_content_assert_sut2,self.driver.page_source)
        print("企业入驻OK")

        self.page.ren3.click()
        time.sleep(2)
        self.assertIn(self.page.search_content_assert_sut3,self.driver.page_source)
        print("企业信息异议OK")

        self.page.meg.click()
        time.sleep(2)
        self.assertIn(self.page.search_content_assert_meg,self.driver.page_source)
        print("我的消息OK")



if __name__ == '__main__':
    # 使用以下语句生成本页面的测试报告
    # now = time.strftime("%Y-%m-%d-%H-%M-%S")
    # suite = unittest.TestSuite()
    # suite.addTest(TestEnterprise("test_Login"))
    # # suite.addTest(TestLogin("test_search1"))
    # # suite.addTest(TestLogin("test_search2"))
    # path = "../report/" + now + "result.html"
    # fp = open(path, 'wb')
    # runner = HTMLTestRunner(stream=fp, title="Web页面自动化测试", description="测试查询功能")
    # runner.run(suite)
    # fp.close()
    unittest.main()

