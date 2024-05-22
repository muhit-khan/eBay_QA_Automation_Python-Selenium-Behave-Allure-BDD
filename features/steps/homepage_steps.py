from behave import given, when, then
from selenium.webdriver.common.by import By

@given('the user is on the eBay homepage')
def step_impl(context):
    context.driver.get("https://www.ebay.com")

@then('the eBay logo should be displayed')
def step_impl(context):
    assert context.driver.find_element(By.ID, "gh-la").is_displayed()

@then('the search bar should be displayed')
def step_impl(context):
    assert context.driver.find_element(By.ID, "gh-ac").is_displayed()

@then('the main content area should be displayed')
def step_impl(context):
    assert context.driver.find_element(By.ID, "mainContent").is_displayed()

@then('the title should contain "eBay"')
def step_impl(context):
    assert "eBay" in context.driver.title
