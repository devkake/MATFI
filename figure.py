import matplotlib
import matplotlib.pyplot as plt

def drawFigureStock(stockPriceList, K=None, figureSize):

	n = len(stockPriceList)
	for i in range(n)