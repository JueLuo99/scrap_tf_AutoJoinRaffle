from selenium import webdriver
import json
import time


# driver = webdriver.Chrome()
opt = webdriver.ChromeOptions()
opt.set_headless()
opt.add_argument('--no-sandbox')
opt.add_argument('--disable-gpu')
opt.add_argument('--hide-scrollbars') #隐藏滚动条, 应对一些特殊页面
# 用的是谷歌浏览器
driver = webdriver.Chrome(options=opt)
cookies = [{
        'domain': 'scrap.tf',
        'expiry': 1573527943,
        'httpOnly': True,
        'name': 'scr_session',
        'path': '/', 'secure': True,
        'value': 'bG9naW5fcmVkaXJlY3R8czoxNzoiaHR0cHM6Ly9zY3JhcC50Zi8iO2lkfGk6MjQ1NTk1Mjt0b2tlbnxzOjY0OiIxYTkxNDg0ZDVjNTRiZDcxYWZmZDg2NmUxNzI0NjQ4MDYyN2M5NzFmNDRmOTIyYjIzNTQwMGRkNjJhZTIwNDYxIjtmcmVlMnBsYXl8YjoxO3ByaXZhdGVWYWxpZGF0aW9ufGk6MTU2OTI5NzUyOTtiNjQ5OTIzNjY4OWE4MGY0MzFiNmViNjc0ZmVlNDg3MTQ2ZGViYTVmODgyZTg1NzE1NzdmNjlmZjllZjNhNWMxY2MzMjViY2M2MDhkODQzOTBmYzY3ZThmYzY3OWNmN2U0ZjkwMWZhZGViOTljMTFkMDkyZDhlOWEyMTkyYTU4YQ%3D%3D'
        # 大号
        #'value': 'bG9naW5fcmVkaXJlY3R8czoxNzoiaHR0cHM6Ly9zY3JhcC50Zi8iO2lkfGk6MTg0MzYwMDt0b2tlbnxzOjY0OiIwYjAyZWFmMDM1NzU0NDExNGY5ODYxNmNlMWM4MDMyMDQ0OGZmNjk2OTk2ZDZkMmRiNDdiZGFjNjM0NzBmYmE1IjtmcmVlMnBsYXl8YjowO3ByaXZhdGVWYWxpZGF0aW9ufGk6MTU2OTMwNzI5Mzs2MzBkNmRmNThhMzViZTUwNTg3MzY2ZTFkZDBhMjliOGJmMTVhMTgxNGE2NWY2MDBmNGQzM2YwNDdlZWM2ZWQ4YjcyZGVkMDFjNzdiM2I2ODg0NzU3YjZiMmFkMDQ5MjA5ZTA5ZjYzNjFmNGNlYjk2OTIyZDE0ODllNWM3ODcxMg%3D%3D'
        # 小号
        # 'value': 'bG9naW5fcmVkaXJlY3R8czoxNzoiaHR0cHM6Ly9zY3JhcC50Zi8iO2lkfGk6MTkwMzA2NDt0b2tlbnxzOjY0OiIwMDM1YzY2ZDc2ZDdhYTI4YWEyM2JhNmNhMTJiZTVlNTM4Nzk3MjJlNGE3MThjNjc0MTBiZDE5MTg0ZjE0NDllIjtmcmVlMnBsYXl8YjowO3ByaXZhdGVWYWxpZGF0aW9ufGk6MTU2OTI5NDM0MDs3YjU1NWE3OTUyYWMxZjhjYmIxYWRlMDYzOWMwZjM4NjJkYTA4MWJjODI5OWU0MzY5ZTZiMWMyZjc1NmQyYjQ4MTdmNmZkOTdlODk4YjY1MTQ5OTUwOTE2YzgxM2JmZmZhNTYwYjg0Mzc2Y2RhN2NjZGY1M2M1OTQzNzkzMmZiMg%3D%3D'
    }, {
        'domain': 'scrap.tf',
        'expiry': 1632366343,
        'httpOnly': False,
        'name': '_ga',
        'path': '/',
        'secure': False,
        'value': 'GA1.2.1693240194.1569294288'
    }, {
        'domain': 'scrap.tf',
        'expiry': 1600916743,
        'httpOnly': False,
        'name': '__auc',
        'path': '/',
        'secure': False,
        'value': '806fbdd616d613a826813b6bbbb'
    }, {
        'domain': 'scrap.tf',
        'expiry': 1577070343,
        'httpOnly': False,
        'name': '_fbp',
        'path': '/',
        'secure': False,
        'value': 'fb.1.1569294288084.1223469996'
    }, {
        'domain': 'scrap.tf',
        'expiry': 1569296143,
        'httpOnly': False,
        'name': '__asc',
        'path': '/',
        'secure': False,
        'value': '806fbdd616d613a826813b6bbbb'
    }, {
        'domain': 'scrap.tf',
        'expiry': 1569380743,
        'httpOnly': False,
        'name': '_gid',
        'path': '/',
        'secure': False,
        'value': 'GA1.2.255188840.1569294288'
    }, {
        'domain': 'scrap.tf',
        'expiry': 1600830286,
        'httpOnly': True,
        'name': '__cfduid',
        'path': '/',
        'secure': True,
        'value': 'd07bf593190b9fa50676bf1549c25edb71569294284'
    }]
    
driver.get("https://scrap.tf/raffles/")
print("正在前往 " + driver.title)
for cookie in cookies:
    # cookie.pop("domain")
    driver.add_cookie(cookie)
print("正在导入 cookies")
# driver.add_cookie(cookie)
driver.get("https://scrap.tf/raffles/")
print()
# f1 = open('d:/cookie.txt')
# cookie = f1.read()
# cookie = json.loads(cookie)
while True:
    print("正在获取 raffles 列表")
    # raffleList = driver.find_elements_by_class_name("raffle-name")
    rafflePage = driver.find_element_by_xpath("//div[@class='panel-raffle ' and not(contains(@class,'raffle-entered'))]")
    rafflePage = rafflePage.find_element_by_tag_name("div").find_element_by_tag_name("div").find_element_by_tag_name("a")
    # //div[contains(@class,'panel-raffle') and not(contains(@class,'raffle-entered'))]
    print("正在加入 " + rafflePage.get_attribute("href"))
    rafflePage.click()
    driver.find_element_by_id("raffle-enter").click()
    time.sleep(10)
    driver.back()
    time.sleep(10)
# print(type(raffleList))
# print("raffleList => " + str(raffleList))

# for i in raffleList:
#     # print(i)
#     rafflePage = i.find_element_by_tag_name("a").get_attribute("href")
#     print("正在打开 " + rafflePage)
    # print(i.find_element_by_tag_name("a").get_attribute("text"))
    # print(type(b))
    # print("b => " + str(b))
    # driver.get(rafflePage)
    # time.sleep(10000)
    # js = "window.open('" + rafflePage + "')"
    # driver.execute_script(js)
    

# for c in cookie:
#     driver.add_cookie(c)

# driver.refresh()






# a = driver.find_element_by_id("raffle-enter").click()
# print(type(a))
# print("a => " + str(a))

# driver.quit()
