import csv
with open("students.csv", mode="r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        first_name, last_name, phone_number, birthdate = row
        full_name = f"{first_name} {last_name}"
        print(f"Name: {full_name:<20} Phone: {phone_number:<25} Birthdate: {birthdate}")