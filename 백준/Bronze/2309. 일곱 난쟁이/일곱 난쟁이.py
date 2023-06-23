import sys
selected = [0 for _ in range(7)]
def comb(idx, start, sumValue):
    if sumValue > 100:
        return

    if idx == 7:
        if sumValue == 100:
            selected.sort()
            for ele in selected:
                print(ele)
            sys.exit()
        return

    for i in range(start, 9):
        selected[idx] = ls[i]
        comb(idx+1, i+1, sumValue + ls[i])

ls = [int(input()) for _ in range(9)]
comb(0, 0, 0)