# We'll learn Conditionals.

# > greater than 
# < less than 
# >= grater than or equal to 
# <= less than or equal to
# == equal 
# != not equal 

x = int(input("What's x: "));
y = int(input("What's y: "));

# Sample One
if x < y : 
    print("x is less than y.");
elif x > y:
    print("x is greater than y.");   
else:
    print("x is equal to y.");

# Sample Two
if x < y or x > y:
    print("x is not equal to y.");
else:
    print("x is equal to y.");

# Sample Three
if x != y:
    print("x is not equal to y.");
else:
    print("x is equal to y.");

# Sample Four
if x == y:
    print("x is equal to y.");
else:
    print("x is not equal to y.");

# Another Sample and using and operator.
score = int(input("Score: "));

if score >= 90 and score <= 100:
    print("Grade: A");

elif score >= 80 and score < 90:
    print("Grade: B");

elif score >= 70 and score < 80:
    print("Grade: C");

elif score >= 60 and score < 70:
    print("Grade: D");

else:
    print("Grade: F");


# + addition
# - subtraction 
# * multiplecation 
# / division
# % mod or modular arithmetic

if x % 2 == 0:
    print("Even");
else:
    print("Odd"); 

# Even or Odd with Function and using Boolen. True or False
def main():
    number = int(input("What's number: "));
    if is_even(number):
        print("Even");
    else:
        print("Odd");

def is_even(n):
    if n % 2 == 0:
        return True;
    else:
        return False;

def is_odd(n):
    return False if n % 2 == 1 else True;

def  better_way(n):
    return (n % 2 == 0)
# if it's correct, it'll retrun true. else false. 

main();

# Match 

name = input("What's your name: ");

match name:
    case "Harry" | "Dumbel":
        print("Griyffindor");
    case "Hermione":
        print("Griyffinodor");
    case "Ron":
        print("Griyffindor");
    case "Draco":
        print("Slytherin");
    case _:
        print("Who?");

# | = or



