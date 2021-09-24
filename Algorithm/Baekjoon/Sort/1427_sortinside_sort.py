import sys

print(''.join(list(reversed(sorted(list(str(int(sys.stdin.readline().strip()))), key=lambda x : x[0])))))