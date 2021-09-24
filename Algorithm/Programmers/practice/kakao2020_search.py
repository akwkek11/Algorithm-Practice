# Trie
class Node(object):
    def __init__(self, key, data=None, count=0):
        self.key = key
        self.data = data
        self.children = {}
        self.count = 0
class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        current_node = self.head

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
            current_node.count += 1

        current_node.data = string

    def starts_with(self, prefix):
        current_node = self.head
        count: int = 0

        for p in prefix:
            if p in current_node.children:
                current_node = current_node.children[p]
            else:
                return 0

        if prefix == '':
            for i in current_node.children.values():
                count += i.count
            return count
        else:
            return current_node.count

def solution(words: list, queries: list) -> list:
    trie: list = [Trie() for _ in range(10001)]
    reverse_trie: list = [Trie() for _ in range(10001)]
    answer: list = []
    for word in words:
        trie[len(word)].insert(word)
        reverse_trie[len(word)].insert(word[::-1])

    for query in queries:
        query_len: int = len(query)
        length_check: int = 0
        if query[0] == '?':
            res_query = query.split('?')[-1]
            print(res_query)
            length_check = reverse_trie[query_len].starts_with(res_query[::-1])
            #print(res_query, length_check)
        else:
            res_query = query.split('?')[0]
            print(res_query)
            length_check = trie[query_len].starts_with(res_query)
            #print(res_query, length_check)

        if length_check is None:
            answer.append(0)
        else:
            answer.append(length_check)
    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?", "??????"]))