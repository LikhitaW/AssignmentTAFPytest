import time
import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperty import ReadConfigProperty
from utilities.customeLogger import LogGen
from utilities import seleniumFunctions
from utilities import excelUtils

@pytest.mark.usefixtures("setup")
class Test_001_Login:
    baseurl = ReadConfigProperty("common info","baseurl")
    email = ReadConfigProperty("common info", "username")
    password = ReadConfigProperty("common info", "password")
    path = ".//TestData//LoginData.xlsx"
    logger = LogGen.loggen()

    def test_001_login_using_valid_credentials(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.lp=LoginPage(self.driver)
        self.lp.do_login(self.email,self.password)
        time.sleep(2)
        act_title=self.driver.title
        if act_title == "Swag Labs":
            assert True
        else:
            assert False
        self.logger.info("User is able to login successfully")
        seleniumFunctions.capture_screenshot(self.lp,"Login Page")
        self.lp.do_logout()


    def test_002_ddt_login_using_invalid_credentials(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.rows = excelUtils.getRowCount(self.path,'Sheet1')
        self.logger.info(f"Number of rows {self.rows}")
        for r in range(2,int(self.rows+1)):
            self.username = excelUtils.readData(self.path,'Sheet1',r,1)
            self.password = excelUtils.readData(self.path,'Sheet1',r,2)
            self.exp_result = excelUtils.readData(self.path,'Sheet1',r,3)
            self.lp.do_login(self.username,self.password)
            time.sleep(2)
            seleniumFunctions.capture_screenshot(self.lp,"Invalid Login credentials")
            self.logger.info("user is unable to login")
            self.lp.verify_error_invalid()
            if self.exp_result=='Fail':
                seleniumFunctions.capture_screenshot(self.lp,"Error Message")
                self.logger.info("Error message appear for invalid")
        self.driver.close()
