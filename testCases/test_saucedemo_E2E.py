import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.ProductPage import ProductPage
from pageObjects.AddProductPage import AddProductPage
from pageObjects.RemoveProductPage import RemoveProductPage
from utilities.readProperty import ReadConfigProperty
from utilities.customeLogger import LogGen
from utilities import seleniumFunctions


@pytest.mark.usefixtures("setup")
class Test_001_SauceDemoE2E:
    baseurl = ReadConfigProperty("common info","baseurl")
    email = ReadConfigProperty("common info", "username")
    password = ReadConfigProperty("common info", "password")
    logger = LogGen.loggen()

    def test_001_login_using_valid_credentials(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.act_title=self.driver.title
        self.loginpage = LoginPage(self.driver)
        self.loginpage.do_login(self.email, self.password)
        self.logger.info("User is able to login successfully")
        seleniumFunctions.capture_screenshot(self.loginpage, "Login Page")
        if self.act_title =="Swag Labs":
            assert True
        else:
            assert False


    def test_002_verify_product(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.loginpage = LoginPage(self.driver)
        self.loginpage.do_login(self.email, self.password)
        self.product=ProductPage(self.driver)
        # self.driver.implicitly_wait(10)
        time.sleep(10)
        self.product_list=self.product.verify_products()
        self.logger.info(self.product_list)
        self.logger.info("User is able to see products")
        seleniumFunctions.capture_screenshot(self.product,"Product page")

    def test_003_add_product_cart(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.loginpage = LoginPage(self.driver)
        self.loginpage.do_login(self.email, self.password)
        self.add_product=AddProductPage(self.driver)
        self.driver.implicitly_wait(10)
        time.sleep(10)
        self.add_product.add_product_to_cart()
        self.logger.info("Product is selected to add to cart")
        seleniumFunctions.capture_screenshot(self.add_product,"Product selected")
        self.add_product.verify_product_get_added()
        self.logger.info("Product get added to cart")
        seleniumFunctions.capture_screenshot(self.add_product,"Product to Cart")


    def test_004_remove_product_from_cart(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.loginpage = LoginPage(self.driver)
        self.loginpage.do_login(self.email, self.password)
        self.driver.implicitly_wait(10)
        time.sleep(10)
        self.add_product = AddProductPage(self.driver)
        self.add_product.verify_product_get_added()
        self.removeprod = RemoveProductPage(self.driver)
        self.removeprod.remove_product()
        self.logger.info("User is able to remove product from cart")
        seleniumFunctions.capture_screenshot(self.removeprod,"Product removed")
        time.sleep(5)
        self.removeprod.verify_product_get_removed()
        self.logger.info("Product gets removed from cart")
        seleniumFunctions.capture_screenshot(self.removeprod,"Empty cart")
        boo_flg=self.removeprod.checkout_option()
        if boo_flg=='False':
            self.logger.info("user should not be able to proceed for checkout")
            seleniumFunctions.capture_screenshot(self.removeprod,"Checkout not proceeded")
        else:
            self.logger.info("User is able to proceed for checkout")
            seleniumFunctions.capture_screenshot(self.removeprod,"Checkout proceeded")


    def test_005_logout(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.loginpage = LoginPage(self.driver)
        self.loginpage.do_login(self.email, self.password)
        self.loginpage =LoginPage(self.driver)
        time.sleep(2)
        self.driver.implicitly_wait(10)
        self.loginpage.do_logout()
        self.logger.info("User is logout successfully")
        seleniumFunctions.capture_screenshot(self.loginpage,"Logout successfully")
        self.driver.close()
