class LoginPage():
    usernameTextbox_id = "Email"
    passwordTextbox_id = "Password"
    loginButton_xpath = "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/input"
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



