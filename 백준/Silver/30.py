#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10610                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dlchdaud04 <boj.kr/u/dlchdaud04>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10610                          #+#        #+#      #+#     #
#    Solved: 2024/08/16 17:34:29 by dlchdaud04    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n = int(input())

sum = ""
n = int(n)
n = str(n)
n = list(n)
n.sort(reverse=True)
for i in n:
    sum += str(i)
if int(sum)%30 != 0:
    print(-1)
else:
    print(sum)
