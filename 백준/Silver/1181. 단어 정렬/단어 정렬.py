import sys
def main():
    N = int(input())
    list = []
    for i in range(N):
        tmp = input()
        list.append([len(tmp),tmp])
    list.sort(key = lambda x : (x[0], x[1]))

    s = set()
    for idx, ele in list:
        if ele in s:
            continue
        s.add(ele)
        print(ele)


if __name__ == '__main__':
    main()