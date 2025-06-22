def solution(bandage, health, attacks):
    mhealth = health
    stack = 0
    i = [0,0]
    while i[0] <= attacks[-1][0]:
        if i[0] != attacks[i[0]][0]:
            attacks.insert(i[0],i[:])
        i[0]+=1
    for i in attacks:
        if i[1] == 0 and health<mhealth:
            health += bandage[1]
            stack += 1
            if stack == bandage[0]:
                health += bandage[2]
                stack = 0
        if health > mhealth:
            health = mhealth
        if i[1] != 0:
            health -= i[1]
            stack = 0
    
        if health <= 0:
            health = -1
            break
    return health