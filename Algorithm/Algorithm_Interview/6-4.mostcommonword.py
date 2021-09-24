from collections import defaultdict

import re
import sys

paragraph: str = str(sys.stdin.readline().strip().split())
banned: str = str(sys.stdin.readline().strip().split())

paragraph = paragraph.lower()
banned = banned.lower()

paragraph = re.sub('[^a-z ]', '', paragraph)
banned = re.sub('[^a-z ]', '', banned)

paragraph_list: list = list(map(str, paragraph.split()))
banned_list: list = []
if ' ' not in banned:
    banned_list.append(banned)
else:
    banned_list = list(map(str, banned.split()))

count_dict: defaultdict = defaultdict(int)

for i in paragraph_list:
    if i not in banned_list:
        count_dict[i] += 1

res: list = sorted(count_dict.items(), key=lambda x: x[1], reverse = True)
print(f'{res[0][0]}')

'''
from collections import Counter

final_list: list = []
for i in paragraph_list:
    if i not in banned_list:
        final_list.append(i)

counts = Counter(final_list)
print(f'{counts.most_common(1)[0][0]}')
'''