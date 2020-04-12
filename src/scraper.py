import argparse
import requests
from bs4 import BeautifulSoup
import pandas as pd


def getAllCryptos():
    elementList = []
    response = requests.get('https://coinmarketcap.com/coins/')
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.findAll('table')[2]
    index = 0
    for row in table.findAll("tr"):
        if (index > 0):
            columns = row.findAll("td")
            cryptoUrl = columns[1].find('a')['href'].split('/')[2]
            elementList.append(cryptoUrl)
        index += 1
    return elementList
    

def getExchangePrices(crypto) :
    elementList = []  
    url = "https://coinmarketcap.com/currencies/{crypto}/markets/".format(crypto=crypto)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    table = soup.findAll('table')[2]
    index = 0
    for row in table.findAll("tr"):
        if (index > 0):
            columns = row.findAll("td")
            if (columns[2].find(text=True).endswith("/USD".format(crypto=crypto))):
                exchange = columns[1].find('a')['title']
                price=float(columns[4].find(text=True).split("$")[1].replace(',',''))
                element=[exchange,price]
                elementList.append(element)
        index += 1
    return elementList


def main():
    availableCryptos = getAllCryptos()

    parser = argparse.ArgumentParser()
    parser.add_argument('--filter', type=str, nargs='*', help="USAGE: --filter " + " ".join(availableCryptos))
    args=parser.parse_args()

    cryptoList = []
    if args.filter:
        if (len(args.filter) <= 8):
            for crypto in args.filter:
                if (crypto in availableCryptos):
                    cryptoList.append(crypto)
                else:
                    print("Not found: " + crypto)
        else:
            raise argparse.ArgumentTypeError("Too many arguments, max 8")

    else:
        cryptoList = ['bitcoin', 'ethereum', 'dash', 'litecoin', 'bitcoin-cash']

    print('Scrapping...')
    df = pd.DataFrame()
    for crypto in cryptoList:
        elements = getExchangePrices(crypto)
        auxDf = pd.DataFrame(elements, columns=["exchange", crypto+"-USD"])
        if (df.empty):
            df = auxDf
        else:
            df = pd.merge(left=df, right=auxDf, on="exchange", how="outer")
    
    df.to_csv(r'csv/dataframe.csv', index=False, header=True)
    print('Done!')


if __name__ == "__main__":
    main()
