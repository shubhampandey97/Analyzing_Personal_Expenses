import pandas as pd
import random
from faker import Faker
from datetime import date

fake = Faker()

categories = ["Food", "Transport", "Bills", "Entertainment", "Shopping", "Gifts", "Travel"]
payment_modes = ["Cash", "Credit Card", "Debit Card", "UPI", "Net Banking"]

def generate_expense_data(month):
    """Generate expense data for a given month and save as a CSV file."""
    month = str(month).zfill(2)  # Ensure two-digit month format

    # Convert string dates to `datetime.date` objects
    start_date = date(2024, int(month), 1)
    end_date = date(2024, int(month), 28)

    data = []
    for _ in range(200):  # 200 transactions per month
        data.append({
            "date": fake.date_between(start_date=start_date, end_date=end_date),  # Use date objects
            "category": random.choice(categories),
            "payment_mode": random.choice(payment_modes),
            "description": fake.sentence(nb_words=3),
            "amount_paid": round(random.uniform(50, 5000), 2),
            "cashback": round(random.uniform(0, 200), 2) if random.random() < 0.2 else 0
        })
    
    df = pd.DataFrame(data)
    df.to_csv(f"data_simulation/expenses_{month}.csv", index=False)
    print(f"✅ Data for month {month} saved successfully!")

# Generate data for all 12 months
for month in range(1, 13):
    generate_expense_data(month)

print("🎉 Expense data for 12 months generated successfully!")
