from selenium.common.exceptions import NoSuchElementException

django_admin_url_staging = "http://leeloo.datahub.staging.uktrade.io/admin/company/company/"
django_admin_url_dev = "http://leeloo.datahub.dev.uktrade.io/admin/company/company/"


def assert_element_is_present_xpath(context, selector, err_msg):
    try:
        context.driver.find_element_by_xpath(selector)
    except NoSuchElementException:
        assert False, err_msg

def assert_element_is_present(context, selector, err_msg):
    try:
        context.driver.find_element_by_id(selector)
    except NoSuchElementException:
        assert False, err_msg
