from behave import *
from appium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


@given("I am on the login page")
@given("I access to the student management app tc02")
@given("I access the student management app tc03")
@given("I access the student management app tc04")
@given("I access the student management app tc05")
def launch_app(context):
    caps = {
        "automationName": "UiAutomator2",
        "devicedName": "MyPhone57",
        "platformName": "android",
        "appPackage": "com.example.uda_qlsv",
        "appActivity": "com.example.uda_qlsv.MainActivity",
    }
    context.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)

#TC01

@when("I enter valid MSSV and password")
def enter_username_password_tc01(context):
    input_mssv_tc01 = context.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]")
    input_mssv_tc01.click()
    sleep(2)
    input_mssv_tc01.send_keys("44005")

    input_password_tc01 = context.driver.find_element(by=By.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]')
    input_password_tc01.click()
    sleep(2)
    input_password_tc01.send_keys("abc.12345")

@when("I enter wrong MSSV")
def enter_username_password_tc02(context):
    input_mssv_tc02 = context.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]")
    input_mssv_tc02.click()
    sleep(2)
    input_mssv_tc02.send_keys("44000")

    input_password_tc02 = context.driver.find_element(by=By.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]')
    input_password_tc02.click()
    sleep(2)
    input_password_tc02.send_keys("abc.12345")

@when("I enter the correct MSSV - I entered the wrong password")
def enter_username_password_tc03(context):
    input_mssv_tc03 = context.driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]")
    input_mssv_tc03.click()
    sleep(2)
    input_mssv_tc03.send_keys("44005")

    input_password_tc03 = context.driver.find_element(by=By.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]')
    input_password_tc03.click()
    sleep(2)
    input_password_tc03.send_keys("abc.123456")

@when("I enter MSSV")
def enter_mssv_tc04(context):
    input_mssv_tc04 = context.driver.find_element(by=By.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]')
    input_mssv_tc04.click()
    sleep(2)
    input_mssv_tc04.send_keys("44005")

@when("I don't enter the password")
def leave_password_blank_tc04(context):
    input_password_tc04 = context.driver.find_element(by=By.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]')
    input_password_tc04.click()
    sleep(2)

@when("I don't enter MSSV")
def enter_mssv_tc05(context):
    input_mssv_tc05 = context.driver.find_element(by=By.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]')
    input_mssv_tc05.click()
    sleep(2)

@when("I enter the password")
def leave_password_blank_tc05(context):
    input_password_tc05 = context.driver.find_element(by=By.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]')
    input_password_tc05.click()
    sleep(2)
    input_password_tc05.send_keys("abc.12345")

@when("I press the \"ĐĂNG NHẬP\" button")
def click_login(context):
    login_button = context.driver.find_element(by=By.XPATH, value='//android.widget.Button[@content-desc="ĐĂNG NHẬP"]')
    login_button.click()
    sleep(2)


@then("I should see the official page of the app")
def verify_successful_login_tc01(context):
    official_page_tc01 = context.driver.find_element(by=By.XPATH, value='//android.view.View[@content-desc="UDA University"]')
    assert official_page_tc01.is_displayed()

    context.driver.quit()

@then("I won't be able to access the official page of the app and will have an error message \"incorrect MSSV or password\"")
def verify_successful_login_tc03(context):
    error_message_tc03 = context.driver.find_element(by=By.XPATH,value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[2]')
    assert error_message_tc03.is_displayed()
    context.driver.quit()

@then("I won't be able to access the official page of the app and will have an error message \"Lỗi đăng nhập bạn chưa nhập đủ thông tin\"")
def verify_unsuccessful_login_tc04(context):
    error_message = context.driver.find_element(by=By.XPATH,value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[2]')
    assert error_message.is_displayed()
    context.driver.quit()


#     # behave - k login.feature
