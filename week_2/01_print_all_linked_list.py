

# 노드안에는 data, next가 있어야 한다

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node = Node(3)
first_node = Node(4)
node.next = first_node
print(node.next)
print(node.data)
print(node.next.data)


class LinkedList: # head node만 가지고있으면 된다
    def __init__(self, data):
        self.head = Node(data)


# [3] -> [4] -> [5] ... append 사용
    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        self.head.next = Node(data)
        cur = self.head
        print("cur is", cur.data)
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)

# [3] → [5] → [6] → [8] -> None 을 코드로 구현
# head -> cur -> cur->cur->None



linked_list = LinkedList(3)

print(linked_list.head)

def print_all(self):
    cur = self.head
    while cur is not None:
        print(cur.data)
        cur = cur.next


LinkedList.print_all()

