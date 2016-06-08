import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model

from pybrain.structure import FeedForwardNetwork
from pybrain.structure import LinearLayer, SigmoidLayer



def loadData():
	'''
		Loads the data and prints some summary statistics
		
	'''
	diabetes = datasets.load_diabetes()
	diabetes_X = diabetes.data[:,np.newaxis, 2]
	
	diabetes_X_train = diabetes_X[:-20]
	diabetes_X_test = diabetes_X[-20:]
	diabetes_y_train = diabetes.target[:-20]
	diabetes_y_test = diabetes.target[-20:]
	
	regr = linear_model.LinearRegression()
	
	regr.fit(diabetes_X_train, diabetes_y_train)
	
	print("Coefficients: \n", regr.coef_)
	

class NN:
	def __init__(self):
	
	def neural(self):
		n = FeedForwardNetwork()
	


if __name__ == '__main__':
	loadData()