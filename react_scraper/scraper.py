from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def scrape(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")  # new headless mode, more stable
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")

    # No Service() or ChromeDriverManager() needed — Selenium manages it
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        time.sleep(5)

        title = driver.find_element(By.TAG_NAME, "h1").text
        paragraphs = driver.find_elements(By.TAG_NAME, "p")
        content = "\n".join([p.text for p in paragraphs if p.text.strip()])

        return {"title": title, "content": content}
    finally:
        driver.quit()

if __name__ == '__main__':
    
    url = 'https://www.netflix.com/in/'
    scrape = scrape(url)

    print(scrape['title'])
    print(scrape['content'])