height = float(input("Enter Number in cm:"))
weight = float(input("Enter Number in kg:"))

BMI = weight/ (height/100)**2

print("Your BMI is", BMI)

if BMI <= 18.4:
    print("You're underweight")
if BMI <= 24.9:
    print("You're healthy")
if BMI <= 29.9:
    print("You're over weighted")
if BMI <= 34.9:
    print("You're close to getting obeese")
if BMI <= 39.9:
    print("You're obeese")
else:
    print("You're TOO obeese")