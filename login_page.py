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

def test_hudl_logo_goes_to_main_page():
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

def test_left_arrow_goes_to_main_page():
    driver = webdriver.Chrome(executable_path= "drivers/chromedriver.exe")

    driver.get("https://www.hudl.com/login")

    time.sleep(5)

    title = driver.title
    assert title == "Log In"

    link_left_arrow = driver.find_element(by=By.CLASS_NAME, value="styles_backIconContainer_MhkioW9m8rx70X7CIGuws")

    link_left_arrow.click()

    time.sleep(5)

    btn_log_in = driver.find_element(by=By.CLASS_NAME, value="mainnav__item--expandable")
    assert btn_log_in.is_enabled()

    driver.close()
    driver.quit()

def test_need_help_goes_to_help_page():
    driver = webdriver.Chrome(executable_path= "drivers/chromedriver.exe")

    driver.get("https://www.hudl.com/login")

    time.sleep(5)

    title = driver.title
    assert title == "Log In"

    link_need_help = driver.find_element(by=By.LINK_TEXT, value="Need help?")

    link_need_help.click()

    time.sleep(5)

    txt_login_help = driver.find_element(by=By.XPATH, value='//h2[@data-qa-id="login-help-headline"]')

    assert txt_login_help.is_displayed()

    driver.close()
    driver.quit()
