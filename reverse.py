#program to reverse a string
print("reversing a string")
my_str="Bharati"
rev_str=""

for char in my_str:
    rev_str=char+rev_str
print("original str",my_str)
print("reversed str:",rev_str)
#alt
#print(my_str[::-1])
