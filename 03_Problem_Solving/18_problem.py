c = int(input("Enter the temperature in celcius: "))

def c_to_f(c):
    f=(((9/5)*c)+32)
    return f

print(f"Temperature in farenhiet is: {round(c_to_f(c),2)}°F")  #round is used to round off the decimal places to the assigned places
