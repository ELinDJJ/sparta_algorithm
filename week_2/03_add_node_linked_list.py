class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

    def add_node(self, index, value):
        new_node = Node(value)  # [6]
        if index == 0:
            new_node.next = self.head # [6] -> [5]
            self.head = new_node # head _> [6] -> [5] -> ....

        node = self.get_node(index - 1) # [5]
        next_node = node.next #[ 12]
        node.next = new_node # [5] -> [6]
        new_node.next = next_node # [6] -> [12]

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)
# print(linked_list.get_node(1).data) # -> 5를 들고 있는 노드를 반환해야 합니다!
# [5] -> [12] -> [8] 로 만들어졌다


# [5] -> [6] -> [12] -> [8] 로 만들어보기
linked_list.add_node(1, 6)
linked_list.print_all()

