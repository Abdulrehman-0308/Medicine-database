# Medication Data Flask App

This is a Flask app that reads medication data from an Excel file and saves it to a Postgres database. The app also splits the product_name column into three parts (name, type, quantity) and saves them as additional columns.

## Setup

1. Install the required packages by running pip install -r requirements.txt
2. Create a Postgres database and update the SQLALCHEMY_DATABASE_URI variable in config.py with your database credentials
3. Run the app by executing python app.py
4. Use a tool like Postman to send a POST request to http://localhost:5000/upload with the Excel file attached

## API Endpoints

* POST /upload: Upload an Excel file and save the data to the database

## Database Schema

The app uses the following database schema:

| Column Name | Data Type |
| --- | --- |
| id | integer |
| product_name | string |
| name | string |
| type | string |
| quantity | string |
| dosage | string |
| frequency | string |
| duration | string |
| created_at | timestamp |
| updated_at | timestamp |

## Field Level Validations

The app applies the following field level validations:

* product_name: required, max length 255
* name: required, max length 255
* type: required, max length 255
* quantity: required, max length 255
* dosage: required, max length 255
* frequency: required, max length 255
* duration: required, max length 255
