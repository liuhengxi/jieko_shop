from common.base import open_app,Base
class LoginPage(Base):
    username_page=("xpath","//*[@text='用户名']")# 用户名
    password_page=("id","com.insthub.ecmobile:id/login_password")
    index_page=("xpath","//*[@text='登录']")
    def click_username(self):
        self.element_click(self.username_page)
    def clear_username(self):
        self.element_clear(self.username_page)
    def send_username(self):
        self.element_send_keys(self.username_page,"lancer")
    def click_password(self):
        self.element_click(self.password_page)
    def clear_password(self):
        self.element_clear(self.password_page)
    def send_password(self):
        self.element_send_keys(self.password_page,"123456")
    def click_index(self):
        self.element_click(self.index_page)
if __name__ == '__main__':
    desired_caps = {
        "platformName": "Android",  # 系统名称
        "platformVersion": "5.1.1",  # 系统版本
        "deviceName": "127.0.0.1:21503",
        "appPackage": "com.insthub.ecmobile",
        "appActivity": ".activity.A0_SigninActivity"}
    driver=open_app(desired_caps)
    lg=LoginPage(driver)
    lg.click_username()
    lg.clear_username()
    lg.send_username()
    lg.click_password()
    lg.clear_password()
    lg.send_password()
    lg.click_index()