import numpy as np
import matplotlib
import matplotlib.pyplot as plt

import simulation
import figure

global subjectExplication
subjectExplication = "Calculation of Price for max[0,T](St-K)+. Evaluation of convergence speed in proportion to step"

if __name__ == '__main__':

	print(subjectExplication)
	print("Simulation Start")

	# Stock and Option Information

	S0 = 10.0 # underlying price 
	Krate = 1.0 # strike rate (/underlying)
	K = S0 * Krate # strike price
	r = 0.05 # interest rate (/year)
	mu = 0.1 # stock increasing rate (/year)
	sigma = 0.1 # volatility (/sqrt(year))
	T = 1.0 # maturity (/year)
	discretization = 1000 # discretization
	# discretization = 365 # one day discretization
	# discretization = 365 * 24 # one hour discretization

	
	"""
	stockPriceList = []
	stockTimeList = []

	for i in range(3):
		optionPrice, stockPrice, timeList, deltat = simulation.simulateMaxOption(K, S0, mu, sigma, T, discretization, stockSimulation=True, method="Euler", randomSeed=None)
		print(optionPrice)
		stockPriceList.append(stockPrice)
		stockTimeList = timeList

	stockPriceList = np.array(stockPriceList)
	figure.drawFigureStock(stockPriceList, stockTimeList, K=K, figureSize=(8, 5))
	"""

	# Monte Carlo and Discretization Information

	MCiteration = 1000
	simulationTime = 50
	# discretizationList = [200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000]
	# discretizationList = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220]
	# discretizationList = [20, 60, 80, 120, 160, 200, 240, 280, 320, 360, 400, 440, 480, 520, 560, 600, 640, 680, 720, ]
	discretizationList = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]
	
	resultOptionPrice = np.zeros((simulationTime, len(discretizationList)))
	for i in range(simulationTime):
		print(str(i + 1) + " step finished")
		optionPricePresent, optionPricePresentVariance = simulation.calculateMaxOptionPrice(MCiteration, discretizationList, K, S0, r, mu, sigma, T, method="Euler", randomSeed=None)
		resultOptionPrice[i, :] = optionPricePresent

	mostProbableOptionPrice = np.average(resultOptionPrice[:, len(discretizationList) - 1])
	maxErrorList = np.array([np.max(np.absolute(resultOptionPrice[:, i] - mostProbableOptionPrice)) for i in range(len(discretizationList))])
	maxErrorRateList = maxErrorList / mostProbableOptionPrice * 100


	plt.figure(figsize=(8, 5))
	plt.plot(discretizationList, resultOptionPrice[0, :])
	plt.plot(discretizationList, resultOptionPrice[1, :])
	plt.plot(discretizationList, resultOptionPrice[2, :])
	plt.plot(discretizationList, resultOptionPrice[3, :])
	plt.plot(discretizationList, resultOptionPrice[4, :])
	plt.title('Predicted Option Price')
	plt.xlabel('Discretization Number')
	plt.ylabel('Option Price')
	plt.show()
	

	plt.figure(figsize=(8, 5))
	plt.plot(discretizationList, maxErrorRateList)
	plt.title('Max Error Result')
	plt.xlabel('Discretization Number')
	plt.ylabel('Max Error [%]')
	plt.show()

