def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    li = [video_len,pos,op_start,op_end]
    li2 = []
    for i in li:
        a,b = map(str,i.split(":"))
        i = int(a)*60 + int(b)
        li2.append(i)
        
    video_len=li2[0]
    pos=li2[1]
    op_start=li2[2]
    op_end=li2[3]
    
    if pos<= op_end and pos>= op_start:
        pos = op_end
    
    for cmd in commands:
        if pos<= op_end and pos>= op_start:
            pos = op_end
        if cmd =='next':
            if pos+10<= video_len:
                pos +=10
            else:
                pos = video_len
        elif cmd =='prev':
            if pos-10>= 0:
                pos -=10
            else:
                pos = 0
                
    if pos<= op_end and pos>= op_start:
        pos = op_end
    
    a = pos//60
    b = pos%60
    if a//10 == 0:
        a = "0"+str(a)
    if b//10 == 0:
        b = "0"+str(b)
    answer=str(a)+":"+str(b)
    return answer