try:
    num1, num2 =eval(input("Enter 2 numbers, separated by a comma: "))
    result = num1 / num2
    print("result is", result)

except ZeroDivisionError:
    print("Divison by zero is error!!")

except SyntaxError:
    print("Comma is missing. Enter numbers separated by comma like 1, 2")

except:
    print("Wrong input")

else:
    print("No exceptions")

finally:
    print("This is execute no matter what")