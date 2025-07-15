# Stage B: User Inputs Coefficients and Time
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
t = float(input("Enter time (t): "))

T = a * t**2 + b * t + c
print(f"At time {t} hours, the temperature is {T:.2f}°C")
