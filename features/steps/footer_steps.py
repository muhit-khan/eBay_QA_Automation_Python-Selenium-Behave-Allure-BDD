from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@when('the user scrolls to the bottom of the page')
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

@then('the footer should contain the "eBay Community" link')
def step_impl(context):
    wait = WebDriverWait(context.driver, 30)
    footer_link = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="gf-BIG"]/table/tbody/tr/td[5]/ul[2]/li[2]/a')))
    assert "eBay Community" in footer_link.text

@then('the footer should have links')
def step_impl(context):
    footer_links = context.driver.find_elements(By.CSS_SELECTOR, "#gf-BIG a")
    assert len(footer_links) > 0
