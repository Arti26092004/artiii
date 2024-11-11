roll = (input("Roll_no: "))
name = input("Name: ")
clas = input("Class: ")
Eng= int(input("Enter marks in English"))
Math= int(input("Enter marks in Maths"))
Sci= int(input("Enter marks in Science"))
S_sc= int(input("Enter marks in Social Science"))
comp= int(input("Enter marks in Computer"))
Total= Eng+Math+Sci+S_sc+comp
print("----------------------------------------------")
print(f"Roll No: {roll}")
print(f"Name : {name}")
print(f"Class : {clas}")

print("----------------------------------------------")
print("Subject          Full marks  Marks Obtained")
print(f"English        | 100       | {Eng}")
print(f"Maths          | 100       | {Math}")
print(f"Science        | 100       | {Sci}")
print(f"Social Science | 100       | {S_sc}")
print(f"Computer       | 100       | {comp}")
print("----------------------------------------------")
print(f"Total          | 500       | {Total}")
marksp = Total/5
if marksp >=80.0:
    print("O Grade")
elif marksp <=79.0 and marksp >= 70.0 :
    print("A Grade")
elif marksp <=69.0 and marksp >= 60.0 :
    print("B Grade")
elif marksp <=59.0 and marksp >= 50.0 :
    print("C Grade")
elif marksp <=49.0 and marksp >= 40.0 :
    print("D Grade")
else:
    print("Fail")

print("Program by Udit Madaan")
