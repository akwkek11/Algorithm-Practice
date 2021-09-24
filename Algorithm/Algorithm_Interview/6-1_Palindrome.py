import re
import sys

s: str = str(sys.stdin.readline().strip())

s = s.lower()
s = re.sub('[^a-z0-9]', '', s)
list_s : list = list(s)
reversed_s : list = list(reversed(list_s))
if list_s == reversed_s:
    print('true')
else:
    print('false')