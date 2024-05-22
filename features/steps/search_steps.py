from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('the user searches for "Laptop"')
def step_impl(context):
    context.driver.get("https://www.ebay.com")
    search_box = context.driver.find_element(By.NAME, "_nkw")
    search_box.send_keys("Laptop")
    search_box.submit()

@then('the search results should contain "Laptop" in the title')
def step_impl(context):
    assert "Laptop" in context.driver.title

@then('the search results should be displayed')
def step_impl(context):
    assert context.driver.find_elements(By.CSS_SELECTOR, ".s-item")

@given('the user clicks the search button after entering "laptop"')
def step_impl(context):
    context.driver.get("https://www.ebay.com")
    search_box = context.driver.find_element(By.ID, "gh-ac")
    search_box.send_keys("laptop")
    search_button = context.driver.find_element(By.ID, "gh-btn")
    search_button.click()

@given('the user navigates to the search results page for "Laptop"')
def step_impl(context):
    context.driver.get("https://www.ebay.com/sch/i.html?_nkw=Laptop")

@then('the pagination should be displayed and functional')
def step_impl(context):
    pagination = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".pagination__items"))
    )
    assert pagination.is_displayed()
    next_button = context.driver.find_element(By.CSS_SELECTOR, ".pagination__next")
    next_button.click()
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".pagination__items")))

@then('the user should be able to filter results by "New" condition')
def step_impl(context):
    new_condition_filter = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@aria-label='New']"))
    )
    new_condition_filter.click()
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'New')]"))
    )
