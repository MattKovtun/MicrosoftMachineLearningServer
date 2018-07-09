from azureml.deploy import DeployClient
from azureml.deploy.server import MLServer
import numpy as np
import pickle
from keras.models import load_model, model_from_json
from keras_pickle_wrapper import KerasPickleWrapper
from PIL import Image

# -- Define the location of the ML Server --
# -- for local onebox for Machine Learning Server: http://localhost:12800
# -- Replace with connection details to your instance of ML Server.
HOST = 'http://localhost:12800'
context = ('admin', 'Eleks@2018')
client = DeployClient(HOST, use=MLServer, auth=context)

# keras models can not be pickled, use KerasPickleWrapper to wrap the model for serialization
json_file = open('model/model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights('model/model.h5')

model_wrapper = KerasPickleWrapper(loaded_model)
python_model = pickle.dumps(model_wrapper)


# Define Function to deploy as webservice

def deploy():
    def func(x):
        import numpy as np
        im = np.reshape(x, newshape=[1, 28, 28, 1])
        prediction = keras_model().predict(im)

        return np.argmax(prediction, axis=1)

    def init():
        import pickle
        global keras_model
        keras_model = pickle.loads(input_model)

    # Deploy the web service
    service_name = 'KerasModel'
    service_version = '1.0.0'

    service = client.service(service_name) \
        .version(service_version) \
        .code_fn(func, init) \
        .inputs(x=np.matrix) \
        .outputs(answer=int) \
        .models(input_model=python_model) \
        .description('keras model example') \
        .deploy()

    # with open("swagger.json", "w") as swagger_file:
    #     swagger_file.write("%s" % service.swagger())
    #


def explore():
    img = Image.open('images/img_10.jpg')
    x = np.array(img)  # im2arr.shape: height x width x channel
    # x = np.ones((28, 28))
    svc = client.get_service('KerasModel', version='1.0.0')
    res = svc.func(x)
    # output is the predicted number
    print(res.outputs)


def destroy():
    client.delete_service('KerasModel', version='1.0.0')


if __name__ == "__main__":
    # destroy()
    # deploy()
    explore()
