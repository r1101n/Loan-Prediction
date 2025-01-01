PRAGMA foreign_keys = ON;


-- Create Customers Table
CREATE TABLE IF NOT EXISTS customers (
    customer_id TEXT PRIMARY KEY,
    name TEXT,
    income REAL,
    age INTEGER,
    marital_status TEXT,
    home_ownership TEXT,
    car_ownership BOOLEAN,
    profession TEXT,
    years_in_current_job INTEGER,
    credit_score INTEGER
);

-- Create Loan Applications Table
CREATE TABLE IF NOT EXISTS loan_applications (
    application_id TEXT PRIMARY KEY,
    customer_id TEXT,
    loan_amount REAL,
    purpose_of_loan TEXT,
    application_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Create Predictions Table
CREATE TABLE IF NOT EXISTS predictions (
    prediction_id TEXT PRIMARY KEY,
    application_id TEXT,
    risk_flag TEXT,
    probability_score REAL,
    model_version TEXT,
    FOREIGN KEY (application_id) REFERENCES loan_applications(application_id)
);

-- Create Loan Officers Table
CREATE TABLE IF NOT EXISTS loan_officers (
    officer_id TEXT PRIMARY KEY,
    name TEXT,
    department TEXT,
    position TEXT
);

-- Create Loan Officer Applications Junction Table
CREATE TABLE IF NOT EXISTS loan_officer_applications (
    application_id TEXT,
    officer_id TEXT,
    PRIMARY KEY (application_id, officer_id),
    FOREIGN KEY (application_id) REFERENCES loan_applications(application_id),
    FOREIGN KEY (officer_id) REFERENCES loan_officers(officer_id)
);

-- Create Data Analysts Table
CREATE TABLE IF NOT EXISTS data_analysts (
    analyst_id TEXT PRIMARY KEY,
    name TEXT,
    department TEXT,
    specialization TEXT
);

-- Create Data Analyst Predictions Junction Table
CREATE TABLE IF NOT EXISTS data_analyst_predictions (
    prediction_id TEXT,
    analyst_id TEXT,
    PRIMARY KEY (prediction_id, analyst_id),
    FOREIGN KEY (prediction_id) REFERENCES predictions(prediction_id),
    FOREIGN KEY (analyst_id) REFERENCES data_analysts(analyst_id)
);

-- Create System Administrators Table
CREATE TABLE IF NOT EXISTS system_administrators (
    admin_id TEXT PRIMARY KEY,
    name TEXT,
    department TEXT,
    role TEXT
);

