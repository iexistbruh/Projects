#Take input from user
rows = int(input("Please Enter the total Number of Rows: "))
number = 1 #initialise by 1

print("Flod's Triangle")
#outer loop for numbers of rows
for i in range(1, rows + 1):
    #inner loop for number of columns
    for j in range(1, i + 1):
        #display result
            print(number, end = '')
            number = number + 1
    print()