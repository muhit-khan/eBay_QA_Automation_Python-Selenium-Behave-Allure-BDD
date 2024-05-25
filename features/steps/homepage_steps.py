#homepage_steps.py 
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from features.steps.common_steps import *

@then('the eBay logo should be displayed')
def step_impl(context):
    try:
        logo = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "gh-logo"))
        )
        assert logo.is_displayed(), "Test Passed"
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Exception during logo verification: {e}")
        raise e

@then('the search bar should be displayed')
def step_impl(context):
    try:
        search_bar = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "gh-ac"))
        )
        assert search_bar.is_displayed(), "Test Passed"
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Exception during search bar verification: {e}")
        raise e

@then('the main content area should be displayed')
def step_impl(context):
    try:
        main_content = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "mainContent"))
        )
        assert main_content.is_displayed(), "Test Passed"
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Exception during main content verification: {e}")
        raise e

@then('the popular categories menu should be displayed')
def step_impl(context):
    try:
        popular_categories = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "vl-card-header__headline"))
        )
        assert popular_categories.is_displayed(), "Test Passed"
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Exception during popular categories verification: {e}")
        raise e
    
@then('the site shifting options should be displayed')
def step_impl(context):
    try:
        site_shifting = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "gf-bttl"))
        )
        assert site_shifting.is_displayed(), "Test Passed"
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Exception during site shifting verification: {e}")
        raise e
    
@then('the footer should be displayed')
def step_impl(context):
    try:
        footer = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "glbfooter"))
        )
        assert footer.is_displayed(), "Test Passed"
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Exception during footer verification: {e}")
        raise e
