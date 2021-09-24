class MyCircularQueue:
    circular_queue: list = []
    queue_size: int = 0
    start_pointer: int = 0
    end_pointer: int = 0

    def __init__(self, size: int):
        self.circular_queue = [None for _ in range(size)]
        self.queue_size = size
        self.start_pointer = 0
        self.end_pointer = 0

    def enQueue(self, input_object) -> bool:
        if self.end_pointer - self.start_pointer in [self.queue_size-1, -1]:
            return False
        else:
            if self.circular_queue[self.end_pointer] is not None:
                self.end_pointer += 1
                if self.end_pointer == self.queue_size:
                    self.end_pointer = 0
            
            self.circular_queue[self.end_pointer] = input_object
            return True

    def Rear(self) -> object:
        return self.circular_queue[self.end_pointer]

    def isFull(self) -> bool:
        return not (self.end_pointer - self.start_pointer in [self.queue_size-1, -1])

    def deQueue(self) -> object:
        if self.circular_queue[self.start_pointer] is None:
            return False
        else:
            result: object = self.circular_queue[self.start_pointer]
            self.circular_queue[self.start_pointer] = None
            if self.start_pointer != self.end_pointer:
                self.start_pointer += 1
                if self.start_pointer == self.queue_size:
                    self.start_pointer = 0
            
            return True

    def Front(self) -> object:
        return self.circular_queue[self.start_pointer]

    def isEmpty(self) -> bool:
        return self.start_pointer == self.end_pointer and self.circular_queue[self.start_pointer] is None

circularQueue: MyCircularQueue = MyCircularQueue(5)
print(circularQueue.enQueue(10))
print(circularQueue.enQueue(20))
print(circularQueue.enQueue(30))
print(circularQueue.enQueue(40))
print(circularQueue.enQueue(50))
print(circularQueue.enQueue(60))
print(circularQueue.Rear())
print(circularQueue.isFull())
print(circularQueue.deQueue())
print(circularQueue.deQueue())
print(circularQueue.enQueue(70))
print(circularQueue.Rear())
print(circularQueue.Front())
print(circularQueue.enQueue(80))
print(circularQueue.enQueue(100))
print(circularQueue.Rear())
print(circularQueue.Front())
print(circularQueue.deQueue())
print(circularQueue.deQueue())
print(circularQueue.deQueue())
print(circularQueue.enQueue(100))
print(circularQueue.deQueue())
print(circularQueue.deQueue())
print(circularQueue.deQueue())
print(circularQueue.deQueue())
print(circularQueue.isEmpty())