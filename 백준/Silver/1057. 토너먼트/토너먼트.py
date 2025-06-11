n,a,b = map(int,input().split())
low = min(a,b)
high = max(a,b)
round = 1
while not(low%2==1 and low+1 == high):
    if low%2==1:
        low= low//2+1
    else:
        low//=2
    if high%2==1:
        high= high//2+1
    else:
        high//=2
    round+=1
print(round)