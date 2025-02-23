import random
from typing import List

aList = []
for i in range(5):
    aList.append(random.randrange(1, 50))

print(f"unsorted list: {aList}")

#bubble sort
iterations