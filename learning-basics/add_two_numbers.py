# Python3 program to add two numbers
x=4
y=6

#then add
add=x+y

#print
print(" the Sum of number :",add)

# Python3 program to add two numbers

x=input("first number please:")
y=input(" second number please:")

# Adding two numbers
# User might also enter float numbers
Sum=int(x)+int(y)
# Display the sum
# will print value in float
print("The sum of {0} and {1} is {2}" .format(x,y, Sum))

#To define a function that take two integers 
# and return the sum of those two numbers
def addtion(a,b):
    return a+b
#initializing the variables
num1 = 10
num2 = 5

#function calling and store the result into sum_of_twonumbers
sum_of_twonumbers = addtion(num1,num2)

#To print the result
print("Sum of {0} and {1} is {2};" .format(num1,
                           num2, sum_of_twonumbers))

# Python3 program to add two numbers

num1 = 15
num2 = 12

# Adding two nos
import operator
su = operator.add(num1,num2)

# printing values
print("Sum of {0} and {1} is {2}" .format(num1,
                                       num2, su))
# Define a lambda function to add two numbers
add_numbers = lambda x, y: x + y

# Take input from the user
num1 = 1
num2 = 2

# Call the lambda function to add the two numbers
result = add_numbers(num1, num2)

# Print the result
print("The sum of", num1, "and", num2, "is", result)
class Calculator:
    def add(self, num1, num2):
        return num1 + num2

# Example usage:
calc = Calculator()
result = calc.add(10, 20)
print(result)

