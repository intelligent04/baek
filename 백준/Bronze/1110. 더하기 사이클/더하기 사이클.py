cycle = 0
first = input()
num = first
big = 0

while True:  # while True:
    if int(num) < 10:
        num = str(int(num) * 10 + int(num))


    elif int(num[0]) + int(num[1]) < 10:  # 50
        num = num[1] + str(int(num[0]) + int(num[1]))  # num = 0 + 5

    elif int(num[0]) + int(num[1]) >= 10:
        big = str(int(num[0]) + int(num[1]))  # == 10
        num = str(int(num[1])) + str(int(big[1]))  # == 50

    cycle += 1

    if int(str(num)) == int(first):
        print(cycle)
        break