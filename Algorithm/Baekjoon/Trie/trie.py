import re
import sys

class Node(object):
    def __init__(self, key, data=None, count=0):
        self.key = key
        self.data = data
        self.children = {}
        self.count = count
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

    def search(self, string):
        current_node = self.head

        for char in string:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return False

        if current_node.data:
            return True
        else:
            return False

    def starts_with(self, prefix):
        current_node = self.head
        words = []

        for p in prefix:
            if p in current_node.children:
                current_node = current_node.children[p]
            else:
                return None

        current_node = [current_node]
        next_node = []
        while True:
            for node in current_node:
                if node.data:
                    words.append(node.data)
                next_node.extend(list(node.children.values()))
            if len(next_node) != 0:
                current_node = next_node
                next_node = []
            else:
                break

        return words

def click_count(l: int, cur: Trie) -> None:
    global cnt
    if len(cur.children) > 1 or l == 0 or cur.end:
        for c in cur.children:
            cnt += cur.children[c].count
    
    for c in cur.children:
        click_count(l + 1, cur.children[c])

trie: Trie = Trie()
reverse_trie: Trie = Trie()
cnt: int = 0
word_list: list = ["frodo", "front", "firefox", "fire"]
for word in word_list:
    trie.insert(word)

'''
    How To Reverse String

    word: str = 'Hello, world!'
    word = word[::-1]
    >> !dlrow ,olleH
'''

for word in word_list:
    reverse_trie.insert(word[::-1])


print(trie.starts_with('fire'))
print(trie.starts_with(''))
N: int = int(sys.stdin.readline().strip())
for _ in range(N):
    input_str: str = str(sys.stdin.readline().strip())
    reverse_side = False
    if input_str.startswith('?'):
        input_str = input_str[::-1]
        reverse_side = True
    
    input_str_length: int = len(input_str)
    input_str = re.sub(r'[?]', '', input_str)
    res_list: list = [s for s in trie.starts_with(input_str) if len(s) == input_str_length] if not reverse_side else [s[::-1] for s in reverse_trie.starts_with(input_str) if len(s) == input_str_length]
    print(f'{res_list}')

# click_count(0, trie.head)
# print("{:,.2f}".format(round((cnt / len(word_list)), 2)))
