low= int(input("Enter lower range: "))
high=int(input("Enter higher range: "))
count =0
for i in range (low,high+1):
    num = i
    digit = str(num)
    num_dig = len(digit)
    sum_num = sum(int(digit) ** num_dig for digit in digit)
    if sum_num == num:
        print(f"{num} is Armstrong number")
        count=count+1
    else:
        continue
print(f"Total armstrong numbers between {low} and {high} = {count}")
print("Program by Udit Madaan")