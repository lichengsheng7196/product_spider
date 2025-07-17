import yaml
import os
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from flows.taobao_login_flow import TaobaoLoginFlow
from selenium.webdriver.edge.service import Service


def load_config(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def build_driver(headless: bool = False):
    edge_options = Options()
    if headless:
        edge_options.add_argument('--headless')
        edge_options.add_argument('--disable-gpu')
    edge_options.add_argument('--start-maximized')

    driver_path = os.path.join("drivers", "msedgedriver.exe")
    service = Service(executable_path=driver_path)
    driver = webdriver.Edge(service=service, options=edge_options)
    return driver


def main():
    config = load_config("configs/keyword_mode.yaml")
    mode = config.get("mode")
    phone = config.get("phone")
    headless = config.get("headless", False)
    platform = config.get("platforms", ["taobao"])[0]

    driver = build_driver(headless)

    try:
        if mode == "login" and platform == "taobao":
            flow = TaobaoLoginFlow(driver, phone)
            flow.login()

        else:
            print(f"⚠️ 当前 mode [{mode}] 暂不支持或未实现")

    finally:
        input("📌 流程执行完毕，按回车关闭浏览器...")
        driver.quit()


if __name__ == "__main__":
    main()
