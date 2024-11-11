class Countdown:
     def __init__(self, n):
        self.n = n

     def __iter__(self):
        while self.n > 0:
             yield self.n
             self.n -= 1

for number in Countdown(5):
     print(number)
print("Program by Udit Madaan")