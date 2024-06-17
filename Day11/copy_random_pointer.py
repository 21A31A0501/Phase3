#not working but interview answer should be this

# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        if head == None:
            return head 

        store = dict()
        curr = head 
        while curr:
            store[curr.val] = Node(curr.val)
            curr = curr.next 

        curr = head 
        while curr:
            currDeepCopy = store[curr.val]
            if curr.next:
                nextNodeDeepCopy = store[curr.next.val]
                currDeepCopy.next = nextNodeDeepCopy

            if curr.random:
                randomNodeDeepCopy = store[curr.random.val]
                currDeepCopy.random = randomNodeDeepCopy
            curr = curr.next 
        return store[head.val]
        



#optimal one
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        if head == None:
            return None 

        currNode = head 
        while currNode:
            currDeepCopy = Node(currNode.val)
            currDeepCopy.next = currNode.next 
            currNode.next = currDeepCopy 
            currNode = currNode.next.next 

        currNode = head 
        while currNode:
            currDeepCopy = currNode.next 
            if currNode.random:
                currDeepCopy.random = currNode.random.next 

            currNode = currNode.next.next
        
        currNode = head 
        dummyNode = Node(-1)
        tail = dummyNode
        while currNode:
            currDeepCopy = currNode.next 
            tail.next = currDeepCopy 
            tail = tail.next 
            currNode.next = currDeepCopy.next 
            currNode = currNode.next 
        return dummyNode.next