# We'll learn Loops. 

# While loop

i = int(input("i: "));
while i != 0:
    print(i);
    i -= 1;

# For loop

number = int(input("What's number: "));

for i in range(number):
    print(i);

#sample
while True:
    n = int(input("What's x: "));
    if n > 0:
        break;
for _ in range(n):
    print(n);

# Sample
def main():
    number = get_number();
    print_Func(number);

def get_number():
    while True:
        n = int(input("What's n: "));
        if n > 0 :
            break;
    return n; 

def print_Func(n):
    for _ in range(n):
        print(n);
       
#sample and Using List.

students = ["Hermione","Harry","Ron","Draco"];
houses = ["Gryffindor","Gryffindor","Gryffindor","Slytherin"];

for student in students:
    print(student);

for i in range(len(students)):
    print(i, students[i]);

# Dict 

newStudents = {
        "Hermione":"Gryffindor",
        "Harry":"Gryffindor",
        "Ron":"Gryffindor",
        "Draco":"Slytherin"
    };

for student in newStudents:
    print(student, students[student], sep=", "); 

# using None
newStudents_2 = [
    {"name": "Hermione" , "house": "Gryffindor","pattronus":"Otter"},
    {"name": "Harry" , "house": "Gryffindor","pattronus":"Stag"},
    {"name": "Ron" , "house": "Gryffindor","pattronus":"Jack Russel terrier"},
    {"name": "Draco" , "house": "Slytherin","pattronus": None},
    ];

for student in newStudents_2:
    print(student["name"],student["house"],student["pottronus"], sep=", ");

#sample

def main():
    print_square(3);

def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#",end="");
        print();

main();