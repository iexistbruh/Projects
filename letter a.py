a = input("Enter word: ")
for i in a:
    if (i=='A' and i=='a'):
        print("A found")
        break
    elif (i=='A' or i=='a'):
        print('A found')
        break
else:
    print("A is not found")
    