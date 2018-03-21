import numpy
def fix_seed():
	#fixing a random seed for reproductibility
	numpy.random.seed(7)

def load_data():
	#using the Pima Indian dataset from the UCI Machine Learning repository
	#loading dataset
	dataset = numpy.loadtxt("pima-indians-diabetes.csv", delimiter=",")
	X = dataset[:,0:8]
	Y = dataset[:,8]
	return X, Y
