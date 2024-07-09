# Time Complexity : O(n)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
class Stack:
    def __init__(self):
        self.a_stack = None
        
    def push(self, data):
        new_node = Node(data)
        curr = self.a_stack
        if curr is None:
            curr = new_node
        else:
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node

    def pop(self):
        prev, curr = None, self.a_stack
        if curr is None:
            return None
        while curr.next is not None:
            prev = curr
            curr = curr.next
        # handle case of only one node
        if prev is None:
            self.a_stack = None
            return curr.data

        element = curr.data
        prev.next = None
        return element

a_stack = Stack()
while True:
    #Give input as string if getting an EOF error. Give input like "push 10" or "pop"
    print('push <value>')
    print('pop')
    print('quit')
    do = input('What would you like to do? ').split()
    #Give input as string if getting an EOF error. Give input like "push 10" or "pop"
    operation = do[0].strip().lower()
    if operation == 'push':
        a_stack.push(int(do[1]))
    elif operation == 'pop':
        popped = a_stack.pop()
        if popped is None:
            print('Stack is empty.')
        else:
            print('Popped value: ', int(popped))
    elif operation == 'quit':
        break
