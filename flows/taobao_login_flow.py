import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.taobao_login_page import TaobaoLoginPage


class TaobaoLoginFlow:
    LOGIN_URL = "https://login.taobao.com/havanaone/login/login.htm?bizName=taobao"

    def __init__(self, driver, phone):
        self.driver = driver
        self.phone = phone
        self.page = TaobaoLoginPage(driver)

    def wait_for(self, element_fn, timeout=10, condition=EC.element_to_be_clickable):
        """统一封装等待某元素加载可操作"""
        return WebDriverWait(self.driver, timeout).until(condition(element_fn()))

    def login(self):
        self.driver.get(self.LOGIN_URL)

        # 1. 等待并点击“短信登录”Tab（默认可能为密码登录）
        self.wait_for(self.page.sms_tab).click()

        # 2. 输入手机号
        self.wait_for(self.page.phone_input, condition=EC.visibility_of).send_keys(self.phone)

        # 3. 点击“获取验证码”按钮
        self.wait_for(self.page.get_code_button).click()

        # 4. 命令行等待验证码
        verify_code = input("📩 请输入你手机收到的验证码：")

        # 5. 输入验证码
        self.wait_for(self.page.code_input).send_keys(verify_code)
        time.sleep(0.5)

        # 6. 点击“登录”按钮
        self.wait_for(self.page.submit_button).click()

        # 检查并点击“保持登录”
        try:
            hold_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.page.keep_login_button())
            )
            hold_button.click()
            print("✅ 点击了“保持登录”按钮")
        except Exception:
            print("⚠️ 未检测到“保持登录状态”弹窗，可能已自动关闭")

        # 7. 等待跳转完成
        time.sleep(3)
        print("✅ 登录流程执行完毕")
