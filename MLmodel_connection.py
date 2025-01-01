import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

# Step 1: Connect to the SQLite database and load the data
db_path = 'E:/Loan_Prediction/loanpredictionsystem.db' 
conn = sqlite3.connect(db_path)

# Query data for training
query = """
SELECT 
    c.income, 
    c.age, 
    c.credit_score, 
    l.loan_amount, 
    l.purpose_of_loan, 
    p.risk_flag 
FROM 
    customers c
JOIN 
    loan_applications l ON c.customer_id = l.customer_id
JOIN 
    predictions p ON l.application_id = p.application_id
WHERE 
    p.risk_flag IS NOT NULL
"""
df = pd.read_sql_query(query, conn)
conn.close()

# Step 2: Preprocess the data
# Encode categorical variables (e.g., purpose_of_loan)
df = pd.get_dummies(df, columns=['purpose_of_loan'], drop_first=True)

# Define features (X) and target (y)
X = df.drop('risk_flag', axis=1)
y = df['risk_flag']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Train a Machine Learning Model
model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X_train, y_train)

# Step 4: Evaluate the Model
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Step 5: Save the Model
model_path = 'E:/Loan_Prediction/loan_model.pkl'
joblib.dump(model, model_path)
print(f"Model saved to {model_path}")
