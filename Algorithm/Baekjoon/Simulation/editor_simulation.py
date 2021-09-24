import sys

target_string: list = list(input())
n: int = int(input())
save_string: list = []

for _ in range(n):
    cmd = sys.stdin.readline().strip().split()
    if cmd[0] == 'L':
        if len(target_string):
            save_string.append(target_string.pop())
    elif cmd[0] == 'D':
        if len(save_string):
            target_string.append(save_string.pop())
    elif cmd[0] == 'B':
        if len(target_string):
            target_string.pop()
    elif cmd[0] == 'P':
        target_string.append(cmd[1])

for _ in range(len(save_string)):
    target_string.append(save_string.pop())

print(''.join(target_string))