import sys
sys.setrecursionlimit(10 ** 5)

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
    for c in cur.children:
        if c != '*':
            cnt += cur.children[c].count
    
    for c in cur.children:
        if c != '*' and cur.children[c].count >= 2:
            click_count(l + 1, cur.children[c])

def solution(words: list) -> int:
    global cnt
    trie: Trie = Trie()
    for word in words:
        trie.insert(word)
    
    click_count(0, trie.head)
    answer: int = cnt
    return answer

print(solution(["go","gone","guild"]))
print(solution(["abc","def","ghi","jklm"]))
print(solution(["word","war","warrior","world"]))
print(solution(["hello","hell","heaven","goodbye"]))