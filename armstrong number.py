num = int(input("Enter a number: "))
digit=str(num)
num_dig=len(digit)
sum_num = sum(int(digit) ** num_dig for digit in digit)
if sum_num == num:
    print(f"{num} is Armstrong number")
else:
    print(f"{num} Is not an armstrong number")
print("Program by Udit Madaan")