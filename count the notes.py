#taking total amount as the input from the user
amount = int(input("please enter amount for withdraw:"))

#calculation
note1 = amount//100
note2 = (amount%100)//50
note3 = ((amount%100)%50)//10

print("the notes of 100 rupee: ", note1)
print("the notes of 50 rupee: ", note2)
print("the notes of 10 rupee: ", note3)