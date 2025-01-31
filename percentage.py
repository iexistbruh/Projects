# take marks as input from user
print("Enter Marks obtained in 4 subjects: ")
math = int(input("math: "))
english = int(input("english: "))
science = int(input("science: "))
language = int(input("language: "))

# percentage
sum = math + english + language + science
print("sum of math, english, science, language", sum)

perc = (sum/400)*100
print(end="Percentage Mark =")
print(perc)