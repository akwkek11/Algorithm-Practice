import sys
sys.setrecursionlimit(10 ** 4)

class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}
class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        current_node = self.head

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        current_node.data = string

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

def search_all_words(target: list, depth: int) -> None:
    print_word: str = '--' * depth + target[-1]
    print(f'{print_word}')

    next_words: list = []
    next_lists: list = trie.starts_with(target)
    if next_lists is not None:
        for select_list in next_lists:
            if len(select_list) > len(target) and select_list[len(target)] not in next_words:
                next_words.append(select_list[len(target)])
    
    next_words.sort()
    for i in next_words:
        target.append(i)
        search_all_words(target, depth + 1)
        target.pop()

trie: Trie = Trie()

N: int = int(sys.stdin.readline().strip())
word_list: list = []
start_word_list: list = []
for _ in range(N):
    input_str = list(map(str, sys.stdin.readline().strip().split()))
    word_list.append(input_str[1:])

    if input_str[1] not in start_word_list:
        start_word_list.append(input_str[1])

start_word_list.sort()
for word in word_list:
    trie.insert(word)

for i in start_word_list:
    search_all_words([i], 0)