#comment

"""
multiline comment
"""


def add(a, b):
    """

    a(int,float): First number
    b(int,float): Second number
    """
    return a + b


def subtract(a, b):
    """

    a(int,float): First  number
    b(int,float): Second number
    """
    return a - b


sum = add(3, 5)
print(sum)
sub = subtract(7, 3)
print(sub)

if __name__ == "__main__" :
    x,y=10,5

print(f"sum of {x} and {y} is {add(x,y)}")
print(f"difference of {x} and {y} is {subtract(x,y)}")

