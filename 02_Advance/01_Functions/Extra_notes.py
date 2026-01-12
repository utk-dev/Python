#function definition
def calc_sum(a,b): #parameters
    return a+b

sum = calc_sum(1,2) #function call; arguments(arg1,arg2)
print(sum)

#recursion

def show(n):
    if(n == 0):   #base case(use to decide where should recursion stop)
        return
    print(n)
    show(n-1)

show(8)

def fact(n):
    if(n==0 or n==1):
        return 1
    return fact(n-1)*n

print(fact(4))
