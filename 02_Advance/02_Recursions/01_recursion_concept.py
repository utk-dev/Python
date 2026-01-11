#Recursion - it is a function which calls itself. Generally used to directly use a mathematical formula as function
'''
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2 x 1
factorial(3) = 3 x 2 x 1
factorial(4) = 4 x 3 x 2 x 1
factorial(5) = 5 x 4 x 3 x 2 x 1
.
.
factorial(n) = n x (n-1) x .... x 3 x 2 x 1
or
factorial(n) = n x factorial(n-1)
'''
#a machine to find factorial of any number
n = int(input("Enter the number: "))

def factorial(n):
    if(n==0 or n==1):
        return 1
    return n*factorial(n-1)


print("The factorial of the number is: ", factorial(n))

''' The programmer needs to be extremely careful while working with recursion to ensure that the function doesn't infinitely keep calling
itself. Recursion is sometimes the most direct way to code an algorithm'''
