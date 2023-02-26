from datetime import time
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    time.sleep(10)
    driver.quit()


#Testcase 1: Successfully sign in using any credentials.
#-----------------
# 1.Open web browser( chrome in this case)
# 2.Open URL https://www.saucedemo.com/
# 3.Provide Username
# 4.Provide Password
# 5.Click on Login
# 6.assert product page (verify)... (Expected result)


def test_TC1(driver):
    driver.get("https://www.saucedemo.com/")
    time.sleep(1)
    driver.maximize_window()
    time.sleep(1)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    time.sleep(1)
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(1)
    driver.find_element(By.ID, "login-button").click()
    assert "https://www.saucedemo.com/inventory.html" in driver.current_url
    time.sleep(5)

#Testcase 2: Login using the following credentials and check (verify with assert) that a error message has been displayed
# #(Credentials: Username-> locked_out_user, Password-> secret_sauce)

# 1.Open web browser( chrome in this case)
# 2.Open URL https://www.saucedemo.com/
# 3.Provide Username as locked_out_user
# 4.Provide Password as secret_sauce
# 5.Click on Login
# 6.assert error message Epic sadface: Sorry, this user has been locked out.

def test_TC2(driver):
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    time.sleep(1)
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    time.sleep(1)
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(1)
    driver.find_element(By.ID, "login-button").click()
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h3[@data-test='error']"))
    )
    assert error_message.text == "Epic sadface: Sorry, this user has been locked out."
    time.sleep(5)

#Testcase 3:

#1.Successfully Login
#2.Navigate to Products page and add Sauce Labs Bolt T-Shirt to basket
#3.Assert that the prices is $15.99
#4.Add Sauce Labs Backpack to the basket
#5.Go to checkout and enter the name and pin
#6.Assert the total price of the order
#7.Finish the order

def test_TC3(driver):
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    time.sleep(1)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    time.sleep(1)
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(1)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(1)

    # Navigate to Products page and add Sauce Labs Bolt T-Shirt to basket
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    time.sleep(1)

    # Assert that the price is $15.99
    price = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[3]/div[2]/div[2]/div")
    assert price.text == "$15.99"

    # Add Sauce Labs Backpack to the basket
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    time.sleep(1)

    # Go to checkout and enter the name and pin
    driver.find_element(By.ID, "shopping_cart_container").click()
    time.sleep(1)
    driver.find_element(By.ID, "checkout").click()
    time.sleep(1)
    driver.find_element(By.ID, "first-name").send_keys("John")
    time.sleep(1)
    driver.find_element(By.ID, "last-name").send_keys("Doe")
    time.sleep(1)
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    time.sleep(1)
    driver.find_element(By.ID, "continue").click()
    time.sleep(1)

    # Assert the total price of the order
    total_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[5]")
    assert total_price.text == "Item total: $45.98"

    # Finish the order
    driver.find_element(By.ID, "finish").click()
    assert "https://www.saucedemo.com/checkout-complete.html" in driver.current_url


if __name__ == "__main__":
    pytest.main(["-v", '--html=report.html'])


