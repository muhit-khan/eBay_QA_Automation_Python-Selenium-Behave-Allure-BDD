from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@then('the user should see product listings for "laptop"')
def step_impl(context):
    context.driver.get("https://www.ebay.com/sch/i.html?_nkw=laptop")
    assert context.driver.find_elements(By.CSS_SELECTOR, ".s-item")

@then('the product images should be displayed')
def step_impl(context):
    product_image = context.driver.find_element(By.CSS_SELECTOR, ".s-item__image-img")
    assert product_image.is_displayed()

@then('the "Advanced" search link should be displayed and clickable')
def step_impl(context):
    context.driver.get("https://www.ebay.com")
    advanced_search_link = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Advanced"))
    )
    assert advanced_search_link.is_displayed()
    advanced_search_link.click()
    WebDriverWait(context.driver, 10).until(EC.title_contains("Advanced Search"))

@then('the "Daily Deals" link should be displayed and clickable')
def step_impl(context):
    daily_deals_link = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Daily Deals"))
    )
    assert daily_deals_link.is_displayed()
    daily_deals_link.click()
    WebDriverWait(context.driver, 10).until(EC.title_contains("Daily Deals"))

@then('the "Sell" link should be displayed and clickable')
def step_impl(context):
    sell_link = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Sell"))
    )
    assert sell_link.is_displayed()
    sell_link.click()
    WebDriverWait(context.driver, 10).until(EC.title_contains("Sell"))

@then('the "Sign out" button should not be present')
def step_impl(context):
    sign_out_button = context.driver.find_elements(By.LINK_TEXT, "Sign out")
    assert len(sign_out_button) == 0

@then('the "Accessibility" link should be displayed and clickable')
def step_impl(context):
    accessibility_link = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Accessibility"))
    )
    assert accessibility_link.is_displayed()
    accessibility_link.click()
    WebDriverWait(context.driver, 10).until(EC.title_contains("Accessibility"))
