from selenium import webdriver
from browserstack.local import Local
import os, json

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


def before_feature(context, feature):
    desired_capabilities = CONFIG['environments'][TASK_ID]

    for key in CONFIG["capabilities"]:
        if key not in desired_capabilities:
            desired_capabilities[key] = CONFIG["capabilities"][key]

    if "browserstack.local" in desired_capabilities and desired_capabilities["browserstack.local"]:
        start_local()

    context.driver = webdriver.Remote(
        desired_capabilities=desired_capabilities,
        command_executor="http://%s:%s@%s/wd/hub" % (BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESS_KEY, CONFIG['server'])
    )

def after_feature(context, feature):
    context.driver.quit()
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