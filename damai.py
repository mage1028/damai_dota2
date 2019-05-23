from selenium import webdriver
import time

d = webdriver.Chrome()

d.get('http://www.damai.cn')
while 1:
    try:
        windows = d.window_handles
        # 切换到当前最新打开的窗口
        d.switch_to.window(windows[-1])
        a = d.find_element_by_xpath('''//span[@class="next-checkbox-label"]''')
        a.click()

        break
    except:
        pass
while 1:
    try:
        b = d.find_element_by_xpath(
            '//div[@class="submit-wrapper"]/button[@class="next-btn next-btn-normal next-btn-medium"]')
        b.click()
        break
    except:
        pass
    try:
        c = d.find_element_by_xpath('//*[@id="confirmOrder_1"]/div[9]/button')
        c.click()
    except:
        pass
time.sleep(100)
