from common.base import open_app,Base
class PayMentPage(Base):
    payMethod_loc=("id","com.insthub.ecmobile:id/balance_pay_type")# 支付方式
    deliveryMethod_loc=("id","com.insthub.ecmobile:id/balance_dis")# 配送方式
    invoice_loc=("xpath","//*[@text='发票信息']")# 发票
    redBag_loc=("xpath","//*[@text='红包']")# 红包
    refer_loc=("xpath","//*[@text='提交订单']")# 提交订单
    money_loc=("xpath","//*[@text='支付宝']")# 支付宝
    express_loc=("xpath","//*[@text='申通快递']")# 申通快递
    demo_loc=("xpath","//*[@text='demo']")# demo
    pid_loc = ("id", "com.insthub.ecmobile:id/invoice_type1")# 比例
    rise_loc = ("xpath", "//*[@text='发票抬头']")  # 发票抬头
    save_loc = ("xpath", "//*[@text='保存']")# 保存
    bac_loc=("id","com.insthub.ecmobile:id/red_papaer_back")# 返回
    confirm_loc=("xpath", "//*[@text='确定']")# 确定
    alipay_loc=("xpath", "//*[@text='支付宝支付']")# 支付宝支付
    end_loc=("xpath", "//*[@text='很抱歉，“ECMobile”已停止运行。']")# 结束
    def click_payMethod(self):
        """点击支付方式"""
        self.element_click(self.payMethod_loc)
    def click_money(self):
        """点击支付宝"""
        self.element_click(self.money_loc)
    def click_deliveryMethod(self):
        """点击配送方式"""
        self.element_click(self.deliveryMethod_loc)
    def click_express(self):
        """点击申通快递"""
        self.element_click(self.express_loc)
    def click_invoice(self):
        """点击发票"""
        self.element_click(self.invoice_loc)
    def click_demo(self):
        """点击demo"""
        self.element_click(self.demo_loc)
    def click_pid(self):
        """点击比例"""
        self.element_click(self.pid_loc)
    def click_rise(self):
        """点击发票抬头"""
        self.element_click(self.rise_loc)
    def send_rise(self):
        """输入文本"""
        self.element_send_keys(self.rise_loc,"好饿")
    def click_save(self):
        """点击保存"""
        self.element_click(self.save_loc)
    def click_redBag(self):
        """点击红包"""
        self.element_click(self.redBag_loc)
    def click_bac(self):
        """点击返回"""
        self.element_click(self.bac_loc)
    def click_refer(self):
        """点击提交订单"""
        self.element_click(self.refer_loc)
    def click_confirm(self):
        """点击确定"""
        self.element_click(self.confirm_loc)
    def click_alipay(self):
        """选择支付宝支付"""
        self.element_click(self.alipay_loc)
    def text_end(self):
        """落幕"""
        self.text(self.end_loc)