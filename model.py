def model():
	model = Sequential()
	model.add(Dense(12, input_dim=8, activation='relu')) #12 neurons, accepts 8 input variables, rectifier activation
	model.add(Dense(8, activation='relu'))
	model.add(Dense(1, activation='sigmoid')) #sigmoid function to ensure output of 0 or 1
