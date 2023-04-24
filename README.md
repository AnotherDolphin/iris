## Dockerized Flask app serving IRIS model predictions

This is a simple Flask app that serves predictions from a pre-trained model. The model is a simple logistic regression model trained on the IRIS dataset. The model is saved as a pickle file and is loaded into the app at runtime.

The app is dockerized and can be run locally or deployed to a cloud provider.

### Running the app locally

1. Clone the repo
2. Build the docker image: `docker build -t iris-app .`
3. Run the docker container: `docker run -p 5000:5000 iris-app`
4. Navigate to `http://localhost:5000/` to confirm the app is running
4. Make a prediction request

#### Example request:

    - [POST] http://localhost:5000/predict
    - Content-Type: application/json
    - Body: {"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}

#### Example response:
`{"prediction": ""Iris-setosa""}`

### No time to run locally? Try it out Live!

The app is deployed on Google Cloud Run and can be accessed at the following URL:

https://iris-xld6dcishq-uc.a.run.app/