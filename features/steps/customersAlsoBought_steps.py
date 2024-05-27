# customersAlsoBought_steps.py
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from features.steps.common_steps import *

@then('I should see the Customer also boughts section')
def step_impl(context):
    try:
        context.driver.execute_script("window.scrollTo(0, 1400);")
        WebDriverWait(context.driver, 10)
        similar_items_section = WebDriverWait(context.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="placement101196"]/div/div/div/div/div'))
        )
        assert similar_items_section is not None, "Similar Items section not found"
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Exception during verification of Similar Items section: {e}")
        raise e


@then('I should see Customer also bought item\'s title')
def step_impl(context):
    try:
        similar_item_title = WebDriverWait(context.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="c4-15[0[0[0]]]-36-list"]/li[1]/div/div/div[2]/a/div/div[2]/h3'))
        )
        assert similar_item_title.text != "", "Similar Item title not found"
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Exception during verification of Similar Item title: {e}")
        raise e


@then('I should see Customer also bought item\'s condition')
def step_impl(context):
    try:
        similar_item_condition = WebDriverWait(context.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="c4-15[0[0[0]]]-36-list"]/li[1]/div/div/div[2]/a/div/div[2]/div[1]/div[1]/span'))
        )
        assert similar_item_condition.text != "", "Similar Item condition not found"
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Exception during verification of Similar Item condition: {e}")
        raise e


@then('I should see Customer also bought item\'s price')
def step_impl(context):
    try:
        similar_item_price = WebDriverWait(context.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="c4-15[0[0[0]]]-36-list"]/li[1]/div/div/div[2]/a/div/div[2]/div[1]/div[2]'))
        )
        assert similar_item_price.text != "", "Similar Item price not found"
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Exception during verification of Similar Item price: {e}")
        raise e




@then('I click on the first Customer also boughts Item')
def step_impl(context):
    try:
        similar_item_link = WebDriverWait(context.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="c4-15[0[0[0]]]-36-list"]/li[1]/div/div/div[2]/a/div/div[2]/h3'))
        )
        similar_item_link.click()
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Exception during clicking on the first Similar Item: {e}")
        raise e
