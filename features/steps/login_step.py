from behave import given, when, then
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from numpy.testing import assert_equal

# locators and variables
url_link = "http://www.uitestingplayground.com/sampleapp"
user_locator = "//body[1]/section[1]/div[1]/div[2]/div[1]/input[1]"
password_locator = "//body[1]/section[1]/div[1]/div[3]/div[1]/input[1]"
button_locator = "login"
message_locator = "loginstatus"
expected_message = "Welcome, username!"


@given(u'the user navigates to the url')
def step_impl(context):
	context.driver = webdriver.Chrome(ChromeDriverManager().install())
	driver = context.driver
	driver.get(url_link)
	driver.implicitly_wait(10)
	driver.maximize_window()


@when(u'he enters the "{user}" and "{pwd}"')
def step_impl(context, user, pwd):
	driver = context.driver
	username_input = driver.find_element_by_xpath(user_locator).send_keys(user)
	password_input = driver.find_element_by_xpath(password_locator).send_keys(pwd)


@when(u'clicks on the submit button below')
def step_impl(context):
	driver = context.driver
	button_submit = driver.find_element_by_id(button_locator).click()


@then(u'he must see a welcome message')
def step_impl(context):
	driver = context.driver
	message_submit = driver.find_element_by_id(message_locator).text
	assert_equal(message_submit, expected_message)
	driver.close()
