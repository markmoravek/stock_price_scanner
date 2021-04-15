import pandas as pd
import pandas_datareader.data as web


#Load stock tickers from file
ticker_file = 'tickers.txt'
data = pd.read_csv(ticker_file, sep=",", header =None, skipinitialspace=True)
ticker_list = data.loc[0,:].values.tolist()


#Get the stock price
stock_data = {ticker: web.get_data_yahoo(ticker) for ticker in ticker_list}
price = pd.DataFrame({ticker: data['Adj Close'] for ticker, data in stock_data.items()})


#Print price history to .csv
price.to_csv('PriceHistory.csv')
