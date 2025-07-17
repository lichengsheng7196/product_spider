from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TaobaoSearchPage:
    def __init__(self, driver):
        self.driver = driver

    def open_homepage(self):
        self.driver.get("https://www.taobao.com/")

    def search_input(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "q"))
        )

    def search(self, keyword):
        input_box = self.search_input()
        input_box.clear()
        input_box.send_keys(keyword)
        input_box.send_keys(Keys.ENTER)

    def product_cards(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.items div.item'))
        )
        return self.driver.find_elements(By.CSS_SELECTOR, 'div.items div.item')

    def get_product_info(self, card):
        try:
            title = card.find_element(By.CSS_SELECTOR, '.title').text
            price = card.find_element(By.CSS_SELECTOR, '.price').text
            shop_name = card.find_element(By.CSS_SELECTOR, '.shop').text
            url = card.find_element(By.CSS_SELECTOR, '.pic-link').get_attribute("href")
            return {
                "title": title,
                "price": price,
                "shop_name": shop_name,
                "url": url
            }
        except Exception as e:
            return {"error": str(e)}

    def next_page(self):
        try:
            next_btn = self.driver.find_element(By.CSS_SELECTOR, 'li.item.next a')
            if "disabled" in next_btn.get_attribute("class"):
                return False
            next_btn.click()
            return True
        except Exception:
            return False
