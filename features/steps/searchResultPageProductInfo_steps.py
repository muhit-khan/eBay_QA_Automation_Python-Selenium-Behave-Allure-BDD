#searchResultPageProductInfo_steps.py


from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from features.steps.common_steps import *
from bs4 import BeautifulSoup



@then('I should see the search bar')
def step_impl(context):
    try:
        search_bar = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "gh-ac"))
        )
        assert search_bar.is_displayed(), "Search bar is not displayed"
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Exception during search bar visibility check: {e}")
        raise e

@when('I search for "Dell"')
def step_impl(context):
    try:
        search_bar = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "gh-ac"))
        )
        search_bar.clear()
        search_bar.send_keys("Dell")
        search_bar.submit()
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Exception during search for Dell: {e}")
        raise e

@then('I should see "Dell" in the search results')
def step_impl(context):
    try:
        search_results = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".srp-controls__count-heading"))
        )
        assert "Dell" in context.driver.page_source, "Dell not found in search results"
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Exception during verification of search results for Dell: {e}")
        raise e

# @then('I should see the product name')
# def step_impl(context):
#     try:
#         # Get the product info container
#         product_info = WebDriverWait(context.driver, 10).until(
#             EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/div[4]/div[3]/div[1]/div[2]/ul/li[3]'))
#         ).get_attribute("innerHTML")
        
#         # Parse the HTML with BeautifulSoup
#         soup = BeautifulSoup(product_info, 'html.parser')
#         product_name_tag = soup.find(class_="s-item__title")
#         assert product_name_tag is not None, "Product name tag not found"
#         product_name = product_name_tag.text.strip()
#         assert "Dell" in product_name, "Product name does not contain Dell"
#     except (TimeoutException, NoSuchElementException) as e:
#         print(f"Exception during verification of product name: {e}")
#         raise e

# @then('I should see the price of the product')
# def step_impl(context):
#     try:
#         # Get the product info container
#         product_info = WebDriverWait(context.driver, 10).until(
#             EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/div[4]/div[3]/div[1]/div[2]/ul/li[3]'))
#         ).get_attribute("innerHTML")
        
#         # Parse the HTML with BeautifulSoup
#         soup = BeautifulSoup(product_info, 'html.parser')
#         product_price_tag = soup.find(class_="s-item__price")
#         assert product_price_tag is not None, "Product price is not displayed"
#     except (TimeoutException, NoSuchElementException) as e:
#         print(f"Exception during verification of product price: {e}")
#         raise e

# @then('I should see the condition of the product')
# def step_impl(context):
#     try:
#         # Get the product info container
#         product_info = WebDriverWait(context.driver, 10).until(
#             EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/div[4]/div[3]/div[1]/div[2]/ul/li[3]'))
#         ).get_attribute("innerHTML")
        
#         # Parse the HTML with BeautifulSoup
#         soup = BeautifulSoup(product_info, 'html.parser')
#         product_subtitle_tag = soup.find(class_="SECONDARY_INFO")
#         assert product_subtitle_tag is not None, "Product condition is not displayed"
#     except (TimeoutException, NoSuchElementException) as e:
#         print(f"Exception during verification of product price: {e}")
#         raise e

# @then('I should see the product image')
# def step_impl(context):
#     try:
#         product_image = WebDriverWait(context.driver, 10).until(
#             EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/div[4]/div[3]/div[1]/div[2]/ul/li[3]/div/div[1]/div/a/div/img'))
#         )
#         assert product_image.is_displayed(), "Product image is not displayed"
#     except (TimeoutException, NoSuchElementException) as e:
#         print(f"Exception during verification of product image: {e}")
#         raise e


@then('I should see the product name')
def step_impl(context):
    try:
        # Get the product info container
        product_info = WebDriverWait(context.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@class="srp-results srp-list clearfix"]/li[3]'))
        ).get_attribute("innerHTML")
        
        # Parse the HTML with BeautifulSoup
        soup = BeautifulSoup(product_info, 'html.parser')
        product_name_tag = soup.find(class_="s-item__title")
        assert product_name_tag is not None, "Product name tag not found"
        product_name = product_name_tag.text.strip()
        assert "Dell" in product_name, "Product name does not contain Dell"
    except (TimeoutException, NoSuchElementException, AssertionError) as e:
        print(f"Exception during verification of product name: {e}")
        raise e

@then('I should see the price of the product')
def step_impl(context):
    try:
        # Get the product info container
        product_info = WebDriverWait(context.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@class="srp-results srp-list clearfix"]/li[3]'))
        ).get_attribute("innerHTML")
        
        # Parse the HTML with BeautifulSoup
        soup = BeautifulSoup(product_info, 'html.parser')
        product_price_tag = soup.find(class_="s-item__price")
        assert product_price_tag is not None, "Product price is not displayed"
    except (TimeoutException, NoSuchElementException, AssertionError) as e:
        print(f"Exception during verification of product price: {e}")
        raise e

@then('I should see the condition of the product')
def step_impl(context):
    try:
        # Get the product info container
        product_info = WebDriverWait(context.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@class="srp-results srp-list clearfix"]/li[3]'))
        ).get_attribute("innerHTML")
        
        # Parse the HTML with BeautifulSoup
        soup = BeautifulSoup(product_info, 'html.parser')
        product_subtitle_tag = soup.find(class_="SECONDARY_INFO")
        assert product_subtitle_tag is not None, "Product condition is not displayed"
    except (TimeoutException, NoSuchElementException, AssertionError) as e:
        print(f"Exception during verification of product condition: {e}")
        raise e

@then('I should see the product image')
def step_impl(context):
    try:
        product_image = WebDriverWait(context.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@class="srp-results srp-list clearfix"]/li[3]/div/div[1]/div/a/div/img'))
        )
        assert product_image.is_displayed(), "Product image is not displayed"
    except (TimeoutException, NoSuchElementException, AssertionError) as e:
        print(f"Exception during verification of product image: {e}")
        raise e