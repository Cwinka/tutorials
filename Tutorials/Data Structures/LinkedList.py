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

class LinkedList:
    def __init__(self, head_node=None):
        self.head_node = head_node

    def push(self, value):
        new_node = Node(value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def pop(self):
        current_node = self.head_node
        self.head_node = self.head_node.get_next_node()
        return current_node.get_value()

    def find_key(self, key):
        current_node = self.head_node
        while current_node is not None:
            if current_node.get_value()[0] == key:
                return current_node.get_value()[1]
            current_node = current_node.get_next_node()
        return print("No such key")


    def __repr__(self):
        current_node = self.head_node
        new_lst = "["
        while current_node.get_next_node() != None:
            new_lst += f"{current_node.get_value()}, "
            current_node = current_node.get_next_node()
        new_lst += str(current_node.get_value()) +"]"
        return new_lst

ll = LinkedList()
for i,y in zip(range(10), range(20,30)):
    ll.push([i, y])
ll.push([5 ,9845])
print(ll.find_key(12))
print(ll)
