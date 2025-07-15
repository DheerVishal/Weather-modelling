# Stage C: Read coefficients and time from file safely
try:
    with open("weather_input.txt", "r") as f:
        # Remove empty lines and strip whitespace
        lines = [line.strip() for line in f if line.strip()]

    # Check if we have at least 4 valid values
    if len(lines) < 4:
        print("❌ Error: File must contain at least 4 non-empty lines for a, b, c, t.")
        exit()

    # Convert to float
    a = float(lines[0])
    b = float(lines[1])
    c = float(lines[2])
    t = float(lines[3])

    # Calculate temperature
    T = a * t**2 + b * t + c
    print(f"✅ At time {t} hours, the temperature is {T:.2f}°C")

except FileNotFoundError:
    print("❌ Error: File 'weather_input.txt' not found.")
except ValueError:
    print("❌ Error: File contains non-numeric data.")
except Exception as e:
    print(f"❌ Unexpected error: {e}")
