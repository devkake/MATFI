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
	Krate = 0.8 # strike rate (/underlying)
	K = S0 * Krate # strike price
	r = 0.05 # interest rate (/year)
	sigma = 0.1 # volatility (/sqrt(year))
	T = 1.0 # maturity (/year)
	discretization = 1000 # discretization
	# discretization = 365 # one day discretization
	# discretization = 365 * 24 # one hour discretization

	
	"""
	stockPriceList = []
	stockTimeList = []

	for i in range(3):
		optionPrice, stockPrice, timeList, deltat = simulation.simulateMaxOption(K, S0, r, sigma, T, discretization, stockSimulation=True, method="Euler", randomSeed=None)
		print(optionPrice)
		stockPriceList.append(stockPrice)
		stockTimeList = timeList

	stockPriceList = np.array(stockPriceList)
	figure.drawFigureStock(stockPriceList, stockTimeList, K=K, figureSize=(8, 5))
	"""

	MCiteration = 2000
	discretizationList = [10, 100, 1000, 10000]
	optionPricePresent, optionPricePresentVariance = simulation.calculateMaxOptionPrice(MCiteration, discretizationList, K, S0, r, sigma, T, method="Euler", randomSeed=None)
	print(optionPricePresent)
	print(optionPricePresentVariance)	

