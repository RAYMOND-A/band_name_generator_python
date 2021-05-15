
print("Day 1 - Python Print Function")
print("The Function is declared like this:")
print("print('what to print')")

# separates strings into different(new) lines using one print function 
print("Hello world!\nHello world!")

# string concatenation
print("Hello" + " " + "Ray")

print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with backslash and n.")

#input() will get user input from console
name = input("what is your name? ")

# this gets the length of the inputted text
print(len(name))
print(name)

# how to switch the value of the two variables a and b
a = input("a:")
b = input("b:")

print("a is =" + a + " and " + "b is =" + b)

c = a
a = b
b = c

print("a is = " + a)

print("b is = " + b)



# Band Name Generator project

print("Welcome to the Band Name Generator.")

city_name = input("What's the name of the city you grew up in?\n")
pet_name = input("What's the name of your favourite pet?\n")

print("Your band name could be " + city_name + " " + pet_name)
