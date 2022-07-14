# coding=utf-8
from common.pageObject import PageObject, PageElement
from common.url import *

class SearchPage(PageObject):
    # 当前测试页面的测试网址url
    base_url = Url.base_url
    url = base_url+'/'
    enterprise_url= base_url+"/login?userType=1"
    gov_url= base_url+"/login?userType=2"
    bank_url= base_url+"/login?userType=3"

    # 查询元素
    #登录手机号框
    user=PageElement(xpath="//*[@id=\"app\"]/div/div/div/div/form/div[1]/div/div/div/div/input")
    #登录密码框
    password=PageElement(xpath="//*[@id=\"app\"]/div/div/div/div/form/div[2]/div/div/div/div/input")
    #登录按钮
    search_btn=PageElement(xpath="//*[@id=\"app\"]/div/div/div/div/form/div[3]/div/div/button")
    #其他人登录提示框
    pop=PageElement(xpath="/html/body/div[2]/div[2]")
    #其他人登录提示框确认
    pop_ac=PageElement(xpath="/html/body/div[2]/div[2]/div[3]/div/button[2]/span")
    #个人中心
    username=PageElement(class_name="username")
    #实名认证
    aut=PageElement(xpath="//*[@id=\"app\"]/div/section/section/aside/div/div[2]/div/ul/div/li[2]/span")
    #我的金融服务
    ser=PageElement(xpath="//*[@id=\"app\"]/div/section/section/aside/div/div[2]/div/ul/div/li[4]/div/span")
    ser2=PageElement(xpath="//*[@id=\"app\"]/div/section/section/aside/div/div[2]/div/ul/div/li[4]")
    #我的青创贷
    qin=PageElement(xpath="//*[@id=\"app\"]/div/section/section/aside/div/div[2]/div/ul/div/li[4]/ul/li/span")
    #人工审核
    ren1=PageElement(xpath="//*[@id=\"app\"]/div/section/section/aside/div/div[2]/div/ul/div/li[5]/div/span")
    #企业入驻
    ren2=PageElement(xpath="//*[@id=\"app\"]/div/section/section/aside/div/div[2]/div/ul/div/li[5]/ul/li[1]/span")
    #企业信息异议
    ren3=PageElement(xpath="//*[@id=\"app\"]/div/section/section/aside/div/div[2]/div/ul/div/li[5]/ul/li[2]/span")
    #我的消息
    meg=PageElement(xpath="//*[@id=\"app\"]/div/section/section/aside/div/div[2]/div/ul/div/li[6]/span")




    # 查询内容
    #企业手机号
    search_username = "15926353676"
    #企业密码
    search_password="Aa123456"



    # 断言
    search_content_assert_phone = "15926353676"
    search_content_assert_title1= "登录信息"
    search_content_assert_title2= "账号信息"
    search_content_assert_title3= "企业信息"
    search_content_assert_aut="实名认证"
    search_content_assert_but= "青创贷专区"
    search_content_assert_sut2= "企业入驻列表"
    search_content_assert_sut3= "异议列表"
    search_content_assert_meg= "业务通知"



