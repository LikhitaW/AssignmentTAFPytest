import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

TEXT_TIMEOUT=10
# Enter and retrieve text of element
def enter_text_on_element(self,locator,text):
    element=WebDriverWait(self.driver,TEXT_TIMEOUT).until(
        EC.visibility_of_element_located(locator)
    )
    element.clear()
    element.send_keys(text)

def get_text_on_element(self,locator):
    element = WebDriverWait(self.driver, TEXT_TIMEOUT).until(
        EC.visibility_of_element_located(locator)
    )
    return element.text

#visibility functions
def check_element_displayed(self,locator):
    element = WebDriverWait(self.driver, TEXT_TIMEOUT).until(
        EC.visibility_of_element_located(locator)
    )
    return element.is_displayed()

def check_element_not_displayed(self,locator):
    element = WebDriverWait(self.driver, TEXT_TIMEOUT).until(
        EC.invisibility_of_element_located(locator)
    )
    return element

def check_element_enabled(self,locator):
    element = WebDriverWait(self.driver, TEXT_TIMEOUT).until(
        EC.visibility_of_element_located(locator)
    )
    return element.is_enabled()
#click action
def click_on_element(self,locator):
    element = WebDriverWait(self.driver, TEXT_TIMEOUT).until(
        EC.visibility_of_element_located(locator)
    )
    element.click()

#list of elements
def get_elements(self,locator):
    return WebDriverWait(self.driver,TEXT_TIMEOUT).until(
        EC.presence_of_all_elements_located(locator)
    )

#allure screenshot
def capture_screenshot(page_object,image_name):
    allure.attach(page_object.driver.get_screenshot_as_png(),
                  name=f"{image_name}.png",
                  attachment_type=AttachmentType.PNG)


