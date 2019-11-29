from common.base import open_app,Base
class ShoppingPage(Base):
    iphone_loc=("xpath","//*[@text='手机']")# 选择手机
    mouse_loc=("xpath","//*[@text='￥5.88元']")# 选择鼠标垫
    addCar_loc=("xpath","//*[@text='加入购物车']")# 加入购物车
    amount_loc=("id","com.insthub.ecmobile:id/good_category") #点击数量
    add_loc=("id","com.insthub.ecmobile:id/shop_car_item_sum")# 添加数量按钮
    ok_loc=("xpath","//*[@text='确定']")# 确定
    basic_loc=("xpath","//*[@text='基本参数']")# 基本参数
    description_loc=("xpath","//*[@text='商品描述']")# 商品描述
    comment_loc=("xpath","//*[@text='商品评论']")# 商品评论
    back_loc = ("id", "com.insthub.ecmobile:id/top_view_back")  # 返回
    car_loc=("id","com.insthub.ecmobile:id/good_detail_shopping_cart")# 车子标
    def click_goods(self):
        """选择商品类"""
        self.element_click(self.iphone_loc)
    def click_mouse(self):
        """选择商品"""
        self.element_click(self.mouse_loc)
    def click_amount(self):
        """点击数量"""
        self.element_click(self.amount_loc)
    def click_add(self):
        """点击+号"""
        self.element_click(self.add_loc)
    def click_ok(self):
        """点击确定"""
        self.element_click(self.ok_loc)
    def click_basic(self):
        """点击参数"""
        self.element_click(self.basic_loc)
    def click_description(self):
        """点击商品描述"""
        self.element_click(self.description_loc)
    def click_comment(self):
        """商品评论"""
        self.element_click(self.comment_loc)
    def click_back(self):
        """点击返回"""
        self.element_click(self.back_loc)
    def click_addCar(self):
        """点击添加购物车"""
        self.element_click(self.addCar_loc)
    def click_car(self):
        """点击车车"""
        self.element_click(self.car_loc)

if __name__ == '__main__':
    desired_caps = {
        "platformName": "Android",  # 系统名称
        "platformVersion": "5.1.1",  # 系统版本
        "deviceName": "127.0.0.1:21503",
        "appPackage": "com.insthub.ecmobile",
        "appActivity": ".activity.EcmobileMainActivity"}
    driver=open_app(desired_caps)
    sp=ShoppingPage(driver)
    sp.click_goods()
    sp.click_amount()
    sp.click_add()
    sp.click_ok()
    sp.click_basic()
    sp.click_back()
    sp.click_description()
    sp.click_back()
    sp.click_comment()
    sp.click_back()
    sp.click_addCar()