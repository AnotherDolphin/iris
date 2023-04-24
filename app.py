import os
from flask import Flask, request
import pickle
import numpy as np

# load model
model = pickle.load(open('model.pkl', 'rb'))

# predict function
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 4)
    result = model.predict(to_predict)
    return result[0]


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Alexandre!'

@app.route('/predict', methods=['POST'])
def predict():
    to_predict_list = request.get_json()
    to_predict_list = [to_predict_list['sepal_length'], to_predict_list['sepal_width'],
                       to_predict_list['petal_length'], to_predict_list['petal_width']]
    to_predict_list = list(map(float, to_predict_list))
    result = ValuePredictor(to_predict_list)
    return {'prediction': result}

# for cloud run
# if __name__ == '__main__':
#     app.run(port=int(os.environ.get("PORT", 8080)),host='0.0.0.0',debug=True)
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

# enable debug
# if __name__ == '__main__':
#     app.run(debug=True)