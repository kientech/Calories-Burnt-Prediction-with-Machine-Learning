from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import json
import numpy as np
import logging
import traceback

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("FastAPI app started")

app = FastAPI()


class ModelInput(BaseModel):
    Gender: int
    Age: int
    Height: float
    Weight: float
    Duration: float
    Heart_Rate: float
    Body_Temp: float


# Try to load the saved model
try:
    model = pickle.load(open("./colaries_model.sav", 'rb'))
    logger.info("Model loaded successfully.")
except FileNotFoundError:
    logger.error("Model file not found.")
    model = None
except Exception as e:
    logger.error(f"An error occurred while loading the model: {e}")
    model = None


@app.post("/predict")
def prediction(input_parameters: ModelInput):
    if model is None:
        logger.error("Model is not loaded, cannot make predictions.")
        raise HTTPException(status_code=500, detail="Model not available for predictions.")

    try:
        # Convert input parameters to a JSON string
        input_data = input_parameters.json()
        logger.info(f"Received input data: {input_data}")

        # Parse the JSON string into a Python dictionary
        input_dictionary = json.loads(input_data)

        # Extract individual feature values from the dictionary
        gender = input_dictionary['Gender']
        age = input_dictionary['Age']
        height = input_dictionary['Height']
        weight = input_dictionary['Weight']
        duration = input_dictionary['Duration']
        heart_rate = input_dictionary['Heart_Rate']
        body_temp = input_dictionary['Body_Temp']

        # Prepare the input data for prediction
        input_list = [gender, age, height, weight, duration, heart_rate, body_temp]
        input_array = np.asarray(input_list).reshape(1, -1)

        logger.info(f"Input array for prediction: {input_array}")

        # Make prediction
        predicted = model.predict(input_array)
        logger.info(f"Prediction result: {predicted}")

        # Return prediction as JSON
        return {"prediction": float(predicted[0])}

    except Exception as e:
        logger.error(f"An error occurred during prediction: {e}")
        logger.error(traceback.format_exc())  # Log the full stack trace
        raise HTTPException(status_code=500, detail="Prediction failed.")
