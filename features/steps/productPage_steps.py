#productPage_steps.py
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from features.steps.common_steps import *
from bs4 import BeautifulSoup


@when('I search for "HP"')
def step_impl(context):
    try:
        search_bar = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "gh-ac"))
        )
        search_bar.clear()
        search_bar.send_keys("HP")
        search_bar.submit()
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Exception during search for HP: {e}")
        raise e

@then('I should see "HP" in the search results')
def step_impl(context):
    try:
        search_results = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".srp-controls__count-heading"))
        )
        assert "HP" in context.driver.page_source, "HP not found in search results"
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Exception during verification of search results for HP: {e}")
        raise e

# @then('I view the product details of the seventh product')
# def step_impl(context):
#     try:
#         # Get the product info container
#         product_info = WebDriverWait(context.driver, 10).until(
#             EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/div[4]/div[3]/div[1]/div[2]/ul/li[3]'))
#         ).get_attribute("innerHTML")
        
#         # soup = BeautifulSoup(product_info, 'html.parser')
#         # a_tag = soup.find('a', href=True)
#         # seventh_productLink = a_tag['href'] if a_tag else None
#         # seventh_productLink = soup.find('a', class_='s-item__link')['href']
        
#         # Parse the HTML element using Selenium
#         context.driver.get("data:text/html;charset=utf-8," + product_info)

#         # Find the link element
#         link_element = context.driver.find_element_by_css_selector("a.s-item__link")

#         # Get the link URL
#         link = link_element.get_attribute("href")
#         context.driver.get(link)
        
#         # if seventh_productLink:
#             # context.driver.get(seventh_productLink)
        
#     except (TimeoutException, NoSuchElementException) as e:
#         print(f"Exception during verification of product name: {e}")
#         raise e


@then('I view the product details of the seventh product')
def step_impl(context):
    try:
        # Ensure the search results are fully loaded
        search_results = WebDriverWait(context.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".srp-results .s-item"))
        )
        assert len(search_results) >= 7, "Less than 7 products found in search results"

        # Click on the seventh product
        seventh_product = search_results[6]
        seventh_product_link = seventh_product.find_element(By.CSS_SELECTOR, "a.s-item__link").get_attribute("href")
        context.driver.get(seventh_product_link)
    except (TimeoutException, NoSuchElementException, AssertionError) as e:
        print(f"Exception during navigation to the seventh product: {e}")
        raise e




@then('I should see the product name on the product page')
def step_impl(context):
    try:
        context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        product_name = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="mainContent"]/div[1]/div[1]/h1/span'))
        )
        assert product_name.text != ""
    except (TimeoutException, NoSuchElementException, AssertionError) as e:
        print(f"Exception during verification of product name: {e}")
        raise e

@then('I should see the product price on the product page')
def step_impl(context):
    try:
        product_price = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="mainContent"]/div[1]/div[3]/div/div/div[1]/span'))
        )
        assert product_price.text != ""
    except (TimeoutException, NoSuchElementException, AssertionError) as e:
        print(f"Exception during verification of product price: {e}")
        raise e

@then('I should see the product description on the product page')
def step_impl(context):
    try:
        product_description = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="s0-1-25-7-18-1-92[1]-2-3-tabpanel-0"]/div/div/div/div[3]'))
        )
        assert product_description.text != ""
    except (TimeoutException, NoSuchElementException, AssertionError) as e:
        print(f"Exception during verification of product description: {e}")
        raise e

@then('I should see the product image on the product page')
def step_impl(context):
    try:
        product_image = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="PicturePanel"]/div[1]/div/div/div[1]/div[2]/div[4]/div[1]'))
        )
        assert product_image.get_attribute("src") != ""
    except (TimeoutException, NoSuchElementException, AssertionError) as e:
        print(f"Exception during verification of product image: {e}")
        raise e