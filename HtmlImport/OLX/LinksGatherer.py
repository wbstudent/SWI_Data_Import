# https://www.olx.pl/nieruchomosci/domy/
# https://www.olx.pl/nieruchomosci/mieszkania/
# https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/
# https://www.olx.pl/nieruchomosci/mieszkania/wynajem
# https://www.olx.pl/nieruchomosci/stancje-pokoje/
# css for single offer
# detailsLinkPromoted
# detailsLink
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
# Parses search page of OLX and copy links to single offers to given file
# https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/?page=   https://www.olx.pl/nieruchomosci/mieszkania/wynajem/?page=
flatsRentLinksFile = './Flats/Rent/Links.txt'
flatRentSaleLinksFile = './Flats/Sale/Links.txt'

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options, executable_path=r'C:\Users\Wiktor\AppData\Local\Gecko\geckodriver.exe')

for pageNumber in range(2, 480):
    driver.get(f"https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/?page={pageNumber}")
    offers = driver.find_elements_by_class_name("detailsLink")
    offers.extend(driver.find_elements_by_class_name("detailsLinkPromoted"))
    links = []
    for offer in offers:
        if offer.text == '':
            continue
        links.append(offer.get_attribute("href"))
    with open(flatRentSaleLinksFile, 'a+') as f:
        f.writelines(link + '\n' for link in links)