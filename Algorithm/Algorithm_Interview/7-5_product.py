import sys

num_list: list = list(map(int, sys.stdin.readline().strip().split()))
num_list.sort()

p: list = [1]
q: list = [1]

for i in range(len(num_list)-1):
    p.append(p[len(p)-1]*num_list[i])
    q.append(q[len(q)-1]*num_list[len(num_list)-i-1])

q = list(reversed(q))

res: list = [p[i]*q[i] for i in range(len(p))]
print(f'{res}')