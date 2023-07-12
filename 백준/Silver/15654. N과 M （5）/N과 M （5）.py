from itertools import permutations

N, M = map(int, input().split())
N_list = list(map(int, input().split()))
N_list = sorted(N_list) #순서대로 나오게 정렬 먼저

for numbers in list(permutations(N_list, M)):
    for num in numbers:
        print(num, end=' ')
    print()