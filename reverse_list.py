adad = [1,2,3,4,5,6,7]

# With built-in reversed class
for i in reversed(adad):
    print(i)

print ("------")

# Without built-in reversed class

for i in (adad[::-1]):
    print(i)
