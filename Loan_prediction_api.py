from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Helper function to connect to the SQLite database
def get_db_connection():
    conn = sqlite3.connect('E:/Loan_Prediction/loanpredictionsystem.db')
    conn.row_factory = sqlite3.Row
    return conn

# 1. Fetch customer details by ID
@app.route('/customers/<customer_id>', methods=['GET'])
def get_customer(customer_id):
    conn = get_db_connection()
    customer = conn.execute('SELECT * FROM customers WHERE customer_id = ?', (customer_id,)).fetchone()
    conn.close()
    
    if customer:
        return jsonify(dict(customer))
    else:
        return jsonify({'error': 'Customer not found'}), 404

# 2. Submit a loan application
@app.route('/loan_applications', methods=['POST'])
def create_loan_application():
    data = request.get_json()
    customer_id = data.get('customer_id')
    loan_amount = data.get('loan_amount')
    purpose_of_loan = data.get('purpose_of_loan')
    application_date = data.get('application_date')

    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('INSERT INTO loan_applications (customer_id, loan_amount, purpose_of_loan, application_date) VALUES (?, ?, ?, ?)', 
                   (customer_id, loan_amount, purpose_of_loan, application_date))
    conn.commit()
    conn.close()
    
    return jsonify({'status': 'Loan Application Submitted Successfully'}), 201

# 3. Fetch loan prediction for a specific application
@app.route('/predictions/<application_id>', methods=['GET'])
def get_prediction(application_id):
    conn = get_db_connection()
    prediction = conn.execute('SELECT * FROM predictions WHERE application_id = ?', (application_id,)).fetchone()
    conn.close()
    
    if prediction:
        return jsonify(dict(prediction))
    else:
        return jsonify({'error': 'Prediction not found'}), 404

# 4. Fetch all loan officer applications handled by an officer
@app.route('/loan_officers/<officer_id>/applications', methods=['GET'])
def get_officer_applications(officer_id):
    conn = get_db_connection()
    applications = conn.execute('SELECT * FROM loan_officer_applications WHERE officer_id = ?', (officer_id,)).fetchall()
    conn.close()

    if applications:
        return jsonify([dict(app) for app in applications])
    else:
        return jsonify({'error': 'No applications found for this officer'}), 404

if __name__ == '__main__':
    app.run(debug=True)
