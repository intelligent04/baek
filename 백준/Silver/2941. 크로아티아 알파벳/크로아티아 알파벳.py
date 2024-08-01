#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2941                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dlchdaud04 <boj.kr/u/dlchdaud04>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2941                           #+#        #+#      #+#     #
#    Solved: 2024/08/01 15:33:20 by dlchdaud04    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

a = input()
length = len(a)
for i in range(len(a)-1):
    if a[i] == 'c':
        if a[i+1] == '=' or a[i+1] == '-':
            length -= 1
    elif a[i] == 'd':
        if a[i+1] == '-':
            length -= 1
        if a[i+1] == 'z':
            if i+2 < len(a):
                if a[i+2] == '=':
                    length -= 1
    elif a[i] == 'l' and a[i+1] == 'j':
        length -= 1
    elif a[i] == 'n' and a[i+1] == 'j':
        length -= 1
    elif a[i] == 's' and a[i+1] == '=':
        length -= 1
    elif a[i] == 'z' and a[i+1] == '=':
        length -= 1
print(length)
            
