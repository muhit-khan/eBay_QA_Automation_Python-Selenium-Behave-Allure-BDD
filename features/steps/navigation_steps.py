from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from features.steps.common_steps import *

# Helper function to check visibility of navigation links
def check_nav_link(context, xpath, link_name):
    try:
        print(f"Checking visibility of {link_name} with selector {xpath}")
        link = WebDriverWait(context.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )
        assert link.is_displayed(), f"{link_name} is displayed"
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Exception during {link_name} link verification: {e}")
        context.driver.save_screenshot(f"{link_name.replace(' ', '_')}_error.png")
        raise e

@then('I should see the Saved in navigation bar')
def step_impl(context):
    check_nav_link(context, '//*[@id="vl-flyout-nav"]/ul/li[1]/a', "Saved")

@then('I should see the Electronics in navigation bar')
def step_impl(context):
    check_nav_link(context, '//*[@id="vl-flyout-nav"]/ul/li[2]/a', "Electronics")

@then('I should see the Motors in navigation bar')
def step_impl(context):
    check_nav_link(context, '//*[@id="vl-flyout-nav"]/ul/li[3]/a', "Motors")

@then('I should see the Fashion in navigation bar')
def step_impl(context):
    check_nav_link(context, '//*[@id="vl-flyout-nav"]/ul/li[4]/a', "Fashion")

@then('I should see the Collectibles and Art in navigation bar')
def step_impl(context):
    check_nav_link(context, '//*[@id="vl-flyout-nav"]/ul/li[5]/a', "Collectibles and Art")

@then('I should see the Sports in navigation bar')
def step_impl(context):
    check_nav_link(context, '//*[@id="vl-flyout-nav"]/ul/li[6]/a', "Sports")

@then('I should see the Health & Beauty in navigation bar')
def step_impl(context):
    check_nav_link(context, '//*[@id="vl-flyout-nav"]/ul/li[7]/a', "Health & Beauty")

@then('I should see the Industrial equipment in navigation bar')
def step_impl(context):
    check_nav_link(context, '//*[@id="vl-flyout-nav"]/ul/li[8]/a', "Industrial equipment")

@then('I should see the Home & Garden in navigation bar')
def step_impl(context):
    check_nav_link(context, '//*[@id="vl-flyout-nav"]/ul/li[9]/a', "Home & Garden")

@then('I should see the Deals in navigation bar')
def step_impl(context):
    check_nav_link(context, '//*[@id="vl-flyout-nav"]/ul/li[10]/a', "Deals")

@then('I should see the Sell in navigation bar')
def step_impl(context):
    check_nav_link(context, '//*[@id="vl-flyout-nav"]/ul/li[11]/a', "Sell")
