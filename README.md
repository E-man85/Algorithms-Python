# Algorithms and Programming in Python

In this repositories you can find my journey in introducing programming and algorithms in python.

## 06-Projects

> 01-SalesAplication

The application consists of processing information from a data structure of
Sales (Part 1) and respective data outputs (Part 2).
> - [PartI](https://github.com/E-man85/Algorithms-Python/blob/main/06-Projects/01-SalesAplication/PartI.py)

The Sales structure is defined by:

- the Sale ID (integer: incremental 1 / 2 / 3 / 4 / …)
- Seller Code (integer: 100 / 200 / 300 / …)
- Customer Designation (string; “Customer1”, “Customer2”, …)
- Zone (string: North(“N”) / Center(“C”) / South(“S”) / Islands(“I”))
- Date (string with “mm/dd/yyyy” format)
- Product Code (string: “ABC100”, “XYAS12”, “XPTO1”, …)
- Quantity (integer: 1 / 2 / 5 / 7 / …)
- the Sale Value (float €)
  
Example of sales records in a list:

[[1, 100, “N”, “Customer1”, “02/01/2021”, 1234.45, “ABC100”],

[2, 100, "S", "Customer1", "01/02/2021", 234.2, "XPTO1"],

[3, 200, "C", "Customer3", "01/02/2021", 1142.64, "XPTO1"],

[4, 300, “C”, “Customer4”, “01/03/2021”, 1253.9, “XYAS12”], … ]

The logic of relationships is that a seller can sell several
products. You can do it on the same date (or on different dates), on the same
zone (or in different zones) and with the same or different prices. Each
sale generates an incremental sales record. The same customer can
exist in different zones.

- Expected functions: Insert / Consult / List / Change / Delete
> - PartII

Expected outputs:
- Total Sales by Salesperson
- Total sales per customer
- Total sales by Product
- Total sales by Zone
- Total sales per month by each salesperson
- Total Sales and Quantities per Customer / Seller
  
> - [Functions.py](https://github.com/E-man85/Algorithms-Python/blob/main/06-Projects/01-SalesAplication/Functions.py)

In this file are all the functions used in this project.

## 07-Data

- [SalesRecords.csv](https://github.com/E-man85/Algorithms-Python/blob/main/07-Data/SalesRecords.csv)

csv file, with some application records, essential for testing the features of 01-SalesApplication.
