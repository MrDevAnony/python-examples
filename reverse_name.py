name = input("enter your name: ")

# First way
for i in range(len(s)-1, -1, -1):
    print(s[i], end="")
# Second way
print(name[::-1])
