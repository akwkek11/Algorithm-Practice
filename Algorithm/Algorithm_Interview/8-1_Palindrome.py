from collections import deque

import re
import sys

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head: ListNode) -> bool:
    rev = None
    slow = fast = head

    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next
    
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    
    return not rev

def linked_list_print(l: ListNode) -> None:
    if l is None: 
        return ''
    return str(l.val)+'->'+linked_list_print(l.next)

s: str = str(sys.stdin.readline().strip())
s = s.lower()
s = re.sub('[^a-z0-9]', '', s)
list_s: list = list(s)
l1: ListNode = ListNode(s[0])
next_node = l1
for i in range(1, len(s)):
    next_node = next_node.next
    next_node = ListNode(s[i])

print(f'{linked_list_print(next_node)}')
print(f'{isPalindrome(l1)}')