#productPage_steps.py
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from features.steps.common_steps import *


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
    
    



@then('I should see the About this item button')
def step_impl(context):
    try:
        about_this_item_button = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="s0-1-25-7-18-1-92[1]-2-3-tabs-0"]'))
        )
        assert about_this_item_button.text is not None, "About this item button not found"
    except (TimeoutException, NoSuchElementException, AssertionError) as e:
        print(f"Exception during verification of About this item button: {e}")
        raise e


@then('I should see the Item specifics')       
def step_impl(context):
    try:
        specifics = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="s0-1-25-7-18-1-92[1]-2-3-7[0]-7[0]-4[0]-12[1]-1-2-title"]/span/span'))
        )
        assert specifics is not None, "Item specifics not found"
    except (TimeoutException, NoSuchElementException, AssertionError) as e:
        print(f"Exception during verification of About this item button: {e}")
        raise e    


@then('I should see the Condition')
def step_impl(context):
    try:
        condition = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="viTabs_0_is"]/div/div[2]/div/div[1]/div[1]/dl/dt/div/div/span'))
        )
        assert condition is not None, "Condition not found"
    except (TimeoutException, NoSuchElementException, AssertionError) as e:
        print(f"Exception during verification of About this item button: {e}")
        raise e  


@then('I should see the Item description from the seller')
def step_impl(context):
    try:
        sellerDec = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="viTabs_0_is"]/div/div[2]/div/div[1]/div[1]/dl/dt/div/div/span'))
        )
        assert sellerDec is not None, "Seller description not found"
    except (TimeoutException, NoSuchElementException, AssertionError) as e:
        print(f"Exception during verification of About this item button: {e}")
        raise e  


@then('I should see the Shipping, return, and payments button')
def step_impl(context):
    try:
        srpB = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="TABS_SPR"]/span'))
        )
        assert srpB is not None, "Shipping, return, and payments button not found"
    except (TimeoutException, NoSuchElementException, AssertionError) as e:
        print(f"Exception during verification of About this item button: {e}")
        raise e  
    


@then('I should see the Shipping and handling')
def step_impl(context):
    try:
        shipHandle = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="s0-1-25-7-18-1-92[1]-2-3-7[1]-7[1]-4[1]-59[1]-1-2-title"]/span/span'))
        )
        assert shipHandle is not None, "Shipping and Handling not found"
    except (TimeoutException, NoSuchElementException, AssertionError) as e:
        print(f"Exception during verification of About this item button: {e}")
        raise e  
    


@then('I should see the Return policy')        
def step_impl(context):
    try:
        rP = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="s0-1-25-7-18-1-92[1]-2-3-7[1]-7[1]-4[1]-24[2]-1-2-title"]/span/span'))
        )
        assert rP is not None, "Return policy button not found"
    except (TimeoutException, NoSuchElementException, AssertionError) as e:
        print(f"Exception during verification of About this item button: {e}")
        raise e  
    


@then('I should see the Payment details')      
def step_impl(context):
    try:
        pD = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="s0-1-25-7-18-1-92[1]-2-3-7[1]-7[1]-4[1]-26[3]-1-2-title"]/span/span'))
        )
        assert pD is not None, "Payments not found"
    except (TimeoutException, NoSuchElementException, AssertionError) as e:
        print(f"Exception during verification of About this item button: {e}")
        raise e  
    