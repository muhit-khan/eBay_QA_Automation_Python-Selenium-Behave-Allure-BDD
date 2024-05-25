#search_steps.py 
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from features.steps.common_steps import *

def perform_search(context, search_term):
    try:
        search_bar = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "gh-ac"))
        )
        search_bar.clear()
        search_bar.send_keys(search_term)
        search_bar.submit()
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Exception during search for {search_term}: {e}")
        raise e

def verify_search_results(context, search_term):
    try:
        search_results = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".srp-controls__count-heading"))
        )
        assert search_term.lower() in context.driver.page_source.lower(), f"{search_term} not found in search results"
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Exception during verification of search results for {search_term}: {e}")
        raise e

@when('I search for "iPhone"')
def step_impl(context):
    perform_search(context, "iPhone")

@then('I should see "iPhone" in the search results')
def step_impl(context):
    verify_search_results(context, "iPhone")

@when('I search for "Samsung"')
def step_impl(context):
    perform_search(context, "Samsung")

@then('I should see "Samsung" in the search results')
def step_impl(context):
    verify_search_results(context, "Samsung")

@when('I search for "Nokia"')
def step_impl(context):
    perform_search(context, "Nokia")

@then('I should see "Nokia" in the search results')
def step_impl(context):
    verify_search_results(context, "Nokia")