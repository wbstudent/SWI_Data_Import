# Removes otodom from links and creates new file without otodom links

flatsRentLinksFile = './Flats/Rent/Links.txt'
flatRentSaleLinksFile = './Flats/Sale/Links.txt'

flatsRentLinksFileWoOtodom = './Flats/Rent/LinksWithoutOtodom.txt'
flatRentSaleLinksFileWoOtodom = './Flats/Sale/LinksWithoutOtodom.txt'

with open(flatRentSaleLinksFile) as file:
    lines = [line if line.find("otodom") == -1 else '' for line in file]
with open(flatRentSaleLinksFileWoOtodom, 'w+') as f:
    f.writelines(line for line in lines)
