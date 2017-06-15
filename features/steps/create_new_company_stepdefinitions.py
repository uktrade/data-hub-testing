import uuid
import time
from behave import given
from behave import when
from behave import then
from selenium.webdriver.support.select import Select
from features.PageObjects import CompanyDetails
from features.HelperClass.SeleniumDriver import assert_element_is_present
from features.HelperClass.SeleniumDriver import assert_element_is_present_xpath
from features.steps.LoginTestSteps import *


company_name = "Sony"
parent_company_name = "Apple Cake"


@when('I enter CompanyName into Search field')
def enter_companyname_into_search_field(context):
    context.driver.find_element_by_id(CompanyDetails.searchField).send_keys(company_name)


@when('I click search button')
def click_search_link(context):
    context.driver.find_element_by_xpath(CompanyDetails.searchSubmit).click()


@then("I verify the search results display a company")
def verify_search_result_list(context):
    err_msg = "Failed: First company in the list is not displayed, Plz check: "
    assert_element_is_present_xpath(context, CompanyDetails.companyList.format('1'), err_msg)


@then("I verify Create a new company option is displayed")
def verify_create_new_company_button(context):
    err_msg = "Failed: Add New Company button is not displayed, Plz check: "
    assert_element_is_present_xpath(context, CompanyDetails.addNewCompanyButton, err_msg)


@when("I click on Create a new company")
def clickon_create_new_company_button(context):
    context.driver.find_element_by_xpath(CompanyDetails.addNewCompanyButton).click()


@then("I verify possible three radio options displayed")
def verify_different_companies_radiobutton_options(context):
    err_msg = "Failed: '{}' radio button is not displayed, Plz check: "
    assert_element_is_present(context, CompanyDetails.uk_limitedcompany_radiobutton,
                              err_msg.format('UK private or public limited company'))
    assert_element_is_present(context, CompanyDetails.othertypeofukorganisation_radiobutton,
                              err_msg.format('UK private or public limited company'))
    assert_element_is_present(context, CompanyDetails.foreign_organisation_radiobutton,
                              err_msg.format('UK private or public limited company'))


@when("I tick the Foreign Organisation radio button")
def tick_foreign_organisation_option(context):
    #context.driver.window().focus()
    #context.driver.maximize_window()
    context.driver.find_element_by_id(CompanyDetails.foreign_organisation_radiobutton).click()


@when("I tick the other type of UK Organisation radio button")
def tick_other_type_of_UK_organisation_option(context):
    context.driver.find_element_by_id(CompanyDetails.othertypeofukorganisation_radiobutton).click()


@when("I tick the UK private or public limited company radio button")
def tick_UK_private_or_public_limited_company_option(context):
    context.driver.find_element_by_id(CompanyDetails.uk_limitedcompany_radiobutton).click()


@then("I verify Type of Organisation drop down is displayed")
def verify_type_of_organisation_dropdown(context):
    err_msg = "Failed: 'UK private or public limited company' radio button is not displayed, Plz check: "
    assert_element_is_present(context, CompanyDetails.typeOfOrganisation_foreign, err_msg)


@then("I select Company as Type of Organisation")
def select_type_of_organisation(context):
    select = Select(context.driver.find_element_by_id(CompanyDetails.typeOfOrganisation_foreign))
    select.select_by_visible_text('Limited partnership')


@then("I verify Type of Organisation for other type of UK drop down is displayed")
def verify_type_of_organisation_for_other_uk_dropdown(context):
    err_msg = "Failed: 'UK private or public limited company' radio button is not displayed, Plz check: "
    assert_element_is_present(context, CompanyDetails.typeOfOrganisation_other_uk, err_msg)


@then("I select Company as Type of Organisation for other type of UK")
def select_type_of_organisation_for_other_uk(context):
    select = Select(context.driver.find_element_by_id(CompanyDetails.typeOfOrganisation_other_uk))
    select.select_by_visible_text('Limited partnership')


@then("I click on continue button")
def click_continue_button(context):
    context.driver.find_element_by_xpath(CompanyDetails.loginButton).click()


@when("I enter a new {} Company name")
def enter_new_company_name(context, type):
    company_name = 'My {0} company-{1}'.format(type, str(uuid.uuid4())[:8])
    context.driver.find_element_by_id(CompanyDetails.companyName).send_keys(company_name)
    context.company_name = company_name


@when("I enter a Trading name")
def enter_new_trading_name(context):
    alias_name = 'Alias-{1}'.format(type, str(uuid.uuid4())[:8])
    context.driver.find_element_by_id(CompanyDetails.tradingName).send_keys(alias_name)
    context.alias_name = alias_name


@when("I enter Primary address line 1")
def enter_primary_address_line1(context):
    context.driver.find_element_by_id(CompanyDetails.addressLine1).send_keys("Add line 1")


@when("I enter Primary address line 2")
def enter_primary_address_line2(context):
    context.driver.find_element_by_id(CompanyDetails.addressLine2).send_keys("Add line 2")


@when("I enter Primary address town")
def enter_primary_address_town(context):
    context.driver.find_element_by_id(CompanyDetails.town).send_keys("my Town")


@when("I enter Primary address county")
def enter_primary_address_county(context):
    context.driver.find_element_by_id(CompanyDetails.county).send_keys("my County")


@when("I enter Primary address Postcode")
def enter_primary_address_postcode(context):
    context.driver.find_element_by_id(CompanyDetails.postcode).send_keys("POSTCODE")


@when("I select Primary address Country")
def select_primary_address_country(context):
    select = Select(context.driver.find_element_by_id(CompanyDetails.country))
    select.select_by_visible_text('Australia')


@when("I click on Add trading address button")
def click_on_add_trading_address_button(context):
    context.driver.find_element_by_id(CompanyDetails.addTradingAddressButton).click()


@when("I enter trading address line 1")
def enter_trading_address_line1(context):
    context.driver.find_element_by_id(CompanyDetails.tradingAddressLine1).send_keys("Trading Add line 1")


@when("I enter trading address line 2")
def enter_trading_address_line2(context):
    context.driver.find_element_by_id(CompanyDetails.tradingAddressLine2).send_keys("Trading Add line 2")


@when("I enter trading address town")
def enter_trading_address_town(context):
    context.driver.find_element_by_id(CompanyDetails.tradingTown).send_keys("my Trading town")


@when("I enter trading address county")
def enter_trading_address_county(context):
    context.driver.find_element_by_id(CompanyDetails.tradingCounty).send_keys("my Trading county")


@when("I enter trading address Postcode")
def enter_trading_address_postcode(context):
    context.driver.find_element_by_id(CompanyDetails.tradingPostcode).send_keys("TRADE")


@when("I select trading address Country")
def select_trading_address_country(context):
    select = Select(context.driver.find_element_by_id(CompanyDetails.tradingCountry))
    select.select_by_visible_text('Australia')


@when("I select a sector")
def select_a_sector(context):
    # context.driver.find_element_by_xpath(CompanyDetails.sector).click()
    # time.sleep(1)
    # context.driver.find_element_by_xpath(CompanyDetails.sectorItem).click()
    # context.driver.find_element_by_xpath(CompanyDetails.sectorItem).send_keys(u'\ue004')
    pass


@when("I enter a Website")
def enter_a_website(context):
    context.driver.find_element_by_id(CompanyDetails.website).send_keys("https://www.wikipedia.org/")


@when("I enter a Business description")
def enter_a_business_description(context):
    context.driver.find_element_by_id(CompanyDetails.businessDescription).send_keys(
        "Enter some description about your company")


@when("I select Number of employees")
def select_number_of_employees(context):
    select = Select(context.driver.find_element_by_id(CompanyDetails.numberOfEmployees))
    select.select_by_visible_text('10 to 49')


@when("I select Annual turnover")
def select_annual_turnover(context):
    select = Select(context.driver.find_element_by_id(CompanyDetails.annualTurnover))
    select.select_by_index(2)


@when("I click on Save and Create button")
def click_on_save_and_continue_button(context):
    context.driver.find_element_by_xpath(CompanyDetails.loginButton).click()
    #time.sleep(50)


@when("I enter newly created CompanyName into Search field")
def new_companyname_in_searchfield(context):
    context.driver.find_element_by_id(CompanyDetails.searchField).send_keys(context.company_name)


@then("I verify my company is displayed in the search results")
def verify_new_company_in_search_results(context):
    vlue = context.driver.find_element_by_xpath(CompanyDetails.companyListNames).text
    print("My Company name is: {}.".format(vlue))
    assert context.company_name == vlue

def enter_postcode_for_uk_address(context):
    context.driver.find_element_by_xpath(CompanyDetails.primary_uk_postcode).send_keys("EC2Y 9AE")


def click_on_find_my_address_button(context):
    context.driver.find_element_by_xpath(CompanyDetails.primary_find_uk_address).click()


def click_on_uk_address_list(context):
    context.driver.find_element_by_xpath(CompanyDetails.primary_select_an_uk_address_dropdown).click()


def select_uk_address_from_list(context):
    context.driver.find_element_by_xpath(CompanyDetails.primary_select_an_uk_address_from_list).click()
    context.driver.find_element_by_xpath(CompanyDetails.primary_select_an_uk_address_from_list).send_keys(u'\ue004')


def enter_postcode_for_uk_trading_address(context):
    context.driver.find_element_by_xpath(CompanyDetails.primary_uk_postcode.format('trading')).send_keys("EC2Y 9AE")


def click_on_find_my_trading_address_button(context):
    context.driver.find_element_by_xpath(CompanyDetails.primary_find_uk_address.format('trading')).click()


def click_on_uk_trading_address_list(context):
    context.driver.find_element_by_xpath(CompanyDetails.primary_select_an_uk_address_dropdown.format('trading')).click()


def select_uk_trading_address_from_list(context):
    context.driver.find_element_by_xpath(CompanyDetails.primary_select_an_uk_address_from_list.format('trading')).click()
    context.driver.find_element_by_xpath(CompanyDetails.primary_select_an_uk_address_from_list.format('trading')).send_keys(u'\ue004')

def select_uk_region(context):
    select = Select(context.driver.find_element_by_id(CompanyDetails.uk_region))
    select.select_by_index(3)

def enter_parent_companyname_into_search_field(context):
    context.driver.find_element_by_id(CompanyDetails.parent_company_search_field).send_keys(parent_company_name)

def click_on_first_parent_company(context):
    context.driver.find_element_by_xpath(CompanyDetails.parent_company_list).click()

def click_on_choose_parent_company_button(context):
    context.driver.find_element_by_xpath(CompanyDetails.parent_company_choose_button).click()


@when("I create a new Foreign Organisation Company")
def step_impl(context):
    enter_companyname_into_search_field(context)
    click_search_link(context)
    verify_search_result_list(context)
    verify_create_new_company_button(context)
    clickon_create_new_company_button(context)
    verify_different_companies_radiobutton_options(context)
    tick_foreign_organisation_option(context)
    verify_type_of_organisation_dropdown(context)
    select_type_of_organisation(context)
    click_continue_button(context)
    enter_new_company_name(context, 'Foreign')
    #enter_new_trading_name(context)
    enter_primary_address_line1(context)
    enter_primary_address_line2(context)
    enter_primary_address_town(context)
    enter_primary_address_county(context)
    enter_primary_address_postcode(context)
    select_primary_address_country(context)
    click_on_add_trading_address_button(context)
    enter_trading_address_line1(context)
    enter_trading_address_line2(context)
    enter_trading_address_town(context)
    enter_trading_address_county(context)
    enter_trading_address_postcode(context)
    select_trading_address_country(context)
    select_a_sector(context)
    enter_a_website(context)
    enter_a_business_description(context)
    select_number_of_employees(context)
    select_annual_turnover(context)
    click_on_save_and_continue_button(context)


@then("I verify my newly created company in search results")
def step_impl(context):
    navigate_to_datahub_website(context)
    enter_username(context)
    enter_password(context)
    click_login_button(context)
    new_companyname_in_searchfield(context)
    click_search_link(context)
    verify_new_company_in_search_results(context)


@when("I create a new other type of UK Organisation Company")
def step_impl(context):
    enter_companyname_into_search_field(context)
    click_search_link(context)
    verify_search_result_list(context)
    verify_create_new_company_button(context)
    clickon_create_new_company_button(context)
    verify_different_companies_radiobutton_options(context)
    tick_other_type_of_UK_organisation_option(context)
    verify_type_of_organisation_for_other_uk_dropdown(context)
    select_type_of_organisation_for_other_uk(context)
    click_continue_button(context)
    enter_new_company_name(context, 'Other type of UK')
    enter_new_trading_name(context)
    enter_postcode_for_uk_address(context)
    click_on_find_my_address_button(context)
    click_on_uk_address_list(context)
    select_uk_address_from_list(context)
    click_on_add_trading_address_button(context)
    enter_postcode_for_uk_trading_address(context)
    click_on_find_my_trading_address_button(context)
    click_on_uk_trading_address_list(context)
    select_uk_trading_address_from_list(context)
    select_uk_region(context)
    select_a_sector(context)
    enter_a_website(context)
    enter_a_business_description(context)
    select_number_of_employees(context)
    select_annual_turnover(context)
    click_on_save_and_continue_button(context)


@when("I create a new UK private or public limited company")
def step_impl(context):
    enter_companyname_into_search_field(context)
    click_search_link(context)
    verify_search_result_list(context)
    verify_create_new_company_button(context)
    clickon_create_new_company_button(context)
    verify_different_companies_radiobutton_options(context)
    tick_UK_private_or_public_limited_company_option(context)
    click_continue_button(context)
    enter_parent_companyname_into_search_field(context)
    click_search_link(context)
    click_on_first_parent_company(context)
    click_on_choose_parent_company_button(context)
    enter_new_trading_name(context)
    click_on_add_trading_address_button(context)
    enter_postcode_for_uk_trading_address(context)
    click_on_find_my_trading_address_button(context)
    click_on_uk_trading_address_list(context)
    select_uk_trading_address_from_list(context)
    select_uk_region(context)
    select_a_sector(context)
    enter_a_website(context)
    enter_a_business_description(context)
    select_number_of_employees(context)
    select_annual_turnover(context)
    click_on_save_and_continue_button(context)