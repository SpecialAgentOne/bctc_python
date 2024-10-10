sales_tax = 0.07 #tax is 7% by task
item1, item2, item3, item4, item5 = input("Enter the price for item: "), input("Enter the price for item: "), input("Enter the price for item: "), input("Enter the price for item: "), input("Enter the price for item: ")

subtotal = float(item1) + float(item2) + float(item3) + float(item4) + float(item5)
tax_amout = subtotal * sales_tax
sales_total = subtotal + tax_amout

print(f"Subtotal: {subtotal:.2f}\n Sales tax: {tax_amout:.2f}\n Total: {sales_total:.2f}")