from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_successful_login_goes_to_the_home_page():
    #Initiating the webdriver
    driver = webdriver.Chrome(executable_path= "drivers/chromedriver.exe")

    #Navigating to the login page
    driver.get("https://www.hudl.com/login")

    #Implicit wait to give the page time to load
    time.sleep(5)

    #Asserting the title of the page matches expecations
    title = driver.title
    assert title == "Log In"

    #Declaring the login page locators we'll be handling
    txtfld_email = driver.find_element(by=By.ID, value="email")
    txtfld_password = driver.find_element(by=By.ID, value="password")
    btn_log_in = driver.find_element(by=By.ID, value="logIn")

    #Populating the email and password and clicking the Log In button
    txtfld_email.send_keys("jbraden@protonmail.com")
    txtfld_password.send_keys("")
    btn_log_in.click()

    #Implicit wait to give the page time to load
    time.sleep(5)

    #Asserting the title of the page matches expectations
    title = driver.title
    assert title == "Home - Hudl"

    #Asserting the user that's supposed to be logged in is
    txt_user_name = driver.find_element(by=By.CLASS_NAME, value="hui-globaluseritem__display-name").text
    assert txt_user_name == 'Justin B'

    #Closing the browser and ending the driver session
    driver.close()
    driver.quit()

def test_invalid_password_will_display_message():
    driver = webdriver.Chrome(executable_path= "drivers/chromedriver.exe")

    driver.get("https://www.hudl.com/login")

    time.sleep(5)

    title = driver.title
    assert title == "Log In"

    txtfld_email = driver.find_element(by=By.ID, value="email")
    txtfld_password = driver.find_element(by=By.ID, value="password")
    btn_log_in = driver.find_element(by=By.ID, value="logIn")

    txtfld_email.send_keys("asdf@asdf.com")
    txtfld_password.send_keys("")
    btn_log_in.click()

    time.sleep(2)

    txtfld_invalid_login_message = driver.find_element(by=By.CLASS_NAME, value="styles_errorDisplayInnerContainer_3R2ni-zSvPIKWfKXiviJhH")
    assert txtfld_invalid_login_message.is_enabled()

    driver.close()
    driver.quit()

def test_hudl_logo_goes_to_the_main_page():
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

def test_left_arrow_goes_to_the_main_page():
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

def test_need_help_goes_to_the_help_page():
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

def test_need_help_from_invalid_log_in_goes_to_the_help_page():
    driver = webdriver.Chrome(executable_path= "drivers/chromedriver.exe")

    driver.get("https://www.hudl.com/login")

    time.sleep(5)

    title = driver.title
    assert title == "Log In"

    btn_log_in = driver.find_element(by=By.ID, value="logIn")
    btn_log_in.click()

    time.sleep(2)

    link_need_help = driver.find_element(by=By.CLASS_NAME, value="uni-margin--quarter--left")
    link_need_help.click()

    time.sleep(5)

    txt_login_help = driver.find_element(by=By.XPATH, value='//h2[@data-qa-id="login-help-headline"]')
    assert txt_login_help.is_displayed()

    driver.close()
    driver.quit()

def test_clicking_log_in_with_an_organization_goes_to_the_organization_page():
    driver = webdriver.Chrome(executable_path= "drivers/chromedriver.exe")

    driver.get("https://www.hudl.com/login")

    time.sleep(5)

    title = driver.title
    assert title == "Log In"

    btn_log_in = driver.find_element(by=By.XPATH, value='//button[@data-qa-id="log-in-with-organization-btn"]')
    btn_log_in.click()

    time.sleep(5)

    btn_log_in_with_email_and_password = driver.find_element(by=By.XPATH, value='//button[@data-qa-id="log-in-with-email-and-password"]')
    assert btn_log_in_with_email_and_password.is_displayed()

    driver.close()
    driver.quit()

def test_clicking_sign_up_goes_to_the_sign_up_page():
    driver = webdriver.Chrome(executable_path= "drivers/chromedriver.exe")

    driver.get("https://www.hudl.com/login")

    time.sleep(5)

    title = driver.title
    assert title == "Log In"

    btn_sign_up = driver.find_element(by=By.CLASS_NAME, value="styles_signUpLink_1CPc8TbK9yDyBdJiSpUOZV")
    btn_sign_up.click()

    time.sleep(5)

    link_high_schools = driver.find_element(by=By.ID, value="register_demo")
    link_high_schools.is_displayed()

    driver.close()
    driver.quit()
