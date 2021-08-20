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


def get_linked_list_sum(linked_list_1, linked_list_2):
    sum_1 = 0
    head_1 = linked_list_1.head
    while head_1 is not None:
        # sum_1 += head_1.data 이 경우 6 + 7+ 8=21이 된다
        sum_1 = sum_1 * 10 + head_1.data  # 각 자리에 10을 곱하고 더해준다
        head_1 = head_1.next

    sum_2 = 0
    head_2 = linked_list_1.head
    while head_2 is not None:
        # sum_1 += head_1.data 이 경우 6 + 7+ 8=21이 된다
        sum_2 = sum_2 * 10 + head_2.data  # 각 자리에 10을 곱하고 더해준다
        head_2 = head_2.next

    print(sum_1)
    print(sum_2)
    return sum_1 + sum_2

def get_linked_list_sum(linked_list_1, linked_list_2):
    sum_1 = _get_linked_list_sum(linked_list_1)
    sum_2 = _get_linked_list_sum(linked_list_2)

    return sum_1 + sum_2

def _get_linked_list_sum(linked_list): # 위의 식을 중복되지 않게 다시 구현
    sum = 0
    head = linked_list.head
    while head is not None:
        sum = sum * 10 + head.data  # 각 자리에 10을 곱하고 더해준다
        head = head.next



# [6]head -> [7] -> [8]의 구조
linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

# [3]head -> [5] -> [3]의 구조
linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))
