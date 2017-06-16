# # -*- coding: utf-8 -*-
# """Behave configuration file."""

from selenium import webdriver
from browserstack.local import Local
import os, json
import logging
from features.utils import init_loggers

CONFIG_FILE = os.environ['CONFIG_FILE'] if 'CONFIG_FILE' in os.environ else 'config/single.json'
TASK_ID = int(os.environ['TASK_ID']) if 'TASK_ID' in os.environ else 0

with open(CONFIG_FILE) as data_file:
    CONFIG = json.load(data_file)

bs_local = None

BROWSERSTACK_USERNAME = os.environ['BROWSERSTACK_USERNAME'] if 'BROWSERSTACK_USERNAME' in os.environ else CONFIG['user']
BROWSERSTACK_ACCESS_KEY = os.environ['BROWSERSTACK_ACCESS_KEY'] if 'BROWSERSTACK_ACCESS_KEY' in os.environ else CONFIG['key']

def start_local():
    """Code to start browserstack local before start of test."""
    global bs_local
    bs_local = Local()
    bs_local_args = { "key": BROWSERSTACK_ACCESS_KEY, "forcelocal": "true" }
    bs_local.start(**bs_local_args)

def stop_local():
    """Code to stop browserstack local after end of test."""
    global bs_local
    if bs_local is not None:
        bs_local.stop()


def get_local_firefox_driver():
    geckopath = 'C:\\Users\\Venu\\PycharmProjects\\DataHub_DIT\\bin\\geckodriver.exe'
    driver = webdriver.Firefox(executable_path=geckopath)
    driver.maximize_window()
    driver.implicitly_wait(30)
    return driver


def get_browserstack_driver(server, username, accesskey):
    desired_capabilities = {"build": "behave-browserstack",
                            "name": "local_test",
                            "browserstack.debug": True}
    start_local()
    driver = webdriver.Remote(
        desired_capabilities=desired_capabilities,
        command_executor="http://%s:%s@%s/wd/hub" % (username, accesskey, server)
    )
    return driver


def get_driver():
    """Get Local or BrowserStack Selenium Driver based on the environment variable "ENVIRONMENT"

    NOTE:
    Will use local driver if that variable is not set.

    :return: a tuple consisting of Selenium Driver and name of the environment
    """
    # Use local by default
    environment = os.environ.get("ENVIRONMENT", "local").strip()
    assert environment in ["local", "browserstack"], ("Could not recognize ENVIRONMENT: '{}'".format(environment))
    driver = None

    logging.debug("Running tests using {} environment".format(environment))

    if environment == "local":
        logging.debug("Running tests locally")
        driver = get_local_firefox_driver()
    elif environment == "browserstack":
        print("Running tests on Browserstack")
        logging.debug("Running tests on Browserstack")
        assert "BROWSERSTACK_SERVER" in os.environ
        assert "BROWSERSTACK_USERNAME" in os.environ
        assert "BROWSERSTACK_ACCESS_KEY" in os.environ
        driver = get_browserstack_driver(os.environ.get("BROWSERSTACK_SERVER").strip(),
                                         os.environ.get("BROWSERSTACK_USERNAME").strip(),
                                         os.environ.get("BROWSERSTACK_ACCESS_KEY").strip())
    else:
        raise KeyError("Could not recognize the environment: {}".format(environment))

    return (driver, environment)


def before_feature(context, feature):
    context.driver, context.environment = get_driver()


def after_feature(context, feature):
    context.driver.quit()
    if context.environment == "browserstack":
        stop_local()



# # -*- coding: utf-8 -*-
# """Behave configuration file."""
# import logging
# from selenium import webdriver
# from features.utils import init_loggers
#
#
# def before_step(context, step):
#     logging.debug('Step: {} {}'.format(step.step_type, str(repr(step.name))))
#
#
# def after_step(context, step):
#     if step.status == "failed":
#         msg = 'Step "{} {}" has failed. Reason: "{}".'.format(
#             step.step_type, step.name, step.exception)
#         logging.debug(msg)
#         context.driver.get_screenshot_as_png()
#
#
# def before_scenario(context, scenario):
#     logging.debug('Starting scenario: {}'.format(scenario.name))
#     geckopath = 'C:\\Users\\Venu\\PycharmProjects\\DataHub_DIT\\bin\\geckodriver.exe'
#     context.driver = webdriver.Firefox(executable_path=geckopath)
#     context.driver.maximize_window()
#     context.driver.implicitly_wait(30)
#
#
# def after_scenario(context, scenario):
#     # clear the scenario data after every scenario
#     context.scenario_data = None
#     logging.debug('Finished scenario: {}'.format(scenario.name))
#     context.driver.quit()
#
#
# def before_all(context):
#     init_loggers()