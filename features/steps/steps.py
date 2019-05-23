from  selenium.common.exceptions import NoSuchElementException

@given('we are connected to the page')
def step(context):
   context.browser.get('http://127.0.0.1:8000/')

@when('we are connected to the page')
def step(context):
   context.browser.get('http://127.0.0.1:8000/')

@then('it should have a title "Word Counter"')
def step(context):
   assert context.browser.title == "Word Counter"

@when('we introduce a valid twitter account')
def step(context):
    elem = context.browser.find_element_by_name("twitter_user")
    elem.clear()
    elem.send_keys("perezreverte")

@when('we click the execute button')
def step(context):
    elem = context.browser.find_element_by_xpath('//*[@id="user-form"]/input[3]')
    elem.click()

@then('we get the most repeated words')
def step(context):
    elem = context.browser.find_element_by_xpath("/html/body/div/h5[1]")

@when('we introduce an invalid account name')
def step(context):
    elem = context.browser.find_element_by_name("twitter_user")
    elem.clear()
    elem.send_keys("perezreverteasdfgh")

@then('we get an error message')
def step(context):
    elem = context.browser.find_element_by_xpath('/html/body/div/h2')
    assert "User not found try with another" == elem.text

@then('we dont get any result')
def step(context):
    try:
        elem = context.browser.find_element_by_xpath("/html/body/div/h5[1]")
        exception = None
    except Exception as ex:
        elem = None
        exception = ex

    assert isinstance(exception, NoSuchElementException)
    #assertRaises(NoSuchElementException, context.browser.find_element_by_xpath("/html/body/div/h5[1]"))

@given('we have searched for a twitter account')
def step(context):
    context.browser.get("http://127.0.0.1:8000/")
    elem = context.browser.find_element_by_name("twitter_user")
    elem.send_keys("perezreverte")
    elem = context.browser.find_element_by_xpath('//*[@id="user-form"]/input[3]')
    elem.click()

@when('we click the clean button')
def step(context):
   elem = context.browser.find_element_by_xpath('//*[@id="user-form"]/a/button')
   elem.click()

@then('the page gets cleaned up')
def step(context):
   assert "User not found try with another." not in context.browser.page_source

   try:
       elem = context.browser.find_element_by_xpath("/html/body/div/h5[1]")
   except:
       return
   assert True == False
