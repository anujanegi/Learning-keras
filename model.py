from keras.models import Sequential
from keras.layers import Dense

def def_model():
	#12 neurons, accepts 8 input variables, rectifier activation
	model = Sequential()
	model.add(Dense(12, input_dim=8, activation='relu')) 
	model.add(Dense(8, activation='relu'))
	#sigmoid function to ensure output of 0 or 1
	model.add(Dense(1, activation='sigmoid')) 
	return model

def compile_model(model):
	#using logarithmic loss, gradient descent
	model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
	return model

def fit_model(model, X, Y):
	model.fit(X, Y, epochs=50, batch_size=10)
	return model

def evaluate(model, X, Y):
	scores = model.evaluate(X,Y)
	print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
