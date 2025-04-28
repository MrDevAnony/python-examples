list_ = [5, 14, 28, 30, 26, 45]

for i in list(filter(lambda x:x>29, list_)):
    print( i, " is Bigger than 29: ")
        
for i in list(filter(lambda x:x<29, list_)):
    print(i, " is smaller  than 29")
