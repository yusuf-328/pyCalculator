# Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
# Perform the operation based on the user's input and print the result.
# Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.

#answer
#ask user for input
num1 = float(input("enter the first number:"))
num2 = float(input ("enter the second number"))
operation = input("Enter an operation (+, -, *, /):")

#perform the operation:
if operation == "+" :
   result = num1 + num2
   print(f"{num1} + {num2} = {result}")

elif operation == "-" :
   result = num1 - num2
   print(f"{num1} - {num2} = {result}")

elif operation == "*" :
   result = num1 * num2
   print(f"{num1} * {num2} = {result}")


elif operation == "/" :
   if num2 != 0:
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")
   else:
    print ("Error: cannot divide by zero.")
#if the user does not iput any of the above, it prints this:       
else:
     print ("Invalid operation. please use +, -, *,or /.")



 