#calculator from user input

# a = float(input("Enter The First Number: "))
# b = input("Enter the operation (+, -, *, /): ")
# c = float(input("Enter the Second Number: "))
#
# if b == "+":
#     result = a + c
# elif b == "-":
#     result = a - c
# elif b == "*":
#     result = a * c
# elif b == "/":
#     if c != 0:  # Corrected division by zero check
#         result = a / c
#     else:
#         result = "Error: Division by zero is not allowed"
# else:
#     result = "Invalid Operation"
#
# print("The Result Is:", result)




import time

# Get the current time
currentTime = time.strftime('%H:%M:%S %p')

# Extract the current hour and convert it to an integer (24-hour format)
#currentHour = int(time.strftime('%H'))

print("Current time is -", currentTime)

# Check the time and print appropriate greeting
if currentTime <="12":
    print("Good Morning")
elif currentTime <"18":
    print("Good Evening")
else:
    print("Good Night")




