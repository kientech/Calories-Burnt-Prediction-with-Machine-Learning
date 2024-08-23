# 🚀 Calories Burnt Prediction with Machine Learning

## Description

The **Calories Burnt Prediction with Machine Learning** project aims to predict the number of calories burned during physical activities based on various factors such as duration, activity type, age, weight, and more. This system leverages machine learning to provide accurate estimates, helping individuals to monitor their fitness progress and make informed decisions about their exercise routines.

### Purpose

Accurate prediction of calories burnt is essential for individuals tracking their fitness and health goals. This project addresses the following objectives:

- **Predict Calories Burnt:** Use machine learning to estimate the number of calories burned based on activity-related parameters.
- **Support Fitness Goals:** Provide users with insights into their calorie expenditure to help them achieve fitness and health goals.
- **Personalize Recommendations:** Tailor recommendations based on individual characteristics such as weight, age, and activity type.

### How It Works

1. **Data Collection:** The system uses historical data containing information about various physical activities, including parameters like duration, type of activity, age, and weight.
2. **Feature Engineering:** Data preprocessing and feature selection are performed to enhance the model’s performance.
3. **Model Training:** A machine learning model is trained on the dataset to learn the relationship between the input features and calories burnt.
4. **Prediction:** The trained model is used to predict the number of calories burnt based on user input.
5. **User Interface:** Users interact with a web application to input their activity details and receive calorie burn predictions.

### Components

- **Backend:** Implements machine learning algorithms and API endpoints using Python and Flask. It handles data processing, model training, and calorie prediction.
- **Frontend:** Developed using React.js, the frontend provides an intuitive interface for users to input their activity details and view predictions.
- **Model Training:** Involves training scripts and algorithms that process historical data to build a predictive model.

### Features

- **Calories Burnt Prediction:** Predict the number of calories burnt based on activity details such as duration, type, age, and weight.
- **Data Visualization:** Visualize predictions and trends to help users understand their calorie expenditure.
- **Interactive Interface:** Allows users to input their activity parameters and receive predictions in real time.

## Tech Stack

- **Backend:**
  - Python
  - FastAPI (for creating the API)
  - Scikit-learn (for machine learning model training and prediction)
- **Frontend:**
  - React.js (for building the user interface)
  - Axios (for making API calls)
  - Tailwind CSS (for styling and responsive design)
- **Database:** 
  - SQLite / MongoDB (optional, for storing historical data and user inputs)
- **Deployment:**
  - Heroku

## Installation

### Prerequisites

- Python 3.x
- Node.js and npm

### Backend Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/calories-burnt-prediction.git
    ```

2. Navigate to the backend directory:

    ```bash
    cd calories-burnt-prediction/backend
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Start the Flask server:

    ```bash
    python app.py
    ```

   The backend server should now be running on `http://localhost:5000` (or another port if configured differently).

### Frontend Setup

1. Navigate to the frontend directory:

    ```bash
    cd calories-burnt-prediction/frontend
    ```

2. Install the required npm packages:

    ```bash
    npm install
    ```

3. Start the React.js development server:

    ```bash
    npm start
    ```

   The frontend application should now be running on `http://localhost:3000` (or another port if configured differently).

## Usage

- **Web Interface:** Access the web application in your browser. Enter details about your physical activity, including duration, type, age, and weight, to receive a predicted number of calories burnt.
- **API Endpoints:** The backend API provides endpoints for receiving data from the frontend and returning predictions. You can interact with these endpoints directly using tools like Postman for testing.

### Example API Requests

- **GET /api/predict** - Retrieve a predicted number of calories burnt based on input parameters.
- **POST /api/predict** - Submit activity details and receive a prediction of calories burnt.

## Model Training

The machine learning model is trained using a dataset containing activity details and the corresponding calories burnt. The training script is located in the `model_training` directory.

### Steps to Retrain the Model:

1. Navigate to the `model_training` directory:

    ```bash
    cd calories-burnt-prediction/model_training
    ```

2. Run the training script:

    ```bash
    python train_model.py
    ```

   This script will preprocess the data, train the model, and save it for use by the backend API.

## Contributing

Contributions are welcome! To contribute to this project:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes and test them thoroughly.
4. Submit a pull request with a description of your changes.
