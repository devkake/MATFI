import numpy as np
import random
import math

def simulateStock(S0, mu, sigma, T, discretization, method="Euler", randomSeed=None):

	if randomSeed is None:
		random.seed()
	else:
		random.seed(randomSeed)

	deltat = float(T) / float(discretization)
	S = S0
	stockPrice = (discretization + 1) * [0.0]
	stockPrice[0] = S

	timeList = (discretization + 1) * [0.0]
	timeList[0] = 0.0

	if method == "Euler":
		for i in range(1, discretization + 1):
			S = S + mu * deltat + sigma * random.normalvariate(0.0, 1.0) * math.sqrt(deltat)
			stockPrice[i] = S
			timeList[i] = i * deltat

	else:
		print("Unkown method for simulateStock")

	return stockPrice, timeList, deltat

def simulateMaxOption(K, S0, mu, sigma, T, discretization, stockSimulation=True, method="Euler", randomSeed=None):

	if stockSimulation:
		stockPrice, timeList, deltat = simulateStock(S0, mu, sigma, T, discretization, method=method, randomSeed=randomSeed)
		return max(0, max(stockPrice) - K), stockPrice, timeList, deltat

	else:

		if randomSeed is None:
			random.seed()
		else:
			random.seed(randomSeed)

		deltat = float(T) / float(discretization)
		S = S0
		maxS = S

		if method == "Euler":
			for i in range(1, discretization + 1):
				S = S + mu * deltat + sigma * random.normalvariate(0.0, 1.0) * math.sqrt(deltat)
				if maxS < S:
					maxS = S

		else:
			print("Unkown method for simulateStock")

		return max(0, maxS - K), maxS

def statisticsOneMaxOption(trialNumber, K, S0, mu, sigma, T, discretization, method="Euler", randomSeed=None):

	statistics = trialNumber * [0.0]

	for i in range(trialNumber):
		optionPrice, maxS = simulateMaxOption(K, S0, mu, sigma, T, discretization, stockSimulation=False, method=method, randomSeed=randomSeed)
		statistics[i] = optionPrice

	return statistics

def statisticsMaxOption(discretizationList, trialNumber, K, S0, mu, sigma, T, method="Euler", randomSeed=None):

	n = len(discretizationList)
	statistics = np.zeros((trialNumber, n))

	for i in range(n):
		statisticsOne = statisticsOneMaxOption(trialNumber, K, S0, mu, sigma, T, discretizationList[i], method=method, randomSeed=randomSeed)
		statisticsOne = np.array(statisticsOne)
		statistics[:, i] = statisticsOne.T
		# print("discretization by " + str(discretizationList[i]) + " finished")

	return statistics

def calculateMaxOptionPrice(MCinteration, discretizationList, K, S0, r, mu, sigma, T, method="Euler", randomSeed=None):

	statistics = statisticsMaxOption(discretizationList, MCinteration, K, S0, mu, sigma, T, method=method, randomSeed=randomSeed)

	n = len(discretizationList)

	optionPrice = n * [0.0]
	optionPriceVariance = n * [0.0]

	for i in range(n):
		average = np.average(statistics[:, i].T)
		standardDeviation = np.std(statistics[:, i].T)
		optionPrice[i] = average
		optionPriceVariance[i] = standardDeviation

	optionPricePresent = np.exp(-1.0 * r * T) * np.array(optionPrice)
	optionPricePresentVariance = np.exp(-1.0 * r * T) * np.array(optionPriceVariance)

	return optionPricePresent, optionPricePresentVariance
	


if __name__ == '__main__':

	import matplotlib.pyplot as plt

	K = 10.0
	S0 = 10.0
	r = 0.05
	mu = 0.1
	sigma = 0.1
	T = 1.0
	discretization = 1000


	"""
	optionPrice, stockPrice, timeList, deltat = simulateMaxOption(K, S0, mu, sigma, T, discretization, stockSimulation=True, method="Euler", randomSeed=None)
	print(optionPrice)
	plt.plot(timeList, stockPrice)
	plt.show()
	"""

	"""
	discretizationList = [1000, 2000, 3000]
	trialNumber = 10
	statistics = statisticsMaxOption(discretizationList, trialNumber, K, S0, mu, sigma, T, method="Euler", randomSeed=None)
	print(statistics)
	"""

	MCiteration = 1000
	discretizationList = [200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000]
	optionPricePresent, optionPricePresentVariance = calculateMaxOptionPrice(MCiteration, discretizationList, K, S0, r, mu, sigma, T, method="Euler", randomSeed=None)
	print(optionPricePresent)
	print(optionPricePresentVariance)
