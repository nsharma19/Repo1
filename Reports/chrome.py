from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())  # Optional argument, if not specified will search path.
driver.get('https://www.google.com/')
