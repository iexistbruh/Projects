list=[1,2,3,4,5,6,7,8]
print (list)

even,odd = [],[]

for i in list:
    (even if i%2==0 else odd).append(i*i)

print("even square number: ", even)
print("odd square number: ", odd)
