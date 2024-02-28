import sys
n= int(input())
nums = list(map(int,sys.stdin.readline().split()))
nums2 = list(set(nums))
nums2.sort()
dic = {}
for i in range(len(nums2)):
    dic[nums2[i]] = i
for i in (nums):
    print(dic[i],sep="",end=" ")