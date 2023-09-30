import time

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver

from selenium.webdriver.common.by import By

import configparser


from Pages.DashboardPage import DashboardPage

config = configparser.ConfigParser()
config.read(r'config.txt')

url =config.get('global', 'my_url')
browser =  config.get('global', 'browser_name')

def before_all(context):

    if browser=="edge":
        options = webdriver.EdgeOptions()
        options.add_argument("--disable-notifications")
        options.add_experimental_option("detach", True)
        context.driver = webdriver.Edge(options=options)
    else:
        options=webdriver.ChromeOptions()
        options.add_argument("--disable-notifications")
        options.add_experimental_option("detach",True)
        context.driver = webdriver.Chrome(options=options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.get(url)

    #-------------------------------------------------
    #
    context.driver.find_element(By.XPATH, "//input[@id='email']").send_keys("manoj.assetmonk@gmail.com")
    context.driver.find_element(By.XPATH, "(//input[@id='examplePassword0'])[1]").send_keys("Propflo@1234")
    context.driver.find_element(By.XPATH, "//button[normalize-space()='Sign in']").click()
    time.sleep(3)
    context.driver.find_element(By.XPATH, "//app-topbar/div/div/div[2]/div[1]/img").click()
    time.sleep(2)
    #---------------------------------------------------
    context.driver.find_element(By.XPATH, "//a[text()='Users']").click()
    time.sleep(2)





def after_all(context):
    # context.DP=DashboardPage(context.driver)
    # context.DP.clickSignout()
    context.driver.quit()

def after_step(context,step):
    if step.status=="failed":
        allure.attach(context.driver.get_screenshot_as_png()
                      ,name="failed_screenshot"
                      ,attachment_type=AttachmentType.PNG)