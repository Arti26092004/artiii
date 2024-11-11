#PROGRAM TO DEMONSTRATE 5 BUILT IN FUNCTIONS IN PYTHON
print("functions")
#step 1
user_input = input("enter list of numbers separated by commas: ")
input_list = user_input.split()
numbers = list(map(int, input_list))
#step 2
total = sum(numbers)
#step 3
length = len(numbers)
#step 4
sorted_num=sorted(numbers)
#step 5
print("original numbers: ", numbers)
print("sum:",total)
print("number of elements: ", length)
print("sorted numbers", sorted_num)
print("\n")
print("Program by Udit Madaan")