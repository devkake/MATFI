import matplotlib
import matplotlib.pyplot as plt

def drawFigureStock(stockPriceList, timeList, K=None, figureSize=(8, 5)):

	plt.figure(figsize=figureSize)

	m, n = stockPriceList.shape

	if K is not None:
		strike = n * [K]
		plt.plot(timeList, strike)

	for i in range(m):
		plt.plot(timeList, stockPriceList[i])

	plt.title('Simulation for Transition of Stock Price')
	plt.xlabel('Time')
	plt.ylabel('Stock Price')
	plt.show()