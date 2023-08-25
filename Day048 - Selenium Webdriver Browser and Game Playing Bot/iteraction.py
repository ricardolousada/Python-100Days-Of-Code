from selenium import webdriver
from selenium.webdriver.common.keys import Keys



driver = webdriver.Chrome()

"""
driver.get("https://en.wikipedia.org/wiki/Main_Page")

number = driver.find_element_by_css_selector("#articlecount a")
print(number.text)

# click on an element
#number.click()
wiki_data = driver.find_element_by_link_text("Wikidata")
#wiki_data.click()

# write text in a input label
search = driver.find_element_by_name("search")
search.send_keys("python")
search.send_keys(Keys.ENTER)
"""

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element_by_name("fName")
first_name.send_keys("Ricardo")
first_name.send_keys(Keys.ENTER)

last_name = driver.find_element_by_name("lName")
last_name.send_keys("Lousada")
last_name.send_keys(Keys.ENTER)

email = driver.find_element_by_name("email")
email.send_keys("ricardo.lousada@gmail.com")
email.send_keys(Keys.ENTER)

submit = driver.find_element_by_css_selector("form button")
submit.click()

#driver.quit()