from common.base import open_app,Base
class ShoppingCarPage(Base):
    modifier_loc=("xpath","//*[@text='修改']")# 修改按钮
    add_loc = ("id", "com.insthub.ecmobile:id/shop_car_item_sum")  # 添加数量按钮
    ok_loc=("xpath","//*[@text='完成']")# 完成按钮
    payment_loc=("xpath","//*[@text='结算']")# 结算按钮
    def click_modifier(self):
        """点击修改"""
        self.element_click(self.modifier_loc)
    def click_addc(self):
        """点击添加"""
        self.element_click(self.add_loc)
    def click_okc(self):
        """点击完成"""
        self.element_click(self.ok_loc)
    def click_payment(self):
        """点击结算"""
        self.element_click(self.payment_loc)
if __name__ == '__main__':
    desired_caps = {
        "platformName": "Android",  # 系统名称
        "platformVersion": "5.1.1",  # 系统版本
        "deviceName": "127.0.0.1:21503",
        "appPackage": "com.insthub.ecmobile",
        "appActivity": "/.activity.C0_ShoppingCartActivity"}
    driver=open_app(desired_caps)
    sc=ShoppingCarPage(driver)
    sc.click_modifier()
    sc.click_add()
    sc.click_ok()
    sc.click_payment()