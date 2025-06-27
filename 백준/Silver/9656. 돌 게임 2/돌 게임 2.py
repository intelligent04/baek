n = int(input())
li = ["SK", "CY"]
turn = False
if n>6:
    while n < 7:
        n -= 3
        turn = not turn

if n % 2 == 0:
    print(li[int(turn)])
else:
    print(li[int(not turn)])
