# CoinMarketCap Scraper
This Python script obtains and exports to CSV a dataframe formed by the current price of up to 8 user-selected cryptocurrencies from different Exchanges, obtained by scraping [CoinMarketCap](https://coinmarketcap.com) site.


## Dependencies
It is necessary to have installed the following python modules:
```
pip install argparse
pip install beautifulsoup4
pip install pandas
pip install requests
```


## Run
In order to run the script with the default parameters execute the following command:
```
python scraper.py
```
It will be exported a dataframe containing the last updated prices in every exchange available in [CoinMarketCap](https://coinmarketcap.com) for the default cryptocurrencies: Bitcoin, Ethereum, Dash, Litecoin, Bitcoin Cash
The result file is exported in:
```
csv/dataframe.csv
```

### Optional parameters
For customizing the dataframe and obtaining a dataframe with up to 8 cryptocurrencies use the 'filter' argument.
```
python scraper.py --filter crypto1 crypto2... cryptoX
```

Example:
```
python scraper.py --filter ethereum bitcoin-cash
```
It will export a dataframe with the current price of Bitcoin and Bitcoin Cash for each Exchange.

The supported cryptocurrency list as well as their corresponding argument name can be checked by executing:
```
python scraper.py -h
```


## Author
- Sergi Canet Vela


## License
This project is licensed under the terms of the MIT license.