from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_successful_login():
    driver = webdriver.Chrome(executable_path= "drivers/chromedriver.exe")

    driver.get("https://www.hudl.com/login")

    time.sleep(5)

    title = driver.title
    assert title == "Log In"

    txtfld_email = driver.find_element(by=By.ID, value="email")
    txtfld_password = driver.find_element(by=By.ID, value="password")
    btn_log_in = driver.find_element(by=By.ID, value="logIn")

    txtfld_email.send_keys("jbraden@protonmail.com")
    txtfld_password.send_keys("techInterview1")
    btn_log_in.click()

    time.sleep(5)

    title = driver.title
    assert title == "Home - Hudl"

    driver.close()
    driver.quit()

def test_invalid_email_will_display_message():
    driver = webdriver.Chrome(executable_path= "drivers/chromedriver.exe")

    driver.get("https://www.hudl.com/login")

    time.sleep(5)

    title = driver.title
    assert title == "Log In"

    txtfld_email = driver.find_element(by=By.ID, value="email")
    txtfld_password = driver.find_element(by=By.ID, value="password")
    btn_log_in = driver.find_element(by=By.ID, value="logIn")

    txtfld_email.send_keys("asdf@asdf.com")
    txtfld_password.send_keys("techInterview1")
    btn_log_in.click()

    time.sleep(2)

    txtfld_invalid_login_message = driver.find_element(by=By.CLASS_NAME, value="styles_errorDisplayInnerContainer_3R2ni-zSvPIKWfKXiviJhH")
    assert txtfld_invalid_login_message.is_enabled()

    driver.close()
    driver.quit()

def test_hudl_logo_goes_to_home():
    driver = webdriver.Chrome(executable_path= "drivers/chromedriver.exe")

    driver.get("https://www.hudl.com/login")

    time.sleep(5)

    title = driver.title
    assert title == "Log In"

    svg_hudl_logo = driver.find_element(by=By.CLASS_NAME, value="styles_hudlLogoContainer_1L8Lig-sH69T84pB_fXSlv")

    svg_hudl_logo.click()

    time.sleep(5)

    btn_log_in = driver.find_element(by=By.CLASS_NAME, value="mainnav__item--expandable")
    assert btn_log_in.is_enabled()

    driver.close()
    driver.quit()

