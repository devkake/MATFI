import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import multiprocessing as mp
import random
import pickle

import simulation
import figure

global subjectExplication
subjectExplication = "Calculation of Price for max[0,T](St-K)+. Evaluation of convergence speed in proportion to step"


"""
resultOptionPrice = np.zeros((simulationTime, len(discretizationList)))
for i in range(simulationTime):
	print(str(i + 1) + " step finished")
	optionPricePresent, optionPricePresentVariance = simulation.calculateMaxOptionPrice(MCiteration, discretizationList, K, S0, r, mu, sigma, T, method="Euler", randomSeed=None)
	resultOptionPrice[i, :] = optionPricePresent
"""

if __name__ == '__main__':

	print(subjectExplication)
	print("Simulation Start")
	random.seed()

	# Stock and Option Information

	S0 = 10.0 # underlying price 
	Krate = 0.8 # strike rate (/underlying)
	K = S0 * Krate # strike price
	r = 0.05 # interest rate (/year)
	mu = 0.1 # stock increasing rate (/year)
	sigma = 0.1 # volatility (/sqrt(year))
	T = 1.0 # maturity (/year)
	discretization = 100 # discretization
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
	# MCiterationList = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750, 1800, 1850, 1900, 1950, 2000]
	#MCiterationList = [200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400, 3600, 3800, 4000]
	MCiterationList = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420, 440, 460, 480, 500, 520, 540, 560, 580, 600, 620, 640, 660, 680, 700, 720, 740, 760, 780, 800, 820, 840, 860, 880, 900, 920, 940, 960, 980, 1000, 1020, 1040, 1060, 1080, 1100, 1120, 1140, 1160, 1180, 1200, 1220, 1240, 1260, 1280, 1300, 1320, 1340, 1360, 1380, 1400, 1420, 1440, 1460, 1480, 1500]
	# MCiterationList = [50, 100, 150, 200]
	simulationTime = 100
	process = 4 # number for parallel calculation
	partialSimulationTime = int(simulationTime / process)
	# discretizationList = [200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000]
	# discretizationList = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220]
	# discretizationList = [20, 60, 80, 120, 160, 200, 240, 280, 320, 360, 400, 440, 480, 520, 560, 600, 640, 680, 720, 760, 800, 840, 880, 920, 960, 1000]
	# discretizationList = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]
	
	
	"""
	resultOptionPrice = np.zeros((simulationTime, len(discretizationList)))
	for i in range(simulationTime):
		print(str(i + 1) + " step finished")
		optionPricePresent, optionPricePresentVariance = simulation.calculateMaxOptionPrice(MCiteration, discretizationList, K, S0, r, mu, sigma, T, method="Euler", randomSeed=None)
		resultOptionPrice[i, :] = optionPricePresent
	"""

	"""
	def functionForMultiProcess(processNumber):
		print("start " + str(processNumber) + " process")
		resultOptionPrice = np.zeros((partialSimulationTime, len(discretizationList)))
		for i in range(partialSimulationTime):
			optionPricePresent, optionPricePresentVariance = simulation.calculateMaxOptionPrice(MCiteration, discretizationList, K, S0, r, mu, sigma, T, method="Euler", randomSeed=None)
			resultOptionPrice[i, :] = optionPricePresent
		print("finish " + str(processNumber) + " process")
		return resultOptionPrice

	pool = mp.Pool(process)
	callback = pool.map(functionForMultiProcess, range(process))

	resultOptionPrice = np.zeros((simulationTime, len(discretizationList)))

	for i in range(process):
		for j in range(partialSimulationTime):
			resultOptionPrice[i * partialSimulationTime + j, :] = callback[i][j, :]
	"""

	optionPriceList = len(MCiterationList) * [0.0]
	plt.figure(figsize=(8, 5))
	for j in range(3):
		for i in range(len(MCiterationList)):
			n = MCiterationList[i]
			print("MC Iteration " + str(n) + " Finished")
			optionPricePresent, optionPricePresentVariance = simulation.calculateMaxOptionPrice(n, [discretization], K, S0, r, mu, sigma, T, method="Euler", randomSeed=None)
			optionPriceList[i] = optionPricePresent[0]

		
		plt.plot(MCiterationList, optionPriceList)
	plt.title('Convergence of Option Price')
	plt.xlabel('Number of Iteration for Monte-Carlo')
	plt.ylabel('Option Price')
	plt.show()

	print("calculation finished")

	"""
	openFileName = "pickle_K08.dump"
	openFile = open(openFileName, 'wb')
	pickle.dump(resultOptionPrice, openFile)
	openFile.close()
	"""

	# After pickle

	"""
	openFileName = "pickle1.dump"
	openFile = open(openFileName, 'rb')
	resultOptionPrice = pickle.load(openFile)
	openFile.close()

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
	"""