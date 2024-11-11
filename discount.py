bill = int(input("Enter the bill amount: "))
total_sum= sum(int(digit) for digit in str(bill))


if bill < 10000:
    print(f"total bill is : {bill}")
    discount= 1/2*total_sum
    print(f"discount %: {discount}%")
    Final_bill= bill - bill*discount/100
    print(f"Amount to be paid : {Final_bill}")
else:
    print(f"total bill is : {bill}")
    discount = total_sum
    print(f"discount %: {discount}%")
    Final_bill = (bill - bill * discount / 100)
    print(f"Amount to be paid : {Final_bill}")
print("Program by Udit Madaan")
