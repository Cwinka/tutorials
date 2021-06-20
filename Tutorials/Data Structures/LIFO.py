class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def get_value(self):
        return self.value

    def set_next_node(self, next_node):
        self.next_node = next_node

    def __repr__(self):
        return f"{self.value}"

class Stack:
    def __init__(self):
        self.top_node = None
        self.size = 0


    def push(self, value):
        self.size += 1
        new_node = Node(value)
        if self.top_node is None:
            self.top_node = new_node
            return
        new_node.set_next_node(self.top_node)
        self.top_node = new_node

    def pop(self):
        current_node = self.top_node
        if self.size > 0:
            self.top_node = current_node.get_next_node()
            self.size -= 1
            return current_node
        else:
            print("Stack is empty")

    def peek(self):
      if self.size > 0:
        return self.top_node.get_value()
      else:
        print("No orders waiting!")

ss = Stack()
ss.push(321)
ss.push(22)
ss.push(31)
for i in range(1000001):
    ss.push(i)

def first_value_in_stack():
    while ss.size is not 1:
        ss.pop()
    return ss.peek()

print(first_value_in_stack())
# O(N)
