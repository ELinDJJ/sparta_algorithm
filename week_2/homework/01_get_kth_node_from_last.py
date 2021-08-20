# 링크드 리스트 끝에서 K번째 값 출력
# 1차 개선) 링크트 리스트는 자신의 뒤에 오는 다음 값만을 알고있기 때문에
# 링크드 리스트를 한 바퀴 돌아 길이를 알아낸 다음, 그 길이에서 K만큼을 빼기기

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

    def get_kth_node_from_last(self, k):
        slow = self.head
        fast = self.head

        for i in range(k):
            fast = fast.next

        while fast is not None:
            slow = slow.next
            fast = fast.next

        return slow

linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다! 끝에서 두 번째 위치한 숫자가 출력되도록


# 2차 개선) 포인터를 2개 사용
# 연산횟수가 적다고 무조건 빠르고 효율적인 수행은 아닐 수 있다는 것을 기억하기
