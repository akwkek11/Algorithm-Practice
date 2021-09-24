import sys
sys.setrecursionlimit(10 ** 4)

class Node(object):
    def __init__(self, key, data=None, count=0, end=False):
        self.key = key
        self.data = data
        self.children = {}
        self.count = count
        self.end = end
class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        current_node = self.head

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]

            # len of word
            current_node.count += 1
        current_node.data = string

        # is it end?
        current_node.children['*'] = Node(None)

cnt: int = 0
def click_count(l, cur):
    global cnt
    if len(cur.children) > 1 or l == 0 or cur.end:
        for c in cur.children:
            cnt += cur.children[c].count
    
    for c in cur.children:
        click_count(l + 1, cur.children[c])

try:
    while True:
        n: int = int(sys.stdin.readline().strip())
        trie: Trie = Trie()
        cnt = 0

        for _ in range(n):
            input_str: str = str(sys.stdin.readline().strip())
            trie.insert(input_str)

        click_count(0, trie.head)

        print("{:,.2f}".format(round((cnt / n), 2)))
except:
    exit(0)

'''
def click_count(count: int, number: int, alphabet: list) -> None:
    global cnt
    for i in alphabet:
        next_list: list = trie.starts_with(i)
        now_alphabet: str = i

        if len(next_list) == 1:
            cnt += count
            continue

        next_list.sort(key = len)
        is_same: bool = True
        next_alp: list = []
        next_number: int = number
        if number == len(next_list[0]):
            cnt += count
            next_number += 1
            for k in next_list:
                if len(k) > len(next_list[0]) and now_alphabet + k[number] not in next_alp:
                    next_alp.append(now_alphabet + k[number])
        else:
            for j in range(number, len(next_list[0])):
                for k in next_list:
                    if k[j] != next_list[0][j]:
                        if now_alphabet + next_list[0][j] not in next_alp:
                            next_alp.append(now_alphabet + next_list[0][j])
                        
                        if now_alphabet + k[j] not in next_alp:
                            next_alp.append(now_alphabet + k[j])

                        is_same = False
                
                if not is_same:
                    next_number = j + 1
                    break

                else:
                    now_alphabet += next_list[0][j]
            
            if len(next_alp) == 0:
                cnt += count
                next_number = len(next_list[0]) + 1
                now_alphabet = next_list[0]
                for k in next_list:
                    if len(k) > len(next_list[0]) and now_alphabet + k[len(next_list[0])] not in next_alp:
                        next_alp.append(now_alphabet + k[len(next_list[0])])

        click_count(count + 1, next_number, next_alp)

while True:
    n: int = int(sys.stdin.readline().strip())
    trie: Trie = Trie()
    cnt = 0
                    
    start_alp: list = []
    for _ in range(n):
        input_str: str = str(sys.stdin.readline().strip())
        trie.insert(input_str)
        if input_str[0] not in start_alp:
            start_alp.append(input_str[0])
                    
    start_alp.sort()
    click_count(1, 1, start_alp)

    print("{:,.2f}".format(round((cnt / n), 2)))
'''