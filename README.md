# CoinGecko API to retrieve quotes for multiple cryptocurrencies in Flask

In this implementation I used Python API through the Flask framework to fetch cryptocurrency quotes using a URL link as a request. 

The CoinGecko API was used to retrieve quotes for multiple cryptocurrencies and allow the selection of exchange currencies. 

It's important make sure to install the Flask and requests packages before running the code. 

The API has a single endpoint (/get_crypto_quotes) that accepts a list of query parameters crypto_name in the URL, as well as an optional parameter vs_currency that allows you to select the exchange currency. 

The get_crypto_quotes function is responsible for making the call to the CoinGecko API and processing the quotes for the specified cryptocurrencies.