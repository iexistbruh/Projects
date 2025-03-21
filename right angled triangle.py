#Take Input
print("Half Pyramid Patterns of Stars")
n = int(input("Enter the Numbers of Rows: "))
#outer loop to handle rumber of rows
for i in range(n):
    #inner loop to handle number of columns
    for j in range(i+1):
        #display result
        print("* ", end="")
    print()