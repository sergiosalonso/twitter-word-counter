from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def before_all(context):
    options = Options()
    options.add_argument("--no-sandbox")
    options.headless = True
    options.binary_location = "/usr/bin/google-chrome-stable"
    context.browser = webdriver.Chrome(chrome_options=options, executable_path="/usr/local/bin/chromedriver")

def after_all(context):
	context.browser.quit()
