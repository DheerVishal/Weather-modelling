# Stage A: Hardcoded Coefficients and Time
a = -0.5
b = 4
c = 10
t = 5  # time in hours

T = a * t**2 + b * t + c
print(f"At time {t} hours, the temperature is {T:.2f}°C")
