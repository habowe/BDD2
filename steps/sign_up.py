from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('user is on the sign up page')
def sign_up(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://app.mindlyfe.org/signup/")

@when('user enters credentials')
def validUsernameAndPassword(context):
    context.driver.element(By.NAME, "username").send_keys("hamlet")
    context.driver.element(By.NAME, "email").send_keys("hrubaraza@gmail.com")
    context.driver.element(By.NAME, "password1").send_keys("hamlet123")
    context.driver.element(By.NAME, "password2").send_keys("hamlet123")
    context.driver.element(By.NAME, "submit").click()

@then('Verify Login')
def varify_home(context):
    assert "MindLyfe" == context.driver.title



