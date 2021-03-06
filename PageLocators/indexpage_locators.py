# —— coding :utf-8 ——
# @time:    2020/10/7 20:59
# @IDE:     webTest_frmewok_v2.0
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    indexpage_locators.py
from selenium.webdriver.common.by import By
# 用户名
user_link = (By.XPATH,'//a[@href="/Member/index.html"]')
# 投标按钮
bid_button = (By.XPATH,'//*[text()="抢投标"]')    #//a[@class="btn btn-special"]