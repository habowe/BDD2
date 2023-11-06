from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('open browser')
def open_browser(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://app.mindlyfe.org/login/?next=/")

@when('providing valid username and password')
def validUsernameAndPassword(context):
    context.driver.element(By.NAME, "username").send_keys("hamlet")
    context.driver.element(By.NAME, "password").send_keys("hamlet123")
    context.driver.element(By.NAME, "submit").click()

@then('Verify Home')
def varify_home(context):
    assert "MindLyfe" == context.driver.title

