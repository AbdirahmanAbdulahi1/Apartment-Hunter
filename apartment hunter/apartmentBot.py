from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import  NoSuchElementException
from bs4 import BeautifulSoup
import time
import pandas as pd

# Set up Selenium with headless Chrome This allows processes to run in the backroung
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

# URL of the page
url = "https://www.theblueground.com/furnished-apartments-toronto-canada"
driver.get(url)

# Wait and click "Show More" buttons to load all listings
start_time = time.time()
timeout = 60
while time.time() - start_time < timeout:
    try:
        # Wait for the "Show More" button to be clickable
        show_more_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "ui-button__ghost"))
        )
        show_more_button.click()
        time.sleep(2)  # Allow some time for new listings to load

    except NoSuchElementException:
        print("No more 'Show More' button found. All listings are loaded.")
        break

# Parse the fully loaded page with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')
listings = soup.find_all('a', class_='property')

# Creating our Pandas Dataframe.
df = pd.DataFrame(columns= ["Address", "Link", "Price ($CAD)", "Rooms", "Bathrooms","Area (ft²)"])

#Loops over all the listings, get their details and turn it into dictionary
#we then add each dictionary
rows = []
for apt in listings:
    link = "https://www.theblueground.com" + apt.get('href')
    price_element = apt.find('span', class_="price__amount")
    if price_element:
        price = price_element.text.strip()
        if ',' in price:
            pre, sep, post = price.partition(',')
            price = pre + post
    else:
        price = "N/A"
    name_element = apt.find('span', class_="property__name-address")
    if name_element:
        name = name_element.text.strip()
    else:
        name = "N/A"
    ameneties = apt.find_all('div', class_='listing-amenities__amenity')
    rooms = ameneties[0].find('span').text
    bathrooms = ameneties[1].find('span').text[0]
    if (len(ameneties) >2):
        areaNmetric = ameneties[2].find('span').text
        area, sep, metric = areaNmetric.partition(' ')
        if ',' in area:
            pre, sep, post = area.partition(',')
            area = pre + post

    else:
        area = "N/A"
    rows.append({
        "Address": name,
        "Link": link,
        "Price ($CAD)": price,
        "Rooms": rooms,
        "Bathrooms": bathrooms,
        "Area (ft²)": area
    })


df = pd.concat([df, pd.DataFrame(rows)], ignore_index=True)


driver.quit()
