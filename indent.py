#Proper indentation
print("indentation")
def my_function():
        print("this is properly indented")
        if True:
            print("this is inside an if statement")
#properly indented function
def my_other_function():
    print("this will not cause an error")
for i in range(5):
    print(i)

my_function()
my_other_function()