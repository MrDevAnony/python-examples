name = input("enter your name: ")

# First way
for i in range(len(s)-1, -1, -1):
    print(s[i], end="")
# Second way
print(name[::-1])
# My way
index = len(name) - 1
reversed_name = ""
while 0 <= index:
    reversed_name = reversed_name + name[index]
    index = index - 1
print(reversed_name)
