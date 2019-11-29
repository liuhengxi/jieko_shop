from page.goodsDescription_page import ShoppingPage
from page.login_page import LoginPage
from page.shopoingCar_page import ShoppingCarPage
import time
import pytest
class Test_shopping01:
    def testShoping(self,open_driver01):
        open_driver01[0].click_goods()# 选择商品类
        open_driver01[0].click_mouse()# 选择鼠标
        open_driver01[0].click_amount()# 选择数量
        open_driver01[0].click_add()# 点击+号
        open_driver01[0].click_ok()# 点击确认
        open_driver01[0].click_basic()# 点击参数
        open_driver01[0].click_back()# 点击返回
        open_driver01[0].click_description()# 点击商品详情
        open_driver01[0].click_back()# 点击返回
        open_driver01[0].click_comment()# 点击商品评论
        open_driver01[0].click_back()# 点击返回
        open_driver01[0].click_addCar()# 点击加入购物车
        open_driver01[2].clear_username()# 情况点击栏
        open_driver01[2].send_username()# 输入账户名
        open_driver01[2].clear_password()# 情空输入栏
        open_driver01[2].send_password()# 输入密码
        open_driver01[2].click_index()# 点击登录
        open_driver01[0].click_addCar()  # 点击加入购物车
        open_driver01[0].click_car()  # 点击车子
        open_driver01[1].click_modifier()# 点击修改
        open_driver01[1].click_addc()# 点击增加
        open_driver01[1].click_okc()# 点击完成
        open_driver01[1].click_payment()# 点击结算
        open_driver01[3].click_payMethod()# 点击支付方式
        open_driver01[3].click_money()# 点击支付宝
        open_driver01[3].click_deliveryMethod()# 点击配送方式
        open_driver01[3].click_express()# 点击申通
        open_driver01[3].click_invoice()# 点击发票信息
        open_driver01[3].click_demo()# 点击demo
        open_driver01[3].click_pid()# 点击比列
        open_driver01[3].click_rise()# 点击发票抬头
        open_driver01[3].send_rise()# 输入发票
        open_driver01[3].click_save()  # 点击保存
        open_driver01[3].click_redBag()# 点击红吧
        open_driver01[3].click_bac()# 点击返回
        open_driver01[3].click_refer()# 点击提交订单
        open_driver01[3].click_confirm()# 点击确定
        open_driver01[3].click_alipay()# 点击支付宝
        end_text=open_driver01[3].text_end()# 获取最后信息
        assert end_text=='购买成功'

if __name__ == '__main__':
    pytest.main()



