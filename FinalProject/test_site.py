from ui_helper import OperationsHelper
import logging
import yaml, time

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

name = testdata.get("username")
passw = testdata.get("password")


def test_step1(browser):
    logging.info("Test 1 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("PASSWORD")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"

def test_step2(browser):
    logging.info("Test 2 Starting")
    testpage = OperationsHelper(browser)
    testpage.enter_login(name)
    testpage.enter_pass(passw)
    testpage.click_login_button()
    assert testpage.get_user_text() == f"Hello, {name}"

def test_step3(browser):
    logging.info("Test 3 Starting")
    testpage = OperationsHelper(browser)
    testpage.click_about()
    time.sleep(5)
    assert testpage.get_about_text() == ("About Page")
    assert testpage.get_about_property() == "32px"

