import matplotlib
import matplotlib.pyplot as plt
import simulation

global subjectExplication
subjectExplication = "Calculation of Price for max[0,T](St-K)+. Evaluation of convergence speed in proportion to step"

if __name__ == '__main__':

	print(subjectExplication)
	print("Simulation Start")

	K = 8.0
	S0 = 10.0
	r = 0.05
	sigma = 0.1
	T = 1.0
	deltat = 0.0001


