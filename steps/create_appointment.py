from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('user is on appointment page')
def start_appointment(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://app.mindlyfe.org/create/")

@when('user enters appointment details')
def create_appointment(context):
    context.driver.element(By.NAME, "choose_therapist").send_keys("leon")
    context.driver.element(By.NAME, "date").send_keys("2023-11-06")
    context.driver.element(By.NAME, "time").send_keys("5:45 AM")
    context.driver.element(By.NAME, "payment_number").send_keys("077777777")
    context.driver.element(By.NAME, "health_concern").send_keys("time management")
    context.driver.element(By.NAME, "create_button").click()

@then('Verify Appointment')
def varify_appointment(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://app.mindlyfe.org/user_appointments/")
