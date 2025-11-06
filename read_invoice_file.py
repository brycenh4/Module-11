import csv

cust_no_input = input("enter customer number: ")
total = 0.0

with open("invoices.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["cust_no"] == cust_no_input:
            total += float(row["inv_total"])
print(f"customer number: {cust_no_input}, total invoice amount ${total:.2f}")