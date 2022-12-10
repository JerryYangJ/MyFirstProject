from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

'''
    selenium用于动态渲染页面爬取
    1.创建浏览器对象：
        web = Chrome()
    2.访问页面：
        web.get(url）
    3.关闭浏览器对象：
        web.close()
    4.选取单个节点（多节点加s）方法：返回WebElement对象
        find_element_by_id
        find_element_by_name
        find_element_by_xpath
        find_element_by_link_text
        find_element_by_partial_link_text
        find_element_by_tag_name
        find_element_by_class_name
        find_element_by_css_selector
    5.通用方法：find_element()/find_elements()，返回WebElement对象(列表）
        find_element(By.ID, 'a')
    6.获取节点信息：
        -通过page_source属性获取网页的源代码，使用解析库（正则、BS4、xpath等）提取信息。
        -使用Selenium选取节点的方法，返回的WebElement对象，使用WebElement对象相关的方法和属性来直接提取节点信息
            -获取属性：get_attribute()方法获取节点的属性
            -获取文本值：直接调用WebElement的text属性获取节点内u的文本信息
    7.节点交互：
        send_keys():    输入文字
        clear():        清空文字
        click()：        点击按钮
    8.切换Frame和选项卡windows:
        switch_to.frame():   切换Frame，传入Frame的name属性
        switch_to.window():    切换选项卡，传入选项卡代号（具体参第10点）
    9.Cookies:
        -get_cookies():获取Cookies
        -add_cookies(dic):添加Cookies(传入字典）
        -delete_all_cookies()：删除所有的Cookies
    10.选项卡管理：
        -web.execute_script('window.open()'): 执行开启一个新选项卡的JavaScript语句
        -web.window_handles: window_handles属性调用，获取当前开启的所有选项卡，返回选项卡的代号list
    11.无头参数设置（固定写法，直接copy即可）：
        opt = Options()
        opt.add_argument("--headless")  # 无头
        opt.add_argument('--disable-gpu')
        web = Chrome(options=opt)
    12.延时等待：
        -隐式等待：没有找到节点时继续等待至超设定时间后再次查找，如果找不到则抛出异常
            web.implicitly_wait():传入等待时间
        -显示等待：指定要查找的节点，并指定一个最长等待时间，使用until()方法传入一个等待条件，如果规定时间条件满足，则返回节点。超时抛出异常
            wait = WebDriverWait(web, 10)    # 创建一个WebDriverWait对象，指定最长等待时间
            wait.until(EC)                   # 调用until()方法，设置等待条件
        
'''



# 无头参数设置
# opt = Options()
# opt.add_argument("--headless")  # 无头
# opt.add_argument('--disable-gpu')
#
# web = Chrome(options=opt)

web = Chrome()
try:
    web.get("http://www.baidu.com")
    input = web.find_element(By.ID, 'kw')
    input.send_keys('Python')
    input.send_keys(Keys.ENTER)

    # 设置显式等待，10秒内如果id=‘content_left'节点加载出来，则返回这个节点，否则抛出异常
    wait = WebDriverWait(web, 10)   # 显式等待
    wait.until(EC.presence_of_element_located(By.ID, 'content_left'))



    print(web.current_url)  # 输出当前url
    print(web.get_cookies())    # 输出当前Cookies
    print(web.page_source)      # 输出网页源代码
finally:
    web.close()



# print(web.title)