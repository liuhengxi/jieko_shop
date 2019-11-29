from appium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
def open_app(desired_caps):
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    return driver
class Base:
    def __init__(self,driver):
        self.driver=driver
        self.size = self.driver.get_window_size()
    def find_element(self,locator,timeout=10):
        """元素定位"""
        try:
            element=WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located(locator))
            return element
        except:
            print("没找到")
    def element_click(self,locator):
        """点击"""
        element=self.find_element(locator)
        element.click()
    def element_send_keys(self,locator,text):
        """输入"""
        element=self.find_element(locator)
        element.send_keys(text)
    def element_clear(self,locator):
        """清除"""
        element=self.find_element(locator)
        element.clear()
    def swipe_up(self,t=5000,n=1):
        '''
        向上滑动
        '''
        x1 = self.size['width'] * 0.5  # x坐标
        y1 = self.size['height'] * 0.75  # 起点y坐标
        y2 = self.size['height'] * 0.25  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)
    def swipeDown(self,t=500,n=1):
        '''向下滑动屏幕'''
        lower = self.driver.get_window_size()
        x1 = lower['width'] * 0.5  # x坐标
        y1 = lower['height'] * 0.25  # 起始y坐标
        y2 = lower['height'] * 0.75  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)
    def text(self,locator):
        element = self.find_element(locator)
        return element.text
if __name__ == '__main__':
    desired_caps = {
        "platformName": "Android",  # 系统名称
        "platformVersion": "5.1.1",  # 系统版本
        "deviceName": "127.0.0.1:21503",
        "appPackage": "com.android.settings",
        "appActivity": ".Settings",
        "unicodeKeyboard": True,
        "resetKeyboard": True

    }
    s=open_app(desired_caps)
    base=Base(s)
    # locator=("xpath","//*[@text='蓝牙']")
    # base.element_click(locator)
    base.swipe_up()