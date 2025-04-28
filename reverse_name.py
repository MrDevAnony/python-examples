name = input("enter your name: ")

index = len(name) - 1

reversed_name = ""

while 0 <= index:
    reversed_name = reversed_name + name[index]
    index = index - 1

print(reversed_name)