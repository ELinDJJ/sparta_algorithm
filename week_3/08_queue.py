class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():  # 만약 비어있다면,
            self.tail.next = new_node
            self.tail = new_node
        return


def dequeue(self):
    if self.is_empty():
        return "Queue is empty!"  # 만약 비어있다면 에러!
    delete_head = self.head  # 제거할 node 를 변수에 잡습니다.
    self.head = self.head.next
    return

def peek(self):
    if self.is_empty():
        return "Queue is empty!"

    return self.head.data

def is_empty(self):
    return self.head is None

queue = Queue()
queue.enqueue(3)
print(queue.peek())
queue.enqueue(4)
print(queue.peek())
queue.enqueue(5)
print(queue.peek())
print(queue.peek())
