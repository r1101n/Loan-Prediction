INSERT INTO customers (customer_id, name, income, age, marital_status, home_ownership, car_ownership, profession, years_in_current_job, credit_score)
VALUES 
('C001', 'John Doe', 60000, 35, 'Married', 'Owned', 1, 'Software Engineer', 5, 750),
('C002', 'Jane Smith', 45000, 28, 'Single', 'Rented', 0, 'Teacher', 3, 680),
('C003', 'Mike Johnson', 80000, 42, 'Married', 'Owned', 1, 'Manager', 10, 800);
SELECT * FROM customers 
WHERE name like 'JOHN%'

INSERT INTO loan_applications (application_id, customer_id, loan_amount, purpose_of_loan, application_date)
VALUES 
('A001', 'C001', 20000, 'Home Renovation', '2024-12-01'),
('A002', 'C002', 15000, 'Education', '2024-12-02'),
('A003', 'C003', 50000, 'Business Expansion', '2024-12-03');

select * from loan_applications
where application_id like 'A0%'

INSERT INTO predictions (prediction_id, application_id, risk_flag, probability_score, model_version)
VALUES 
('P001', 'A001', 'Low', 0.2, 'v1.0'),
('P002', 'A002', 'Medium', 0.5, 'v1.0'),
('P003', 'A003', 'High', 0.8, 'v1.0');
select * from predictions
where prediction_id like'P00%'

INSERT INTO loan_officers (officer_id, name, department, position)
VALUES 
('O001', 'Alice Brown', 'Loans', 'Senior Officer'),
('O002', 'David Lee', 'Loans', 'Junior Officer'),
('O003', 'Sara White', 'Risk', 'Risk Analyst');
select * from loan_officers