CREATE DATABASE IF NOT EXISTS finsight360;
USE finsight360;

CREATE TABLE branches (
    branch_id VARCHAR(10) PRIMARY KEY,
    branch_name VARCHAR(100),
    city VARCHAR(50),
    state VARCHAR(50),
    region VARCHAR(20)
);

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    gender VARCHAR(20),
    age INT,
    city VARCHAR(50),
    customer_segment VARCHAR(30),
    signup_date DATE,
    credit_score INT
);

CREATE TABLE accounts (
    account_id INT PRIMARY KEY,
    customer_id INT,
    branch_id VARCHAR(10),
    account_type VARCHAR(30),
    account_status VARCHAR(20),
    opened_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (branch_id) REFERENCES branches(branch_id)
);

CREATE TABLE transactions (
    transaction_id BIGINT PRIMARY KEY,
    account_id INT,
    transaction_date DATE,
    transaction_type VARCHAR(30),
    channel VARCHAR(30),
    amount DECIMAL(14,2),
    currency VARCHAR(5),
    status VARCHAR(20),
    merchant_category VARCHAR(40),
    is_international BOOLEAN,
    FOREIGN KEY (account_id) REFERENCES accounts(account_id)
);

CREATE TABLE support_tickets (
    ticket_id BIGINT PRIMARY KEY,
    customer_id INT,
    created_date DATE,
    issue_type VARCHAR(50),
    priority VARCHAR(20),
    status VARCHAR(20),
    resolution_hours DECIMAL(8,1),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE fraud_alerts (
    alert_id BIGINT PRIMARY KEY,
    transaction_id BIGINT,
    customer_id INT,
    alert_date DATE,
    risk_type VARCHAR(50),
    risk_score DECIMAL(5,1),
    severity VARCHAR(20),
    resolution_status VARCHAR(30),
    FOREIGN KEY (transaction_id) REFERENCES transactions(transaction_id),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);