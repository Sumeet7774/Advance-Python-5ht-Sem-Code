import csv

with open("data.csv",'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        orderid = row["Order ID"]
        customername = row["Customer Name"]
        productname = row["Product Name"]
        quantity = row["Quantity"]
        unitprice = row["Unit Price"]