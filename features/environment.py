from behave.fixture import use_fixture_by_tag
from selenium import webdriver
import os
from configparser import ConfigParser
from selenium.webdriver.common.keys import Keys
import time
from behave.fixture import use_fixture_by_tag
from helper.helper_web import get_browser

caps = {}

def before_all(context):
    caps['browserName'] = context.config.userdata['browser']
    caps['version'] = context.config.userdata['browser_version']
    # To ensure that the same test runs on multiple platforms,
    # platform is read from the environment variable that is added
    # in the YAML file
    # caps['platform'] = context.config.userdata['platform']

    helper_func = get_browser(caps['browserName'], caps['version'])
    context.helperfunc = helper_func

def after_all(context):
    context.helperfunc.close()
