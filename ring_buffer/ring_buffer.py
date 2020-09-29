class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.index = 0

    def append(self, item):
        # List is empty
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        # List is not empty
        else:
            self.storage[self.index] = item
        self.index += 1
        # If capacity = index
        if self.index == self.capacity:
            self.index = 0

    def get(self):
        return self.storage
