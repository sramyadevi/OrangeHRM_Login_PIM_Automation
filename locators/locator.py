class Locator:
    def __init__(self, username_field):
        self.username_field = username_field

    def all_locators(self, username):
        username_field = "//input[@name='username']"
        password_field = "//input[@name='password']"
        submit_field = "//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']"
