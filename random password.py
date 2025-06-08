import random

def make_password(length):
    upper = [chr(i) for i in range(65, 91)]     
    lower = [chr(i) for i in range(97, 123)]     
    digits = [str(i) for i in range(10)]       
    symbols = ['@', '#', '$', '%', '&', '*']     

    chars = upper + lower + digits + symbols
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

length = int(input("Enter password length: "))
print("Your password is:", make_password(length))
