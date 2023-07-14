li = [
    "baby",
    "sukhwan",
    "tururu",
    "turu",
    "very",
    "cute",
    "tururu",
    "turu",
    "in",
    "bed",
    "tururu",
    "turu",
    "baby",
    "sukhwan",
]  # 14개임

n = int(input())
n = n - 1
cycle = n // 14  # cycle 0부터 시작
index = n - cycle * 14
a = 2 + cycle
b = 1 + cycle

if index in [2, 3, 6, 7, 10, 11]:
    li[index] = li[index] + ("ru" * cycle)
    if len(li[index]) >= 12:
        if index == 2 or index == 6 or index == 10:
            print(f"tu+ru*{a}")
        elif index == 3 or index == 7 or index == 11:
            print(f"tu+ru*{b}")
    elif len(li[index]) < 12:
        print(li[index])
else:
    print(li[index])