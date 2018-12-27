# TicketPriceScrapper

Quick code to scrap tickets prices in a specific date, in a specific route, from the website MelhoresDestinos.

In order to the code to work properly you have to install the following libraries: 
- selenium
- BeautifulSoup 
- requests
- html5lib
- pandas 

And you need to place the file chromedriver.exe into the same folder where the script is being processed.

For everytime you want to save the prices for a given date you need to:
1) Run 1_Scrapping.py
2) Run 2_Parsing.py

Open Prices.csv whenever you want to check the prices database.