# **eBay QA Automation with Python, Selenium, Behave, and Allure**

This repository contains automated tests for eBay using Selenium and Python Behave. The tests are written in Gherkin syntax and can be easily understood by both technical and non-technical stakeholders.

## **Features**

- Automated tests for various eBay functionalities
- Easy-to-understand Gherkin syntax
<!-- - Integration with Selenium for browser automation -->
- Detailed test reports for easy analysis
- Generation of Allure reports for better visualization of test results

## **Prerequisites**

Before running the tests, make sure you have the following installed:

- Python 3.x
- Selenium WebDriver
- Behave
- Allure

## **Installation**

1. Clone the repository: `git clone https://github.com/muhit-khan/eBay_QA_Automation_Python-Selenium-Behave-Allure-BDD.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Set up the test environment:
   - Download the Selenium WebDriver for your browser of choice (e.g., ChromeDriver)
   - Update the `webdriver` variable in `behave.ini` to point to the WebDriver executable
4. Run the tests: `behavebehave -f allure_behave.formatter:AllureFormatter -o reports/ features`
5. View the test reports: `allure serve reports`

## **Running Tests**

To run the tests, navigate to the repository root and execute the following command: `behave -f allure_behave.formatter:AllureFormatter -o reports/ features`

## **Viewing Test Reports**

To view the test reports, navigate to the repository root and execute the following command: `allure serve reports`

This will generate an HTML report that can be accessed in a web browser.

## **License**

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
=======
# **eBay QA Automation with Python, Selenium, Behave, and Allure**

This repository contains automated tests for eBay using Selenium and Python Behave. The tests are written in Gherkin syntax and can be easily understood by both technical and non-technical stakeholders.

## **Features**

- Automated tests for various eBay functionalities
- Easy-to-understand Gherkin syntax
- Integration with Selenium for browser automation
- Detailed test reports for easy analysis
- Generation of Allure reports for better visualization of test results

## **Prerequisites**

Before running the tests, make sure you have the following installed:

- Python 3.x
- Selenium WebDriver
- Behave
- Allure

## **Installation**

1. Clone the repository: `git clone https://github.com/muhit-khan/eBay_QA_Automation_Python-Selenium-Behave-Allure-BDD.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Set up the test environment:
   - Download the Selenium WebDriver for your browser of choice (e.g., ChromeDriver)
   - Update the `webdriver` variable in `behave.ini` to point to the WebDriver executable
4. Run the tests: `behavebehave -f allure_behave.formatter:AllureFormatter -o reports/ features`
5. View the test reports: `allure serve reports`

## **Running Tests**

To run the tests, navigate to the repository root and execute the following command: `behave -f allure_behave.formatter:AllureFormatter -o reports/ features`

## **Viewing Test Reports**

To view the test reports, navigate to the repository root and execute the following command: `allure serve reports`

This will generate an HTML report that can be accessed in a web browser.

![image](https://github.com/muhit-khan/eBay_QA_Automation_Python-Selenium-Behave-Allure-BDD/assets/68416439/f51ed557-600f-49b3-b3a5-97b4ade88d69)


## **License**

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
