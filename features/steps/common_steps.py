#common_steps.py
from behave import *
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait

@given('I launch Chrome Browser')
def step_impl(context):
    try:
        context.driver.maximize_window()
    except WebDriverException as e:
        print(f"Exception during browser maximization: {e}")
        raise e

@when('I open homepage')
def step_impl(context):
    try:
        context.driver.get("https://www.ebay.com")
        context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        WebDriverWait(context.driver, 5)
        context.driver.execute_script("window.scrollTo(0, 0);")
        WebDriverWait(context.driver, 5)
    except WebDriverException as e:
        print(f"Exception during opening homepage: {e}")
        raise e
