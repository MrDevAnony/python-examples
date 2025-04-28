adad = [1,2,3,4,5,6,7]

# With built-in reversed class
for i in reversed(adad):
    print(i)

print ("------")

# Without built-in reversed class
index = len(adad) - 1

while 0 <= index:
    print (adad[index])
    index = index - 1