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

class HashTable:
    def __init__(self, max_size):
        self.max_size = max_size
        self.size = 0
        self.array = [None for i in range(max_size)]

    def hash_fanc(self, key, number_of_collisions=0):
        hash = key.encode()
        hash_value = sum(hash)
        return hash_value + number_of_collisions
    def compressor(self, hash_value):
        return hash_value%self.max_size

    def push(self, key, value):
        array_index = self.compressor(self.hash_fanc(key))
        current_value = self.array[array_index]

        if current_value is None:
            self.array[array_index] = [key, value]
            return
        if current_value[0] == key:
            self.array[array_index] = [key, value]
            return

        number_of_collisions = 1
        while current_value[0] != key:
            array_index = self.compressor(self.hash_fanc(key, number_of_collisions))
            current_value = self.array[array_index]

            if current_value is None:
                self.array[array_index] = [key, value]
                return
            if current_value[0] == key:
                self.array[array_index] = [key, value]
                return
            number_of_collisions += 1
        return

    def retrieve(self, key):
        array_index = self.compressor(self.hash_fanc(key))
        possible_value = self.array[array_index]

        if possible_value is None:
            return None

        if possible_value[0] == key:
            return possible_value[1]

        number_of_collisions = 1
        while possible_value[0] != key:
            array_index = self.compressor(self.hash_fanc(key, number_of_collisions))
            possible_value = self.array[array_index]

            if possible_value is None:
                return None

            if possible_value[0] == key:
                return possible_value[1]
            number_of_collisions += 1
        return





hh = HashTable(400)
for i in range(201):
    hh.push(str(i), str(i))
print(hh.retrieve("50"))
# O(N) либо Омега(1)
