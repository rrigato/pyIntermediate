import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model

from pybrain.structure import FeedForwardNetwork
from pybrain.structure import LinearLayer, SigmoidLayer
from sklearn.datasets import load_diabetes


import pickle


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
	

class data_manipulation:
	def __init__(self):
	train = load_diabetes()
	
	trainX = train.data
	trainY = train.target
	
	trainX = pd.DataFrame(trainX)
	
	#rename the columns in python
	trainX.columns = ['a','b','c','d','e','f','g','h','i','j']
	
	trainX['a_by_b'] = trainX.a /trainX.b
	
	
	trainX.a[trainX.a >0] = trainX.a[trainX.a>0] * -1
	
	#initialize a new variable with the color red
	trainX['car'] = 'red'
	
	#replace values with missing
	trainX.car[0:5] = np.nan
	def neural(self):
		n = FeedForwardNetwork()
	



class serializeData:
	def __init__(self):
	
	def dumpData(dataFrame):
		dataFrame.to_pickle()
	def readData():
		return()
	
	
if __name__ == '__main__':
	loadData()