# Stage D: Multiple sets of inputs from file
def calculate_temperature(a, b, c, t):
    return a * t**2 + b * t + c

with open("weather_inputs.txt", "r") as f:
    for line in f:
        a, b, c, t = map(float, line.strip().split())
        T = calculate_temperature(a, b, c, t)
        print(f"For a={a}, b={b}, c={c}, t={t} => Temperature: {T:.2f}°C")
