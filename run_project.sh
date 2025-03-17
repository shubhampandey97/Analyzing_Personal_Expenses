#!/bin/bash

# Create a virtual environment
python -m venv analyzing_personal_expense

# Activate the virtual environment
source analyzing_personal_expense/bin/activate

# Install the required packages
pip install -r streamlit_app/requirements.txt

# Set up the MySQL database
echo "Setting up the MySQL database..."
mysql -u root -p -e "CREATE DATABASE IF NOT EXISTS PersonalExpenses;"
mysql -u root -p PersonalExpenses < database/create_database.sql

# Populate the database with sample data
python database/insert_data.py

# Run the Streamlit app
streamlit run streamlit_app/app.py