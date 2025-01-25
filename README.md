# Apartment Hunter Application

This project was inspired by Toronto's terrible housing market. It is designed to aggregate over 300 apartments in Toronto into an Excel sheet that can be sorted by most expensive, least expensive, most rooms, and most area. I completed this project using the Python libraries Pandas, Selenium, BeautifulSoup, and Pandas. I hope you can find use in my work like I have!


## Features

- Scrapes online Apartment listings using Selenium and Beautiful soup
- Webdriver waits till all apartments are loaded before scraping
- All listings are put into a pandas data frame with columns "Address", "Link", "Price ($CAD)", "Rooms", "Bathrooms", "Area (ft²)"
- Pandas data frame is then converted to CSV
- Users can choose between sorting the Excel sheet based on rooms, area, and price


## Requirements
- Python 3.x
- Selenium
- Pandas
- Beautiful
- Google Chrome
## Installation



```bash  
  pip3 install selenium
  pip3 install beautifulsoup4
  pip3 install pandas
  Download ChromeDriver here.


```
    
## Screenshots
<img width="1440" alt="AptbyArea" src="https://github.com/user-attachments/assets/a8a2bdb5-f30c-4820-8c35-4fae53bb3e85" />


<img width="1440" alt="terminal" src="https://github.com/user-attachments/assets/4cdcba60-905b-4eee-b990-1f70babebf4c" />


