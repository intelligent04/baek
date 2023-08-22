n = int(input())
i = 2
goal = n
output_li = []

while i <= goal:
    while n % i == 0:
        n = n // i
        output_li.append(i)
    i += 1

for i in range(len(output_li)):
    print(output_li[i])