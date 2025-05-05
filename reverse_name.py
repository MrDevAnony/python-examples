name = input("enter your name: ")

# First way
for i in range(len(name)-1, -1, -1):
    print(name[i], end="")
print()
# Second way
print(name[::-1])
# My way                                      index = len(name) - 1
reversed_name = ""
while 0 <= index:
    reversed_name = reversed_name + name[inde>
    index = index - 1
print(reversed_name)
