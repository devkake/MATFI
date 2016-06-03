import random
import math

def simulateStock(S0, r, sigma, T, deltat, method="Euler", randomSeed=None):

	if randomSeed is None:
		random.seed()
	else:
		random.seed(randomSeed)

	n, lastdeltat = divmod(T, deltat)
	n = int(n)
	S = S0
	stockPrice = (n + 1) * [0.0]
	stockPrice[0] = S

	if method == "Euler":
		for i in range(1, n):
			S = S + r * deltat + sigma * random.normalvariate(0.0, 1.0) * math.sqrt(deltat)
			stockPrice[i] = S
		S = S + r * lastdeltat + sigma * random.normalvariate(0.0, 1.0) * math.sqrt(lastdeltat)
		stockPrice[n] = S

	else:
		print("Unkown method for simulationBlackScholes")

	return stockPrice, n, lastdeltat

def simulateMaxOption(K, S0, r, sigma, T, deltat, method="Euler", randomSeed=None):

	stockPrice, n, lastdeltat = simulateStock(S0, r, sigma, T, deltat, method="Euler", randomSeed=None)
	return max(0, max(stockPrice) - K), stockPrice, n, lastdeltat


if __name__ == '__main__':

	import matplotlib.pyplot as plt

	K = 8.0
	S0 = 10.0
	r = 0.05
	sigma = 0.1
	T = 1.0
	deltat = 0.0001

	optionPrice, stockPrice, n, lastdeltat = simulateMaxOption(K, S0, r, sigma, T, deltat, method="Euler", randomSeed=None)
	
	print(optionPrice)
	plt.plot(stockPrice)
	plt.show()
