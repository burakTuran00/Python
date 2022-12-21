#This lecture will teach the Functions and Variables.

#print("Hello World");

name = input("What's your name? ")   # We take a input from user and To transfrom to the variable.
print("Hello",name);    
 
number = input("What's your number? ");  
print("Your number is "+ number + ".")
print(number + " is your number.")

#print("hello, \"friend\"");

name_1 = input("What's your name: ");
print("Hello",end=" ");
print(name_1);
print("Hello",  name_1, sep="xx")

#print("Hello,\"friend\"")

name_2 = input("What's your name: ");
print(f"hello, {name_2}")

name_3 = input("What's your name: ");
name_3 = name_3.strip(); # this method works like trim.
name_3 = name_3.capitalize();
name_3 = name_3.title();
name_3 = name_3.strip().title().capitalize();
print(f"Hello {name_3}")

name_4 = input("What's your name: ").strip().title();
first,last = name_4.split(" ")
print(f"Hello,{last}");

x = int(input("What's x: "));
y = int(input("What's y: "));
z = float(input("What's z: "));

m = round(x+y+z)
print(m);
print(f"{z:,}");


# This part of Lecture, We'll learn How to define a function. def  :-D

def hello(to):
    print("Hello ",to);



name = input("What's your name: ").strip().title();
hello(name);

surname = input("What's your surname: ");
print("Surname is "+surname);




