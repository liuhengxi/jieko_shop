import pytest
from common.base import open_app
from page.goodsDescription_page import ShoppingPage
from page.login_page import LoginPage
from page.shopoingCar_page import ShoppingCarPage
from page.payment_page import PayMentPage




@pytest.fixture(scope='class')
def open_driver01(request):
    desired_caps = {
        "platformName": "Android",  # 系统名称
        "platformVersion": "5.1.1",  # 系统版本
        "deviceName": "127.0.0.1:21503",
        "appPackage": "com.insthub.ecmobile",
        "appActivity": ".activity.EcmobileMainActivity",
        "unicodeKeyboard": True,
        "resetKeyboard": True}
    driver=open_app(desired_caps)
    sp=ShoppingPage(driver)
    scp = ShoppingCarPage(driver)
    lg = LoginPage(driver)
    pm = PayMentPage(driver)
    def end():
        driver.quit()
        request.addfinalizer(end)
    return sp,scp,lg,pm
