# https://www.olx.pl/nieruchomosci/domy/
# https://www.olx.pl/nieruchomosci/mieszkania/
# https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/
# https://www.olx.pl/nieruchomosci/mieszkania/wynajem
# https://www.olx.pl/nieruchomosci/stancje-pokoje/

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
opts = Options()
opts.set_headless()
assert opts.headless  # Operating in headless mode
browser = Firefox(options=opts)
browser.get('https://duckduckgo.com')