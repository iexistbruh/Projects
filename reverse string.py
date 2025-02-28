#Input a words or sentence
string = input("Please enter your string: ")

string2 = ('')
#loop for printing in reverse
for i in string:
    string2 = i + string2

print("\nThe OriginalString = ", string)
print("The Reversed String= ", string2)