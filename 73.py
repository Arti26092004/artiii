def print_num(num1,num2):
    even=[]
    odd=[]
    div=[]
    for num in range (num1,num2+1):
        if num%5==0:
            div.append(num)
        elif num%2==0:
            even.append(num)
        else:
            odd.append(num)
    print("even numbers:",even)
    print("odd numbers: ",odd)
    print("divisible by 5",div)
num1=int(input("enter 1st number: "))
num2=int(input("enter 2nd number: "))
print_num(num1,num2)
print("Program by Udit Madaan")
