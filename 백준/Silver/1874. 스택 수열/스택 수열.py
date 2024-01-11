import copy
t = int(input())
li1 = [] # 입력순서
li2 = [] # 입력받은거 내림차순 정렬
li3 = [] # 출력 리스트
seq = 0
for i in range(t):
    li1.append(int(input()))
    li2.append(li1[i])
li2.sort(reverse=True)
li22 = copy.deepcopy(li2) # 입력받은거 오름차순 정렬
li2.reverse()
out = []
tru = 1

li3.append(li22.pop())
out.append('+')
while len(li3)>=0:
        if(len(li3) > 0):
            if(li1[seq] <li3[-1]):
                print("NO")
                tru = 0
                break
            elif(li3[-1] == li1[seq]):
                li3.pop()
                out.append('-')
                seq+=1
            else:
                li3.append(li22.pop())
                out.append('+')
        else:
            if len(li22)>0:
                li3.append(li22.pop())
                out.append('+')
            else:
                break
# if(out.count('+') != t or out.count('-') != t):
#      print("NO")
if(tru==1):
    for i in range(len(out)):
        print(out[i])