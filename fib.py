#!/usr/bin/python3

fibnum = int(input("Enter number of fib values: "))
fiblist = []

for i in range(fibnum):
    if i < 2:
        fiblist.append(i)
    else:
        fiblist.append((fiblist[i-1]+fiblist[i-2]))

print(fiblist)

