n = int(input())
cnt = n
for _ in range(n):

    word = input()
    word_list = list(word)
    
    nomore = []
    for  i in range(len(word_list)):
        if word_list[i] in nomore:
            if word_list[i] != word_list[i-1]:
                cnt -= 1
                break
        else:
            nomore.append(word_list[i])

print(cnt)
