from selenium.webdriver.common.by import By

class TaobaoLoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login_frame(self):
        return self.driver.find_element(By.ID, "J_loginIframe")

    def sms_tab(self):
        # 通过 class 精确定位短信登录 tab
        return self.driver.find_element(By.CSS_SELECTOR, "a.sms-login-tab-item")

    def password_tab(self):
        return self.driver.find_element(By.CSS_SELECTOR, "a.password-login-tab-item")

    def phone_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input#fm-sms-login-id[name='fm-sms-login-id']")

    def code_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input#fm-smscode[name='fm-smscode']")

    def get_code_button(self):
        # 获取验证码按钮为 <a class="send-btn-link">
        return self.driver.find_element(By.CSS_SELECTOR, "a.send-btn-link")

    def submit_button(self):
        # 登录按钮包含 class sms-login 及 type submit
        return self.driver.find_element(By.CSS_SELECTOR, "button.fm-submit.sms-login[type='submit']")

    def keep_login_button(self):
        return self.driver.find_element(By.XPATH, '//button[normalize-space(.)="保持"]')

    def login_link(self):
        # 默认登录页没有"请登录"，故此方法更多用于首页跳转进入iframe
        return self.driver.find_element(By.LINK_TEXT, "请登录")
