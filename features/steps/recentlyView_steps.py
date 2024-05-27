# recentlyView_steps.py
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from features.steps.common_steps import *


@then('I should see the Recently Viewed Products section')
def step_impl(context):
    try:
        context.driver.execute_script("window.scrollTo(0, 1400);")
        WebDriverWait(context.driver, 10)
        recently_viewed_section = WebDriverWait(context.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="mainContent"]/div[3]/div[1]/div/div/h2'))
        )
        assert recently_viewed_section is not None, "Recently Viewed Products section not found"    
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Exception during verification of Recently Viewed Products section: {e}")
        raise e

@then('I should see the product-1 title')      
def step_impl(context):
    try:
        context.driver.execute_script("window.scrollTo(0, 1400);")
        WebDriverWait(context.driver, 10)
        rviTitle = WebDriverWait(context.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="s0-1-0-48-1-3-5-14-0[1]-2-@match-media-0-@ebay-carousel-list"]/li[1]/div/a/div/div[2]/h3'))
        )
        assert rviTitle is not None, "Product 1 Title not found"    
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Exception during verification of Recently Viewed Products section: {e}")
        raise e

@then('I should see the product-1 price')      
def step_impl(context):
    try:
        context.driver.execute_script("window.scrollTo(0, 1400);")
        WebDriverWait(context.driver, 10)
        rviPrice = WebDriverWait(context.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="s0-1-0-48-1-3-5-14-0[1]-2-@match-media-0-@ebay-carousel-list"]/li[1]/div/a/div/div[2]/div/div/span'))
        )
        assert rviPrice is not None, "Product 1 Price not found"    
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Exception during verification of Recently Viewed Products section: {e}")
        raise e


@then('I should see the product-1 image')      
def step_impl(context):
    try:
        context.driver.execute_script("window.scrollTo(0, 1400);")
        WebDriverWait(context.driver, 10)
        rviImage = WebDriverWait(context.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="s0-1-0-48-1-3-5-14-0[1]-2-@match-media-0-@ebay-carousel-list"]/li[1]/div/a/div/div[1]/div/div'))
        )
        assert rviImage is not None, "Product 1 Image not found"    
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Exception during verification of Recently Viewed Products section: {e}")
        raise e

@then('I view the product page of product-1')
def step_impl(context):
    try:
        context.driver.execute_script("window.scrollTo(0, 1400);")
        first_product = WebDriverWait(context.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="s0-1-0-48-1-3-5-14-0[1]-2-@match-media-0-@ebay-carousel-list"]/li[1]/div/a'))
        )
        first_product_link = first_product.get_attribute("href")
        context.driver.get(first_product_link)
    
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Exception during verification of Recently Viewed Products section: {e}")
        raise e