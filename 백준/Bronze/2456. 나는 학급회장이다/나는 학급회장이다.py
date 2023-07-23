import sys

one = []
two = []
three = []

n = int(sys.stdin.readline())
data = [(sys.stdin.readline().strip()).split() for i in range(n)]

for i in data:
    one.append(int(i[0]))
    two.append(int(i[1]))
    three.append(int(i[2]))

a = int(sum(one))
b = int(sum(two))
c = int(sum(three))

li123 = sorted(
    [
        [a, one.count(3), one.count(2), 1, a],
        [b, two.count(3), two.count(2), 2, b],
        [c, three.count(3), three.count(2), 3, c],
    ]
)

li = [a, b, c]
li = sorted(li)


if a > b and a > c:
    print(1, sum(one))
elif b > a and b > c:
    print(2, sum(two))
elif c > b and c > a:
    print(3, sum(three))
else:
    if li123[2][1:2] == li123[1][1:2]:
        print(0, max([a, b, c]))
    else:
        print(li123[2][3], li123[2][4])
