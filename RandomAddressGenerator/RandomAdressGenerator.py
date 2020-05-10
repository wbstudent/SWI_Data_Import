import csv
import random
import os
# Generates address for given city using data from http://eteryt.stat.gov.pl/eTeryt/rejestr_teryt/udostepnianie_danych/baza_teryt/uzytkownicy_indywidualni/pobieranie/pliki_pelne.aspx?contrast=default
# Data initialization
# SIMC - potrzebny do wzięcia nazwy miejscowości oraz jej symbolu do pliku z ulicami
#   WOJ, POW, GMI jak niżej
#   NAZWA - nazwa miejscowości
#   SYM - identyfikator miejscowości
#
# TERC - potrzebny do zdefiniowania nazw województw, powiatów, gmin użytych w innych plikach
    #   WOJ - symbol województwa
    #   POW - symbol powiatu
    #   GMI 0 symbol gminy
    #   NAZWA - nazwa danej rzeczy, jeśli 3 wypełnione - gminy, jeśli 2 wypełnione, a 3 puste - powiatu, jeśli tylko 1 wypełnione - województwa

# ULIC
    # WOJ, POW, GMI jak wyżej
    # SYM - identyfikator miejscowości
    # NAZWA_1
    # NAZWA_2 - trzeba skleć

def getCitySymbolByCityName():
    citysymbolbycityname = {}
    fileName = os.path.join(os.path.dirname(__file__), 'SIMC_Urzedowy_2020-05-10.csv')
    with open(fileName, 'r', encoding="UTF-8") as file:
        csv_file = csv.DictReader(file, delimiter=";")
        for row in csv_file:
            nazwa = row['NAZWA']
            symbol = str(int(row['SYM']))
            citysymbolbycityname[nazwa] = symbol
    return citysymbolbycityname

def getCityNameByCitySymbol():
    cityNameByCitySymbol = {}
    fileName = os.path.join(os.path.dirname(__file__), 'SIMC_Urzedowy_2020-05-10.csv')
    with open(fileName, 'r', encoding="UTF-8") as file:
        csv_file = csv.DictReader(file, delimiter=";")
        for row in csv_file:
            nazwa = row['NAZWA']
            symbol = str(int(row['SYM']))
            cityNameByCitySymbol[symbol] = nazwa
    return cityNameByCitySymbol


def getCityInfoAndStreetsByCitySymbol():
    cityinfoandstreetsbycitysymbol = {}
    fileName = os.path.join(os.path.dirname(__file__), 'ULIC_Urzedowy_2020-05-10.csv')
    with open(fileName, 'r', encoding="UTF-8") as file:
        csv_file = csv.DictReader(file, delimiter=";")
        for row in csv_file:
            ulica = row['CECHA']
            if ulica != 'ul.':
                continue
            nazwa = ulica + ' ' + row['NAZWA_1'] + ' ' + row['NAZWA_2']
            symbol = str(int(row['SYM']))
            wojewodztwo = str(int(row['\ufeffWOJ']))
            # powiat = row['POW']
            # gmina = row['GMI']
            if symbol not in cityinfoandstreetsbycitysymbol.keys():
                cityinfoandstreetsbycitysymbol[symbol] = {'woj': wojewodztwoBySymbol[wojewodztwo],
                                                          # 'pow': powiat,
                                                          # 'gmi': gmina,
                                                          'streets': [nazwa]}
            else:
                cityinfoandstreetsbycitysymbol[symbol]['streets'].append(nazwa)
    for key in list(cityinfoandstreetsbycitysymbol.keys()):
        if cityinfoandstreetsbycitysymbol[key]['streets'] is None:
            cityinfoandstreetsbycitysymbol.pop(key)
    return cityinfoandstreetsbycitysymbol

wojewodztwoBySymbol = {"2": "dolnośląskie",
                       "4": "kujawsko-pomorskie",
                       "6": "lubelskie",
                       "8": "lubuskie",
                       "10": "łódzkie",
                       "12": "małopolskie",
                       "14": "mazowieckie",
                       "16": "opolskie",
                       "18": "podkarpackie",
                       "20": "podlaskie",
                       "22": "pomorskie",
                       "24": "śląskie",
                       "26": "świętokrzyskie",
                       "28": "warmińsko-mazurskie",
                       "30": "wielkopolskie",
                       "32": "zachodniopomorskie"
                       }
citySymbolByCityName = getCitySymbolByCityName()
cityNameByCitySymbol = getCityNameByCitySymbol()
CITYINFOANDSTREETSBYCITYSYMBOL = getCityInfoAndStreetsByCitySymbol()

def getRandomCityFromList():
    return random.choice(list(citySymbolByCityName.values()))

# generates address in given city if passed as parameter, otherwise random city is used
def generateRandomAddress(cityName):
    try:
        if cityName == '' or citySymbolByCityName.get(cityName) is None:
            cityName = getRandomCityFromList()
        citySymbol = citySymbolByCityName.get(cityName)

        cityInfo = CITYINFOANDSTREETSBYCITYSYMBOL.get(citySymbol)
        if cityInfo is None: # happens, randomize
            citySymbol = random.choice(list(CITYINFOANDSTREETSBYCITYSYMBOL.keys()))
            cityName = cityNameByCitySymbol[citySymbol]
            cityInfo = CITYINFOANDSTREETSBYCITYSYMBOL[citySymbol]
        return {
            "city": cityName,
            "voivodeship": cityInfo['woj'],
            "street": random.choice(cityInfo['streets']),
            "houseNumber": random.randint(1, 145),
            "apartmentNumber": random.randint(1, 145)
        }
    except Exception as e:
        print(e)
        return {
            "city": '',
            "voivodeship": '',
            "street": '',
            "houseNumber": -1,
            "apartmentNumber": -1
        }
