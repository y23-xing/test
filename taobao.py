import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 参考：https://blog.csdn.net/u010454030/article/details/134317195

# 创建WebDriver对象，指定使用Chrome浏览器驱动
wd = webdriver.Chrome()
# 最大等待时长
wd.implicitly_wait(5)

# 1、打开淘宝网站
wd.get("https://www.taobao.com")
# time.sleep(5)
# time.sleep(3)

# 2、登陆
# 2.1、点击登录按钮
wd.find_element(By.XPATH, '//*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[1]').click()
# time.sleep(5)
# 2.2 输入账号密码
user_element = wd.find_element(By.ID, 'fm-login-id')
user_element.send_keys('15257745139')
pwd_element = wd.find_element(By.ID, 'fm-login-password')
pwd_element.send_keys('q.050292131102')
# time.sleep(5)
# 2.3 滑块
# 这个暂时无法实现（手动）
# 2.4 点击登录按钮
wd.find_element(By.CLASS_NAME, 'password-login').click()
# time.sleep(20)

# 3、输入搜索词条
wd.find_element(By.ID, 'q').send_keys('行李箱')
# time.sleep(20)

# 4、点击搜索
wd.find_element(By.XPATH, '//*[@id="J_TSearchForm"]/div[1]/button').click()
time.sleep(5)

# 5、选择“销量”
wd.find_element(By.XPATH, '//*[@id="sortBarWrap"]/div[1]/div[1]/div/div[1]/div/div/div/ul/li[2]/div').click()
time.sleep(20)

# 6、点击第一个商品
wd.find_element(By.XPATH, '//*[@id="pageContent"]/div[1]/div[3]/div[3]/div/div[1]/a/div/div[1]/div[1]').click()
time.sleep(20)
# //*[@id="pageContent"]/div[1]/div[3]/div[3]/div/div[1]

# 7、加入购物车
wd.find_element(By.XPATH, '//*[@id="purchasePanel"]/div[2]/div/div[1]/button[2]').click()
time.sleep(20)

# 8、收藏
wd.find_element(By.XPATH, '//*[@id="purchasePanel"]/div[2]/div/div[2]/div').click()
time.sleep(20)

# 9、返回首页
wd.find_element(By.XPATH, '//*[@id="sn-bd"]/div/p[1]/a').click()
time.sleep(20)

time.sleep(100)

# 10、退出浏览器
wd.quit()

# 3、点击第一个商品
# wd.find_element(By.XPATH, '//*[@id="ice-container"]/div[4]/div/div/div[2]/div[1]/a').click()

# 4、点击进入店铺
# wd.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div[1]/div/a[2]').click()
# wd.find_element(By.CLASS_NAME, 'ShopHeader--leftWrap--1zlcizm').click()

# 点击搜索框搜索
# wd.find_element(By.ID, 'q').send_keys('行李箱')
# 点击搜索
# wd.find_element(By.XPATH, '//*[@id="J_Search"]/form/button[1]').click()


