##loops are used to iterate a particular value


#WHILE loop

#printing table of a number till 10
number = int(input("Enter the number: "))

i = 1  #initializing the value of i
while i<11:   #providing a condition after while loop
    print(number * i)
    i+=1                #this statement is v.v important to exit the infinite loop situation



# for understanding 'for' loop we need to understand 'range' function which is written in the form of (start,stop,step)
n = list(range(1,21,2))
print(n)    #output will be - [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]- this means that the starting point was 1 and ending was 21 and the number was skipped by 2


#FOR loop

for i in range(0,11,2):   #eg 1.
    print(i)

for i in "Kolkata":       #eg 2.
    print(i)

for i in {1:"Krishna", 2:"Rahul", 3:"Mohit"}:
    print(i)
