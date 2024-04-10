from selenium.webdriver.common.by import By
from utilities import seleniumFunctions

class RemoveProductPage:

    price_item=(By.XPATH,"//div[@class='inventory_item_price']")
    remove_prod=(By.XPATH,"//button[contains(text(),'Remove')]")
    cart_item = (By.XPATH, "//div[@class='cart_item_label']")
    checkout_btn=(By.XPATH,"//button[contains(text(),'Checkout')]")

    def __init__(self,driver):
        self.driver = driver

    def remove_product(self):
        assert seleniumFunctions.check_element_displayed(self,self.price_item)
        seleniumFunctions.click_on_element(self,self.remove_prod)

    def verify_product_get_removed(self):
        assert seleniumFunctions.check_element_not_displayed(self,self.cart_item)

    def checkout_option(self):
        boo_flg=seleniumFunctions.check_element_enabled(self,self.checkout_btn)
        if boo_flg:
            seleniumFunctions.click_on_element(self,self.checkout_btn)
        return boo_flg