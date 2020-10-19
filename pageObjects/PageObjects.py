from selenium.webdriver.support.select import By
class LoginPage():
    usernameTextbox_id = "Email"
    passwordTextbox_id = "Password"
    loginButton_xpath = "//body/div[6]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[3]/input[1]"
    #loginButton_class = "button-1 login-button"

    def __init__(self,driver):
        self.driver = driver
    def enter_username(self,username):
        self.driver.find_element_by_id(self.usernameTextbox_id).clear()
        self.driver.find_element_by_id(self.usernameTextbox_id).send_keys(username)
    def enter_password(self,password):
        self.driver.find_element_by_id(self.passwordTextbox_id).clear()
        self.driver.find_element_by_id(self.passwordTextbox_id).send_keys(password)
    def click_login(self):
        self.driver.find_element_by_xpath(self.loginButton_xpath).click()





