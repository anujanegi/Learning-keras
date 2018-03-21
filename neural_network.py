from load_data import *
from model import *

#tieing everything together
fix_seed()
X, Y = load_data()
model = fit_model(compile_model(def_model()), X, Y)
evaluate(model, X, Y)
