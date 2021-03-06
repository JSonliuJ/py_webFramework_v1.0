# —— coding :utf-8 ——
# @time:    2020/10/7 21:01
# @IDE:     webTest_frmewok_v2.0
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    conftest.py
from selenium import webdriver
from TestDatas import Common_datas as CD
from PageObjects.login_page import LoginPage
import pytest

driver = None


# 声明是一个fixture
@pytest.fixture(scope="class")
def access_web():
    global driver
    # 前置操作
    print("所有用例执行之前，setup整个测试类执行一次")
    driver = webdriver.Chrome()
    driver.get(CD.web_login_url)
    lg = LoginPage(driver)
    yield (driver, lg)  # 分割线：返回值
    # 后置操作
    print("所有用例执行完成，tearDown整个测试类执行一次")
    driver.quit()


@pytest.fixture
def refresh_page():
    global driver
    driver = webdriver.Chrome()
    # 前置操作
    yield
    # 后置操作
    driver.refresh()
