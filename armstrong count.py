number= int(input("Enter lower range: "))
x =int(input("Enter number of count: "))
count = 0
num=number+1
while count < x:
    digit = str(num)
    num_dig = len(digit)
    sum_num = sum(int(digit) ** num_dig for digit in digit)
    if sum_num==num:
        print(num)
        count+=1
    num+=1
print(f"Total armstrong numbers = {count}")
print("Program by Udit Madaan")