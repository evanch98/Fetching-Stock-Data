# Import yfinance to get stock data
import yfinance as yf

# Ticker Symbols
symbols = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'FB', 'TSLA', 'NVDA', 'NKE', 'PFE', 'NFLX']

# Name of the company
names = ['Apple', 'Microsoft', 'Google', 'Amazon', 'Facebook', 'Tesla', 'Nvidia', 'Nike', 'Pfizer', 'Netflix']

# To save the data into the text file
stock = open('Stock_data.txt', 'w')

# Counter
i = 0

# Getting the data and writing into a text file
for symbol in symbols:
    symbol_ = yf.Ticker(symbol)
    symbol_data = symbol_.history(period='5d')
    text = stock.write(names[i] + '\n')
    text = stock.write(str(symbol_data.head()) + '\n')
    text = stock.write('\n')
    i += 1

stock.close()
