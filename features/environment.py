from selenium import webdriver

def before_all(context):
    context.browser = webdriver.Chrome('/Users/weeto/Downloads/chromedriver')

def after_all(context):
	context.browser.quit()
