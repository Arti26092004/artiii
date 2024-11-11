sent = input("Enter a sentence")
up = 0
low = 0
for i in sent:
    if i.islower():
        low += 1
    else:
        up += 1
print("No. of lower case", low)
print("No. of upper case", up)
