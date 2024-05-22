from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@then('the navigation bar should have "Electronics", "Saved", and "Motors" links')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT, "Electronics")
    assert context.driver.find_element(By.LINK_TEXT, "Saved")
    assert context.driver.find_element(By.LINK_TEXT, "Motors")

@then('the user should be able to navigate to the "eBay Community" page')
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    wait = WebDriverWait(context.driver, 30)
    footer_link = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="gf-BIG"]/table/tbody/tr/td[5]/ul[2]/li[2]/a')))
    footer_link.click()
    assert "eBay Community" in context.driver.title

@then('the eBay logo should link to the homepage')
def step_impl(context):
    logo = context.driver.find_element(By.ID, "gh-la")
    logo.click()
    assert context.driver.current_url == "https://www.ebay.com/"

@then('the user should be able to navigate to the "Electronics" category')
def step_impl(context):
    category_link = context.driver.find_element(By.LINK_TEXT, "Electronics")
    category_link.click()
    assert "Electronics" in context.driver.title

@then('the user should be able to navigate to the "Cell Phones & Accessories" sub-category')
def step_impl(context):
    sub_category_link = context.driver.find_element(By.LINK_TEXT, "Cell Phones & Accessories")
    sub_category_link.click()
    assert "Cell Phones & Accessories" in context.driver.title
