import sys

count = int(input())

for n in range(count):
    cmd = sys.stdin.readline().split()
    res = int(cmd[0]) + int(cmd[1])
    print(res)