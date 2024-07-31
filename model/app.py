import json
import requests

url = "http://127.0.0.1:8000/predict"

input_data = {
    "Gender": 1,
    "Age": 68,
    "Height": 194.0,
    "Weight": 94.0,
    "Duration": 29.0,
    "Heart_Rate": 105.0,
    "Body_Temp": 40.8
}

# Convert the input data to JSON
input_json = json.dumps(input_data)
try:
    response = requests.post(url, data=input_json, headers={"Content-Type": "application/json"})
    prediction = response.json()
    print(prediction)
    if response.status_code == 200:
        prediction = response.json()
        print(f"Prediction: {prediction}")
    else:
        print(f"Error: Received status code {response.status_code}")
        print(f"Response: {response.text}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
