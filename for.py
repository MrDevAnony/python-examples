list = [5, 14, 28, 30, 26, 45]
tedad = 0
for i in list:
    if i > 29:
        tedad = tedad + 1
        print("Tedad: ", tedad, " | ", i, " is Bigger than 29: ")
        
    else:
        print(i, " is smaller than 29")