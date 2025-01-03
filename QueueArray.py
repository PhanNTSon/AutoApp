class QueueArray:
    def __init__(self, size) -> None:
        self.queue = []
        self.size = size
    
    def isEmpty(self):
        return len(self.queue) == 0

    def isFull(self):
        return len(self.queue) == self.size
    
    def enQueue(self, data):
        if (self.isFull() is False):
            self.queue.append(data)
            return True
        else:
            return False

    def deQueue(self):
        if (self.isEmpty()):
            return None
        else:
            return self.queue.pop(0)

    def isContains(self, data):
        return data in self.queue
    
    def display(self):
        for i in self.queue:
            print(f"{i}",end=", ")


