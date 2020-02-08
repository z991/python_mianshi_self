"""
链表（Linked list）是一种常见的基础数据结构，是一种线性表，但是并不会按线性的顺序存储数据，
而是在每一个节点里存到下一个节点的指针(Pointer)。由于不必须按顺序存储，链表在插入的时候可以达到O(1)的复杂度，
比另一种线性表顺序表快得多，但是查找一个节点或者访问特定编号的节点则需要O(n)的时间，而顺序表相应的时间复杂度分别是O(logn)和O(1)。
"""

"""
1.反转链表 1->2->3->4->5->Null    5->4->3->2->1->Null
"""
def reverseList(head):
    cur, prev = head, None
    while cur:
        cur.next, prev, cur = prev, cur, cur.next
        return prev


"""
2.链表相邻节点反转  1->2->3->4->5  2->1->4->3->5
"""


def swapPairs(self, head):
    pre, pre.next = self, head
    while pre.next and pre.next.next:
        a = pre.next
        b = a.next
        pre.next, b.next, a.next = b, a, b.next
        pre = a
    return self.next

"""
3.判断一个链表是否有环
  1. 直接遍历链表的节点,把节点地址存到一个set集合，判断是否有重复的
  2. 一个快指针（一次遍历两个节点），一个慢指针（一次遍历一个节点），如果快指针的节点地址和慢指针的地址相同则表示有环
"""
