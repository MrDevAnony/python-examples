list = [4,5,3,1,4,2,3,5,8,15]
z=0
f=0

for i in list:
    if i % 2 == 1:
        f = f + 1
    else:
        z = z + 1

print("zoj ha: ", z, "Fard ha: ", f)