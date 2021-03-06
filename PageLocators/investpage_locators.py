# —— coding :utf-8 ——
# @time:    2020/10/7 20:59
# @IDE:     webTest_frmewok_v2.0
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    investpage_locators.py
from selenium.webdriver.common.by import By
# 投资输入框
money_input = (By.XPATH,'//input[contains(@class,"invest-unit-investinput")]')

#投标点击按钮
invest_button = (By.XPATH,'//div[@class="body"]//button')

# 投资成功弹窗的查看并激活按钮
active_button_on_success_pop = (By.XPATH,'//div[@class="layui-layer-content"]//button')

# 错误提示框
invest_failed_popup = (By.XPATH,'')

# 投标按钮上的错误信息
errorMsg_from_investButton = (By.XPATH,'//div[@class="layui-layer-content"]')

# 页面中间的错误提示信息
errorMsg_from_pageCenter = (By.XPATH,'//div/button[@class="btn btn-special height_style"]/text()')
