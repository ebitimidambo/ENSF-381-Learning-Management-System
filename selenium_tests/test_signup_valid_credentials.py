from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

try:
    # Maximize the browser window and open the website
    driver.maximize_window()
    driver.get("http://localhost:3000/")
    sleep(5)

    # Click on the login button to navigate to the login page
    driver.find_element(By.CSS_SELECTOR, "a[href='/login']").click()
    sleep(5)

    # Click on the "Don't have an account? Sign Up" link to navigate to the signup page
    driver.find_element(By.CSS_SELECTOR, "a[href='/signup']").click()
    sleep(2)

    # Verify that the user is redirected to the signup page
    assert driver.current_url == "http://localhost:3000/signup", \
        "Test failed: User did not go to the signup page."
    sleep(2)

    # Enter valid username in the username field
    driver.find_element(By.ID, "username").send_keys("devopsdefender")
    sleep(2)

    # Enter valid email in the email field
    driver.find_element(By.ID, "email").send_keys("ensf519@gmail.com")
    sleep(2)

    # Enter valid password in the password field
    driver.find_element(By.ID, "password").send_keys("P@ssword123!")
    sleep(2)

    # Re-enter valid password in the confirm password field
    driver.find_element(By.ID, "confirm-password").send_keys("P@ssword123!")
    sleep(2)

    # Find signup button and click it
    driver.find_element(By.ID, "signupbutton").click()
    sleep(0.5)

    # Verify that the signup success message is displayed
    success_message = driver.find_element(By.CLASS_NAME, "Success").text
    assert "Success: Signup Successful! Redirecting..." in success_message, \
        "Test failed: Signup was unsuccessful"    
    
    sleep(5)

    # Verify that the user is redirected to the login page after a successful signup
    assert driver.current_url == "http://localhost:3000/login", \
        "Test failed: User did not remain on the login page."

finally:
    # Close the browser after the test is complete
    driver.quit()