import pytest
from selenium import webdriver
@pytest.fixture()
def setup():
    driver = webdriver.Chrome(executable_path="C:/Users/Owner/Desktop/chromedriver/chromedriver.exe")
    return driver