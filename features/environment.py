from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.config import HEADLESS
import os

def before_all(context):
    options = Options()
    if HEADLESS:
        options.add_argument("--headless")
    context.browser = webdriver.Chrome(executable_path="C:/path/to/chromedriver.exe", options=options)
    if not os.path.exists("reports/screenshots"):
        os.makedirs("reports/screenshots")

def after_step(context, step):
    if step.status == "failed":
        screenshot_path = f"reports/screenshots/{step.name.replace(' ', '_')}.png"
        context.browser.save_screenshot(screenshot_path)
        # Attach screenshot to behave HTML report (if supported)
        if hasattr(context, 'embed'):
            with open(screenshot_path, "rb") as image_file:
                context.embed("image/png", image_file.read())

def after_all(context):
    if hasattr(context, "browser"):
        context.browser.quit()