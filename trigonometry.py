import math

angle = float(input("Enter angle in degrees: "))

radian = math.radians(angle)

print("sin({}) = {:.4f}".format(angle, math.sin(radian)))
print("cos({}) = {:.4f}".format(angle, math.cos(radian)))
print("tan({}) = {:.4f}".format(angle, math.tan(radian)))
