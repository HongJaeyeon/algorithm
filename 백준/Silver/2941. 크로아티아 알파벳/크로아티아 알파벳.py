import sys

input = lambda: sys.stdin.readline().strip()

s = input()
dic = {'c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='}

cur = 0
cnt = 0

while cur < len(s) :
	if cur <= len(s)-2 and s[cur] + s[cur+1] in dic:
		# print("s[cur] + s[cur+1]", s[cur] + s[cur+1])
		cur += 2

	elif cur <= len(s)-3 and s[cur] + s[cur+1] + s[cur+2] == 'dz=':
		# print("cur <= len(s)-3 and s[cur] + s[cur+1] + s[cur+2]", cur <= len(s)-3 and s[cur] + s[cur+1] + s[cur+2])
		cur += 3

	else:
		# print("s[cur]", s[cur])
		cur += 1

	cnt += 1

print(cnt)