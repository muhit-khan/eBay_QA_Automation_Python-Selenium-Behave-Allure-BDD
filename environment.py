from config.config import get_driver
from selenium import webdriver

def before_all(context):
    # You can set up a single browser instance for all tests
    context.driver = webdriver.Chrome()  # or any other browser like Firefox
    context.driver.maximize_window()

def after_all(context):
    # Close the browser instance after all tests are done
    context.driver.quit()

def before_scenario(context, scenario):
    # Alternatively, you can setup a new browser instance for each scenario
    context.driver = webdriver.Chrome()  # or any other browser like Firefox
    context.driver.maximize_window()

def after_scenario(context, scenario):
    # Close the browser instance after each scenario
    context.driver.quit()
