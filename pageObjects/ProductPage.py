from selenium.webdriver.common.by import By
from utilities import seleniumFunctions

class ProductPage:
    products=(By.XPATH,"//span[text()='Products']")
    product_list_loc = (By.XPATH,"//a//div[contains(@class,'inventory_item_name')]")

    def __init__(self,driver):
        self.driver = driver

    def verify_products(self):
        assert seleniumFunctions.check_element_displayed(self,self.products)
        product_name=[]
        product_list= seleniumFunctions.get_elements(self,self.product_list_loc)
        for product in product_list:
            productname=product.text
            print(productname)
            product_name.append(productname)
        return product_name