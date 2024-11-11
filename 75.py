def first_even(numbers):
    for n in numbers:
        if n % 2 == 0:
            return n
    return None
nums = [1, 3, 5, 8, 9]
print(first_even(nums))

print("Program by Udit Madaan")
