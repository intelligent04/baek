import sys

n = int(sys.stdin.readline())
data = [(sys.stdin.readline().strip()).split() for i in range(n)]
li = []
li2 = []
dic = {
    "A+": 4.3,
    "A0": 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B0": 3.0,
    "B-": 2.7,
    "C+": 2.3,
    "C0": 2.0,
    "C-": 1.7,
    "D+": 1.3,
    "D0": 1.0,
    "D-": 0.7,
    "F": 0.0,
}

for i in range(n):
    li.append(float(data[i][1]))
    li2.append(float(data[i][1]) * float(dic[data[i][2]]))

a = round(sum(li2) / ((sum(li))) + 0.000000000001, 2)
print(f"{a:.2f}")
