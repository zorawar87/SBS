#!/bin/python3
food= [6.20,5.75]
foodsum=0
for i in food:
    foodsum+=i

tip=0.76
tax=0.3
extra = tip+tax

for i in food:
    print(i + i/foodsum *extra)

