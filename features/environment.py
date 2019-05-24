from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def before_all(context):
    options = Options()
    options.add_argument("--no-sandbox")
    options.binary_location = "/usr/bin/google-chrome-stable"
    options.headless = True
    context.browser = webdriver.Chrome(chrome_options=options, executable_path=ChromeDriverManager().install())



def after_all(context):
	context.browser.quit()
