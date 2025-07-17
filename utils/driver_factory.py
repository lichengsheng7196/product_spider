from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
import os

def build_driver(headless=False):
    driver_path = os.path.abspath("drivers/msedgedriver.exe")
    edge_options = EdgeOptions()
    if headless:
        edge_options.add_argument("--headless=new")
    edge_options.add_argument("--disable-gpu")
    edge_options.add_argument("--window-size=1280,960")
    service = EdgeService(executable_path=driver_path)
    driver = webdriver.Edge(service=service, options=edge_options)
    return driver
