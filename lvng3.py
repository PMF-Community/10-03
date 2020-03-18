import math as m
x = float(input())

if x <= 0:
    print(m.pow(x, 2))
elif x > 0 and x <=100:
    #staviti format ovdje
    print((100-x)/(m.pow(x,4)))
else:
    print(200)
