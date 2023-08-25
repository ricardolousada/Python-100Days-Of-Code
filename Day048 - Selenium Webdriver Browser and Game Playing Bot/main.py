# Created by Ricardo Lousada
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://python.org")
"""
search_bar= driver.find_element_by_name("q")
print(search_bar.get_attribute("placeholder"))
logo = driver.find_element_by_class_name("python-logo")
print(logo.size)
documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
print(documentation_link.text)
submit_bug = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(submit_bug.text)
"""
# driver.close() - Close the current tab
# - Closes all windows

events = {}
event_times = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "event": event_names[n].text
    }

print(events)
driver.quit()