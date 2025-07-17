import time
from pages.taobao_search_page import TaobaoSearchPage

class TaobaoSearchFlow:
    def __init__(self, driver, config):
        self.driver = driver
        self.config = config
        self.page = TaobaoSearchPage(driver)

    def run(self):
        keywords = self.config.get("keywords", [])
        pages = self.config.get("pages", 1)
        all_results = []

        for keyword in keywords:
            print(f"🔍 搜索关键词: {keyword}")
            self.page.open_homepage()
            self.page.search(keyword)
            time.sleep(2)
            for page_idx in range(pages):
                print(f"  📄 正在抓取第 {page_idx + 1} 页")
                cards = self.page.product_cards()
                for idx, card in enumerate(cards):
                    info = self.page.get_product_info(card)
                    print(f"    - 商品{idx+1}: {info.get('title', '无标题')}")
                    all_results.append(info)
                if page_idx < pages - 1 and not self.page.next_page():
                    print("  🚩 已到最后一页")
                    break
                time.sleep(2)
        return all_results
