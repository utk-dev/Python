def greet(name, ending = "Thank You"):   #here default value of ending is entered 'Thank You' so, ending is 'default parameter'
    print("Good Morning", name)
    print(ending)

greet("Mohit")
greet("Rohit", "Thanks")