class QueueArray:
    def __init__(self) -> None:
        self.queue = []
    
    def isEmpty(self):
        return len(self.queue) == 0

    
    def enQueue(self, data):
        self.queue.append(data)

    def deQueue(self):
        if (self.isEmpty()):
            return None
        else:
            return self.queue.pop(0)

    def display(self):
        for i in self.queue:
            print(f"{i}",end=", ")


