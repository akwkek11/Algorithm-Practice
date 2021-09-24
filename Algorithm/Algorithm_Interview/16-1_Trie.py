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
        
        is_unique = False
        index: int = 0
        for char in string:
            if char not in current_node.children:
                if not is_unique:
                    is_unique = True
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]

            # len of word
            current_node.count += 1
            index += 1
        
        if current_node.data is None and not is_unique:
            is_unique = True
        current_node.data = string

        # is it end?
        current_node.children['*'] = Node(None)

        # if already inserted -> False
        # else -> True
        return False if not is_unique else True

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

trie: Trie = Trie()
print(trie.insert('apple'))
print(trie.search('apple'))
print(trie.search('app'))
print(trie.starts_with('app'))
print(trie.insert('app'))
print(trie.search('app'))
print(trie.insert('apple'))