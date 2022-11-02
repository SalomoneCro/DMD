import csv
import yfinance as yf

f = open('consumerdiscr.csv', 'r')
reader = csv.reader(f)
tickers = [i.split(',')[0] for i in f.readlines()]
df = yf.download(tickers, start = "2018-01-01", end="2018-12-31")['Adj Close']
dft = df.T
#convierto el panda dataframe en un vector con los precios de cada empresa en fila
vector = dft.values







