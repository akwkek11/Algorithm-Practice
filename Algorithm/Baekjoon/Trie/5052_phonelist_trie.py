from collections import defaultdict

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

T: int = int(sys.stdin.readline().strip())

for _ in range(T):
    n: int = int(sys.stdin.readline().strip())
    trie: Trie = Trie()
    phone_list: defaultdict = defaultdict(int)
    is_started: bool = False

    for _ in range(n):
        number: str = str(sys.stdin.readline().strip())
        phone_list[number] = 1
        trie.insert(number)

    for key in phone_list.keys():
        if len(trie.starts_with(key)) >= 2:
            is_started = True
            break
    
    print('YES') if not is_started else print('NO')