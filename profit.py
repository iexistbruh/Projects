actual_cost = float(input("amount of the actualy product: "))
sale_amount = float(input("amount of the sales: "))

if (sale_amount>actual_cost):
    amount = sale_amount - actual_cost
    print("Total Profit = {0}".format(amount))
else:
    print("No Profit")