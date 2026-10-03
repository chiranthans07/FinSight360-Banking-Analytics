#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 22:20:28 2026

@author: chiranthansateesh
"""

import pandas as pd
import matplotlib.pyplot as plt

# =========================================================
# FINSIGHT 360 - PYTHON DATA ANALYSIS
# =========================================================

# ---------- 1. LOAD DATA ----------
base_path = "/Users/chiranthansateesh/Desktop/finsight360_dataset/data/raw/"

customers = pd.read_csv(base_path + "customers.csv")
accounts = pd.read_csv(base_path + "accounts.csv")
transactions = pd.read_csv(base_path + "transactions.csv")
branches = pd.read_csv(base_path + "branches.csv")
support = pd.read_csv(base_path + "support_tickets.csv")
fraud = pd.read_csv(base_path + "fraud_alerts.csv")

print("\n========== DATASET SIZES ==========")

datasets = {
    "Customers": customers,
    "Accounts": accounts,
    "Transactions": transactions,
    "Branches": branches,
    "Support Tickets": support,
    "Fraud Alerts": fraud
}

for name, df in datasets.items():
    print(f"{name}: {df.shape[0]} rows, {df.shape[1]} columns")


# ---------- 2. DATA QUALITY ----------
print("\n========== DATA QUALITY ==========")

for name, df in datasets.items():
    print(f"\n{name}")
    print("Missing values:", df.isnull().sum().sum())
    print("Duplicate rows:", df.duplicated().sum())


# ---------- 3. TRANSACTION CLEANING ----------
transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"],
    errors="coerce"
)

# Remove rows where essential transaction information is missing
transactions = transactions.dropna(
    subset=["transaction_id", "account_id", "amount"]
)

# Remove duplicate transaction IDs
transactions = transactions.drop_duplicates(
    subset=["transaction_id"]
)

print("\nTransactions after cleaning:", len(transactions))


# ---------- 4. TRANSACTION KPIs ----------
print("\n========== TRANSACTION KPIs ==========")

print("Total transactions:", len(transactions))
print(
    "Total transaction value: ₹",
    round(transactions["amount"].sum(), 2)
)
print(
    "Average transaction value: ₹",
    round(transactions["amount"].mean(), 2)
)
print(
    "Maximum transaction value: ₹",
    round(transactions["amount"].max(), 2)
)


# ---------- 5. TRANSACTION TYPE ----------
type_analysis = (
    transactions
    .groupby("transaction_type")
    .agg(
        transaction_count=("transaction_id", "count"),
        total_value=("amount", "sum"),
        average_value=("amount", "mean")
    )
    .sort_values("total_value", ascending=False)
)

print("\n========== TRANSACTION TYPE ==========")
print(type_analysis.round(2))


# ---------- 6. TRANSACTION STATUS ----------
status_analysis = (
    transactions
    .groupby("status")
    .agg(
        transaction_count=("transaction_id", "count"),
        total_value=("amount", "sum")
    )
    .sort_values("transaction_count", ascending=False)
)

print("\n========== TRANSACTION STATUS ==========")
print(status_analysis.round(2))


# ---------- 7. MONTHLY TREND ----------
transactions["month"] = (
    transactions["transaction_date"]
    .dt.to_period("M")
    .astype(str)
)

monthly = (
    transactions
    .groupby("month")
    .agg(
        transaction_count=("transaction_id", "count"),
        total_value=("amount", "sum")
    )
    .reset_index()
)

print("\n========== MONTHLY TREND ==========")
print(monthly.round(2))


# ---------- 8. CUSTOMER SEGMENTS ----------
customer_segments = (
    customers
    .groupby("customer_segment")
    .size()
    .sort_values(ascending=False)
)

print("\n========== CUSTOMER SEGMENTS ==========")
print(customer_segments)


# ---------- 9. FRAUD ANALYSIS ----------
fraud_analysis = (
    fraud
    .groupby("severity")
    .agg(
        alert_count=("risk_score", "count"),
        average_risk_score=("risk_score", "mean")
    )
    .sort_values("average_risk_score", ascending=False)
)

print("\n========== FRAUD ANALYSIS ==========")
print(fraud_analysis.round(2))


# ---------- 10. SUPPORT ANALYSIS ----------
support_analysis = (
    support
    .groupby("issue_type")
    .agg(
        ticket_count=("ticket_id", "count"),
        average_resolution_hours=("resolution_hours", "mean")
    )
    .sort_values("ticket_count", ascending=False)
)

print("\n========== SUPPORT ANALYSIS ==========")
print(support_analysis.round(2))


# ---------- 11. CHART 1 ----------
type_analysis["transaction_count"].plot(
    kind="bar",
    figsize=(10, 5),
    title="Transaction Volume by Type"
)

plt.xlabel("Transaction Type")
plt.ylabel("Number of Transactions")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ---------- 12. CHART 2 ----------
status_analysis["transaction_count"].plot(
    kind="bar",
    figsize=(8, 5),
    title="Transaction Status Distribution"
)

plt.xlabel("Transaction Status")
plt.ylabel("Number of Transactions")
plt.tight_layout()
plt.show()


# ---------- 13. CHART 3 ----------
plt.figure(figsize=(12, 5))

plt.plot(
    monthly["month"],
    monthly["total_value"],
    marker="o"
)

plt.title("Monthly Transaction Value Trend")
plt.xlabel("Month")
plt.ylabel("Transaction Value")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# ---------- 14. KEY INSIGHTS ----------
print("\n========== KEY INSIGHTS ==========")

print(
    "Highest-value transaction type:",
    type_analysis.index[0]
)

print(
    "Most common transaction status:",
    status_analysis.index[0]
)

print(
    "Largest customer segment:",
    customer_segments.index[0]
)

print(
    f"Total transactions analyzed: {len(transactions):,}"
)

print(
    f"Total transaction value: ₹{transactions['amount'].sum():,.2f}"
)

print("\n========== ANALYSIS COMPLETE ==========")