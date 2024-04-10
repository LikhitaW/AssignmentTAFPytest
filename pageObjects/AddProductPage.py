from selenium.webdriver.common.by import By
from utilities import seleniumFunctions

class AddProductPage:
    add_product=(By.XPATH,"//a/div[contains(text(),'Sauce Labs Backpack')]")
    add_to_cart_btn=(By.XPATH,"//button[contains(text(),'Add to cart')]")
    check_cart=(By.XPATH,"//a[@class='shopping_cart_link']")
    cart_item=(By.XPATH,"//div[@class='cart_item_label']")

    def __init__(self,driver):
        self.driver = driver

    def add_product_to_cart(self):
        seleniumFunctions.click_on_element(self,self.add_product)
        seleniumFunctions.click_on_element(self,self.add_to_cart_btn)

    def verify_product_get_added(self):
        seleniumFunctions.click_on_element(self,self.check_cart)
        assert seleniumFunctions.check_element_displayed(self,self.cart_item)
