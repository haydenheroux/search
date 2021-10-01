from selenium import webdriver
import requests
import logging

def get(url):
    response = requests.get(url)
    code = response.status_code
    if code != 200:
        logging.error("Non-200 status code {} returned from {}.".format(code, url))
        return
    return response.content.decode('utf-8')


def manual(url, class_):
    driver = webdriver.Firefox()
    driver.get(url)
    content = driver.find_elements_by_class_name(class_)
    return (driver, content)
