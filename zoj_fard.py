list_ = [4,5,3,1,4,2,3,5,8,15]
# Using loop
numbers = {}
for i in list_:
    if i % 2 == 0:
        numbers["even"] = numbers.get("even", 0) + 1
    else:
        numbers["odd"] = numbers.get("odd", 0) + 1
print("zoj ha: ", numbers["even"], "Fard ha: ", numbers["odd"])

# Using filter
even = len(list(filter(lambda x:x%2==0, list_)))
odd = len(list(filter(lambda x:x%2!=0, list_)))
print("zoj ha: ", even, "Fard ha: ", odd)

# Using map
from collections import Counter
divided_numbers = Counter(list(map(lambda x:x%2, list_)))
print("zoj ha: ", divided_numbers[0], "Fard ha: ", divided_numbers[1])
