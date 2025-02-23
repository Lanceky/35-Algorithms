import random
import math
#generating a random list
aList = []
for i in range(5):
    aList.append(random.randrange(1,50))

print(f"unordered list : {aList} ")
print()
#bubble sort
iterations = len(aList) -  1
while iterations > 1:
    j=0
    while j < iterations:
        if aList[j] > aList[j+1]:
            #swap them
            temp = aList[j]
            aList[j] = aList[j+1]
            aList[j+1] = temp
        j += 1
    iterations -= 1

for num in aList:
    print(num, end=",")