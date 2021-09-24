from collections import deque

import sys

# Aho-Corasick
class State:
    sid = None
    value = None
    isFinal = False
    tranList = None
    failState = 0
    outputSet = None

    def __init__(self, sid, val):
        self.sid = sid
        self.value = val
        self.tranList = {}
        self.failState = 0
        self.outputSet = set()

    def goto(self, key):
        if key in self.tranList:
            return self.tranList[key]

    def addOutput(self, key):
        self.outputSet = self.outputSet ^ key

    def display(self):
        print("State:", self.sid, "Outgoing:", len(self.tranList.keys()), "Failure:", self.failState)

        if self.isFinal == True:
            print(" +--Output:", self.outputSet)

        for node in self.tranList.keys():
            s = self.tranList[node]
            s.display()
class AhoCorasick:
    root = None
    sid = 0
    table = {}

    def __init__(self):
        self.root = State(0, None)
        self.table[0] = self.root

    def addKeyword(self, keyword):
        current = self.root

        for key in keyword:
            if key not in current.tranList:
                self.sid = self.sid + 1
                current.tranList[key] = State(self.sid, key)
                self.table[self.sid] = current.tranList[key]

            current = current.tranList[key]

        current.isFinal = True
        current.outputSet.add(keyword)
    def setFailure(self):
        queue = deque()
        current = self.root

        for k in self.root.tranList:
            queue.append(self.root.tranList[k])

        while len(queue) != 0:
            r = queue.popleft()
            for k in r.tranList:
                queue.append(r.tranList[k])
                nd = r.tranList[k]
                sid = r.failState
                value = nd.value
                current = self.table[sid]

                while True:
                    if current.goto(value) == None and current.sid != 0:
                        new_sid = current.failState
                        current = self.table[new_sid]
                    else:
                        break
                child = current.goto(value)

                if child == None:
                    nd.failState = current.sid
                else:
                    nd.failState = child.sid

                nd.addOutput(self.table[nd.failState].outputSet)

    def findString(self, str):
        current = self.root

        count = 0
        for key in str:
            # print("Check:", key)
            while True:
                if current.goto(key) == None and current.sid != 0:
                    current = self.table[current.failState]
                    # print("failure:", current.sid)
                else:
                    child = current.goto(key)
                    break
            if child != None:
                current = child
                if len(child.outputSet) > 0:
                    return True

        return False

    def display(self):
        self.root.display()

if __name__ == "__main__":
    x = AhoCorasick()
    N: int = int(sys.stdin.readline().strip())
    for _ in range(N):
        pattern: str = str(sys.stdin.readline().strip())
        x.addKeyword(pattern)
    x.setFailure()

    Q: int = int(sys.stdin.readline().strip())
    for _ in range(Q):
        target: str = str(sys.stdin.readline().strip())
        print('YES') if x.findString(target) else print('NO')
