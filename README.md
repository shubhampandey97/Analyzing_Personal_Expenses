# Analyzing Personal Expenses

This project is designed to help you track and analyze your personal expenses. It includes a data insertion script to populate a MySQL database with expense data and a Streamlit dashboard to visualize and analyze the expenses.

## Project Structure
Analyzing_Personal_Expenses/
│── data_simulation/
│   ├── generate_expense_data.py  # Generates fake expense data using Faker
│   ├── expense_data.csv  # Sample generated dataset
│
│── database/
│   ├── create_database.sql  # MySQL schema for 12 monthly tables
│   ├── insert_data.py  # Script to insert CSV data into MySQL
│   ├── queries.sql  # SQL queries for insights
│
│── eda/
│   ├── eda_analysis.ipynb  # Jupyter Notebook for Exploratory Data Analysis
│
│── streamlit_app/
│   ├── app.py  # Streamlit dashboard for visualizing expenses
│   ├── query_functions.py  # Functions to fetch query results
│   ├── requirements.txt  # Dependencies (Streamlit, MySQL Connector, Pandas, etc.)
│
│── README.md  # Instructions to run the project
│── .env.example  # Sample database credentials
│── config.py  # Database connection settings
│── run_project.sh  # Script to set up and run the project

## Setup

1. **Clone the repository:**

    ```sh
    git clone <repository_url>
    cd Analyzing_Personal_Expenses
    ```

2. **Create a virtual environment and activate it:**

    ```sh
    python -m venv analyzing_personal_expense
    .\analyzing_personal_expense\Scripts\activate  # On Windows
    source analyzing_personal_expense/bin/activate  # On macOS/Linux
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the MySQL database:**

    - Create a MySQL database named `PersonalExpenses`.
    - Update the `config.py` file with your MySQL credentials.

5. **Populate the database with sample data:**

    ```sh
    python database/insert_data.py
    ```

6. **Run the Streamlit app:**

    ```sh
    streamlit run streamlit_app/app.py
    ```

## Configuration

The `config.py` file contains the database configuration. Make sure to update it with your MySQL credentials:

```python
# import os
# from dotenv import load_dotenv

# load_dotenv()

# DB_CONFIG = {
#     "host": os.getenv("DB_HOST", "localhost"),
#     "user": os.getenv("DB_USER", "root"),
#     "password": os.getenv("DB_PASSWORD", "@shubh97"),
#     "database": os.getenv("DB_NAME", "PersonalExpenses")
# }