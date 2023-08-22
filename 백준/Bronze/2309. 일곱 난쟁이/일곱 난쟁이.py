height_li = []

for i in range(9):
    h = int(input())
    height_li.append(h)
height_li = sorted(height_li)
bb = 1

for a in range(3):
    for b in range(1, 4):
        for c in range(2, 5):
            for d in range(3, 6):
                for e in range(4, 7):
                    for f in range(5, 8):
                        for g in range(6, 9):
                            if (
                                int(
                                    height_li[a]
                                    + height_li[b]
                                    + height_li[c]
                                    + height_li[d]
                                    + height_li[e]
                                    + height_li[f]
                                    + height_li[g]
                                )
                                == 100
                            ) and bb == 1:
                                print(
                                    height_li[a],
                                    "\n",
                                    height_li[b],
                                    "\n",
                                    height_li[c],
                                    "\n",
                                    height_li[d],
                                    "\n",
                                    height_li[e],
                                    "\n",
                                    height_li[f],
                                    "\n",
                                    height_li[g],
                                    sep="",
                                )
                                bb = 0