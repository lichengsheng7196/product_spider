from utils.driver_factory import build_driver
from utils.yaml_loader import load_config
from flows.taobao_login_flow import TaobaoLoginFlow
from flows.taobao_search_flow import TaobaoSearchFlow

def main():
    config = load_config("configs/keyword_mode.yaml")
    driver = build_driver(config.get("headless", False))

    # 1. 登录淘宝
    if config.get("mode") in ["keyword_search", "shop_search"]:
        login_flow = TaobaoLoginFlow(driver, config.get("phone"))
        login_flow.login()  # 登录后会停留在首页或上次访问页面

    # 2. 关键词搜索
    if config.get("mode") == "keyword_search":
        search_flow = TaobaoSearchFlow(driver, config)
        results = search_flow.run()

        # 3. 保存结果
        import json
        with open("outputs/taobao_search_results.json", "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        print("✅ 搜索结果已保存 outputs/taobao_search_results.json")

    driver.quit()

if __name__ == "__main__":
    main()
