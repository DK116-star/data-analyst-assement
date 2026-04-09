# 📊 Data Analyst Assignment
Project Overview

This project demonstrates core data analysis skills using SQL, Excel, and Python.  
It covers real-world scenarios including hotel management, clinic operations, ticket analysis, and basic data processing.

 SQL Analysis

## 📌 Approach

- Used MySQL to create and manage relational tables for Hotel and Clinic systems.
- Implemented queries using `JOIN`, `GROUP BY`, `HAVING`, and aggregate functions.
- Calculated billing amounts using `item_quantity * item_rate`.
- Used window functions like `RANK()` for ranking-based problems.
- Used subqueries and CTEs for better readability and structured logic.
- Profit is calculated as:
  - `Profit = Revenue - Expenses`
- Used `CASE` statements to classify profit status (Profitable / Not Profitable).
- Used `COALESCE` / `IFNULL` to handle missing values.

---

## 📌 Hotel System

- Designed tables: users, bookings, booking_commercials, items
- Solved:
  - Last booked room per user
  - Monthly billing calculations
  - High-value bill filtering
  - Most and least ordered items
  - Second highest bill per month

---

## 📌 Clinic System

- Designed tables: clinics, customer, clinic_sales, expenses
- Solved:
  - Revenue by sales channel
  - Top 10 valuable customers
  - Month-wise revenue, expense, profit, and status
  - Most profitable clinic per city
  - Second least profitable clinic per state

---

# 🟢 Excel Analysis

## 📌 Approach

- Worked with two datasets:
  - Ticket data
  - Feedback data

---

## 📌 Lookup Operation

- Used `INDEX + MATCH` to populate `ticket_created_at`
- Reason:
  - More flexible than VLOOKUP
  - Works even when lookup column is not on the left side

---

## 📌 Time Analysis

- Created helper columns:
  - **Same Day** → using `INT()` to compare dates
  - **Same Hour** → using `HOUR()` to compare time

---

## 📌 Aggregation

- Used `COUNTIFS` to calculate:
  - Tickets created and closed on the same day
  - Tickets created and closed in the same hour
- Performed outlet-wise aggregation

---

# 🟢 Python Implementation

## 📌 1. Time Converter

- Converts minutes into hours and remaining minutes
- Logic used:
  - Integer division (`//`)
  - Modulus (`%`)

---

## 📌 2. Remove Duplicates

- Removes duplicate characters from a string
- Logic used:
  - Loop through characters
  - Add character only if not already present
- Maintains original order of characters


