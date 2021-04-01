from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

def scrape():

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome',**executable_path, headless=False)

    news = {}

    url = "https://redplanetscience.com"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    news['title'] = soup.find('div', class_='content_title').get_text()
    news['paragraph'] = soup.find('div', class_='article_teaser_body').get_text()

    # quit the browser
    browser.quit()

    return news