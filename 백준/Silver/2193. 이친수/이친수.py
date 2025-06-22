# 무조건 바텀업 dp
n = int(input())  #        0 1 2 3 4
if n == 1:
    print(1)
else:
    serial_one = [0] * (
        n + 1
    )  # [0,0,1,3(1+1+1),8(3+3+2),] #serial[i] = 2*serial[i-1] + dp[i-1]
    serial_one2 = [0] * (n + 1)  # 1로 시작하면서 연속으로 1나오는 애들
    serial_one[2] = 1
    dp = [0] * (n + 1)  # [0,1,1,2]
    dp[1] = 1

    for i in range(2, n + 1):
        serial_one[i] = 2 * serial_one[i - 1] + dp[i - 1]
        serial_one2[i] = serial_one[i] - serial_one[i - 1]
        dp[i] = 2 ** (i - 1) - serial_one2[i]
    print(dp[n])
