import logging
from behave import given
from behave import when
from behave import then
from features.HelperClass.SeleniumDriver import assert_element_is_present_xpath
from features.PageObjects import CompanyDetails


@given("I am on the Datahub website")
def navigate_to_datahub_website(context):
    logging.debug("Opening the datahub website")
    # context.driver.get("https://www.datahub.staging.uktrade.io/")
    context.driver.get("https://rhod.datahub.dev.uktrade.io/login")


@when('I enter username')
def enter_username(context):
    err_msg = "Failed: Could not find Login button, means login page not loaded completely, Plz check: "
    assert_element_is_present_xpath(context, CompanyDetails.loginButton, err_msg)
    #fill_out_the_login_form(context.driver)
    context.driver.find_element_by_id(CompanyDetails.userName).send_keys(CompanyDetails.email)


@when('I enter password')
def enter_password(context):
    context.driver.find_element_by_id(CompanyDetails.password).send_keys(CompanyDetails.pwd)


@when('I click on Submit button')
def click_login_button(context):
    context.driver.find_element_by_xpath(CompanyDetails.loginButton).click()


@then('I verify user is successfully logged in')
def verify_successful_login(context):
    err_msg = "Failed: User was not logged in successfully, Plz check: "
    assert_element_is_present_xpath(context, CompanyDetails.logoutButton, err_msg)


@given("I am a Authenticated user logged in to datahub website")
def login_to_datahub(context):
    navigate_to_datahub_website(context)
    enter_username(context)
    enter_password(context)
    click_login_button(context)
    verify_successful_login(context)
