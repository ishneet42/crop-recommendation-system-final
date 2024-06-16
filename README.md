# Crop Recommendation System

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Django](https://img.shields.io/badge/django-v3.2-green.svg)
![Machine Learning](https://img.shields.io/badge/machine_learning-random_forest-orange.svg)

## Description

This is a web application built with Django that recommends suitable crops to farmers based on input parameters such as soil type, temperature, humidity, etc. It uses a Random Forest Classifier model trained on agricultural data to make predictions.

## Features

- **User Authentication**: Allows farmers to create accounts and log in securely.
- **Input Form**: Collects data about soil type, temperature, humidity, rainfall, etc.
- **Prediction**: Uses a pre-trained Random Forest Classifier model to suggest suitable crops.
- **Crop Details**: Provides information about recommended crops including expected yield, growth period, etc.
- **Admin Panel**: Includes an admin interface to manage users, crops, and predictions.
- **User History**: Includes storage and retreival of user history.
  
## Installation

1. Clone the repository:
   git clone https://github.com/ishneet42/crop-recommendation-system-final/master.git

2. Navigate into the project directory:
   cd crop-recommendation-system

3. Install dependencies:
   pip install -r requirements.txt

4. Apply migrations:
   python manage.py migrate

5. Run the development server:
   python manage.py runserver


6. Access the application at [http://localhost:8000/](http://localhost:8000/)

## Usage

1. Create a user account or use the admin credentials.
2. Fill out the form with details about your agricultural conditions.
3. Submit the form to receive crop recommendations.
4. View detailed information about recommended crops.

## Technologies Used

- **Backend**: Django, Python
- **Machine Learning**: scikit-learn, pandas, numpy, seaborn, pickel, matplotlib
- **Frontend**: HTML/CSS, Bootstrap, JavaScript
- **Database**: SQLite (default, for development)




