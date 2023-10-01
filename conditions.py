# CS104
# First name Last name
# conditions.py


temp = int(input("Please enter the current temperature: "))

if temp > 90:
    print("Wear Shorts")
elif temp > 70:
    print("Short Sleeves are fine")
elif temp > 50:
    print("Wear a jacket")
elif temp > 32:
    print("Wear a heavy coat")
else:
    print("Stay Inside")
