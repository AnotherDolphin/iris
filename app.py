from flask import Flask, request
import pickle
import numpy as np

# load model
model = pickle.load(open('model.pkl', 'rb'))

# predict function
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 5)
    result = model.predict(to_predict)
    return result[0]


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/a')
def hello_worsld():
    return 'Hasdfd!'

# predict route
@app.route('/predict', methods=['POST'])
def predict():
    to_predict_list = request.get_json()['input']
    to_predict_list = list(map(int, to_predict_list))
    result = ValuePredictor(to_predict_list)
    return result

# enable debug
if __name__ == '__main__':
    app.run(debug=True)
