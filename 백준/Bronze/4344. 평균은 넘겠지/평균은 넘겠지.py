import sys

t = int(input())


for i in range(t):
    over = 0
    data = list(map(int, sys.stdin.readline().split()))
    average = sum(data[1:]) / (len(data) - 1)

    for ii in range(1, len(data)):
        if data[ii] > average:
            over += 1
    a = (over / (len(data) - 1)) * 100
    b = str(round(a, 3))
    ind = b.index(".")

    while len(b) - ind < 4:
        b = b + "0"

    print(b, "%", sep="")