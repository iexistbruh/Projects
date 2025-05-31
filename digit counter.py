n = int(input("Your no. :"))
amount = 0 
while n > 0:
    n //= 10
    amount += 1
print(amount)
