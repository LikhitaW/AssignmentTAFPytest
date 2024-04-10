from selenium.webdriver.common.by import By
from utilities import seleniumFunctions
class LoginPage:

    username=(By.XPATH,"//input[@id='user-name']")
    password=(By.XPATH,"//input[@id='password']")
    login_btn=(By.XPATH,"//input[@id='login-button']")
    open_menu=(By.XPATH,"//button[contains(text(),'Open Menu')]")
    logout_btn=(By.XPATH,"//a[contains(text(),'Logout')]")
    error_login=(By.XPATH,"//div[@class='error-message-container error']")
    close_error=(By.XPATH,"//button[@class='error-button']")

    def __init__(self,driver):
        self.driver = driver

    def do_login(self,email,password):
        seleniumFunctions.enter_text_on_element(self,self.username,email)
        seleniumFunctions.enter_text_on_element(self,self.password,password)
        seleniumFunctions.click_on_element(self,self.login_btn)

    def do_logout(self):
        seleniumFunctions.click_on_element(self,self.open_menu)
        seleniumFunctions.click_on_element(self,self.logout_btn)

    def verify_error_invalid(self):
        bool_flg=seleniumFunctions.check_element_displayed(self,self.error_login)
        seleniumFunctions.click_on_element(self,self.close_error)
        self.driver.refresh()
        return bool_flg