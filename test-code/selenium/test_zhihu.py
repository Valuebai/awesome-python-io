from selenium import webdriver  # 引入包

driver = webdriver.Chrome()  # 实例化浏览器
driver.get('https://www.zhihu.com/')  # 打开网页
# element = driver.find_element_by_name('fullname')  # 获取页面元素对象
# element.send_keys('woodman')  # 操作页面元素对象

zhihu_zhuce = "/html/body[@class='EntrySign-body']/div[@id='root']/div/main[@class='App-main']/div[@class='SignFlowHomepage']/div[@class='SignFlowHomepage-content']/div[@class='Card SignContainer-content']/div[@class='SignContainer-inner']/div[@class='Register']/div[@class='Register-content']/form/button[@class='Button Register-submitButton Button--primary Button--blue']"
element = driver.find_element_by_xpath(zhihu_zhuce)  # 获取页面元素对象
print("find you, zhuce", element)
driver.quit()  # 关闭浏览器
