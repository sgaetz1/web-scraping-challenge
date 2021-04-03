from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def scrape():
    # get news title and paragraph
    # setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome',**executable_path, headless=False)

    mars = {}

    url = "https://redplanetscience.com"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    mars['title'] = soup.find('div', class_='content_title').get_text()
    mars['paragraph'] = soup.find('div', class_='article_teaser_body').get_text()

    # quit the browser
    browser.quit()

    # get featured image
    # setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url= 'https://spaceimages-mars.com/'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
        
    results = soup.find_all('div', class_="floating_text_area")
        
    for result in results:
        link = result.find('a')
        href = link['href']
        
    featured_image_url = url + href
    mars['featured_image'] = featured_image_url
    
    browser.quit()
    
    # facts table
    url = 'https://galaxyfacts-mars.com/'

    tables = pd.read_html(url)
    df=tables[0]
    df=df.iloc[1:]
    df.columns=['Description','Mars','Earth']
    df=df.set_index('Description')
    html_table=df.to_html()
    html_table.replace('\n', '')
    mars['table'] = html_table

    # hemisphere images and titles

    # setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url= 'https://marshemispheres.com/'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # save links to a list to navigate to each hemisphere page
    links=[]

    results = soup.find_all('div', class_="item")
    for result in results:
        anchor = result.find('a', class_='itemLink')
        href = anchor['href']
        links.append(href)

    browser.quit()

    # setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    titles=[]
    image_urls=[]

    for link in links:
        

        url= 'https://marshemispheres.com/'

        browser.visit(url+link)

        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        results = soup.find_all('div', class_='cover')
    
        for result in results:

            title = result.find('h2', class_="title").text
            titles.append(title)


        images = soup.find_all('div', class_='wide-image-wrapper')

        for image in images:

            img = image.find('img', class_='wide-image')
            image_url = url + img['src'] 
            image_urls.append(image_url)

    browser.quit() 

    both = zip(titles,image_urls)

    hemisphere_image_urls = []
    for title, image in both:
        dictionary = {}
        dictionary['title']=title
        dictionary['image']=image
        hemisphere_image_urls.append(dictionary)  

    mars['hemispheres'] = hemisphere_image_urls

    return mars