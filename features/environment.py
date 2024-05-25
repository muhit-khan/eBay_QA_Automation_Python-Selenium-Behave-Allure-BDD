from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def before_all(context):
    # Set up the WebDriver with the correct driver path
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service)

def after_all(context):
    # Quit the WebDriver
    context.driver.quit()
