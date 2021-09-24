from collections import defaultdict

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

def solution(word_list: list) -> list:
    res_list: list = []
    reverse_trie: Trie = Trie()
    for word in word_list:
        reverse_trie.insert(word[::-1])

    word_to_index: defaultdict = defaultdict(lambda : -1)
    for index, word in enumerate(word_list):
        word_to_index[word] = index

    for word in word_list:
        target_list: list = reverse_trie.starts_with(word)
        if target_list is not None:
            for target_word in target_list:

                reverse_target_word: str = target_word[::-1]
                res_word1: str = ''.join([word, reverse_target_word])
                res_word2: str = ''.join([reverse_target_word, word])

                if word_to_index[word] != word_to_index[reverse_target_word]:
                    if res_word1 == res_word1[::-1] and [word_to_index[word], word_to_index[reverse_target_word]] not in res_list:
                        res_list.append([word_to_index[word], word_to_index[reverse_target_word]])
                    if res_word2 == res_word2[::-1] and [word_to_index[reverse_target_word], word_to_index[word]] not in res_list:
                        res_list.append([word_to_index[reverse_target_word], word_to_index[word]])

    return res_list

print(f'{solution(["abcd", "dcba", "lls", "s", "sssll"])}')
print(f'{solution(["bat", "tab", "cat"])}')