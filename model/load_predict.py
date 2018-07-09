import pandas as pd
import numpy as np
import pickle
from keras.models import load_model, model_from_json
from keras.datasets import mnist
from keras_pickle_wrapper import KerasPickleWrapper


json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights('model.h5')

model_wrapper = KerasPickleWrapper(loaded_model)
python_model = pickle.dumps(model_wrapper)

keras_model = pickle.loads(python_model)

prediction = keras_model().predict(np.ones((1, 28, 28, 1)))
print(np.argmax(prediction, axis=1))
