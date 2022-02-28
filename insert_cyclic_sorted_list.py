###https://www.youtube.com/watch?v=Gk64fs31T6Q
class Solution:
    def insert(head:Node, insertVal:int)->Node:
        ### case 0
        if head is None:
            node = Node(insertVal)
            node.next = node
            return node

        ### find max and min
        mx = head
        while mx.next != head and mx.val <= mx.next.val:
            mx = mx.next
        mini = mx.next
        cur = mini
        ### case 1.1 
        if mini.val >= insertVal or mx.val <= insertVal:
            node = Node(insertVal, mini)
            mx.next = node
        else:
            while cur.next and cur.next.val < insertVal:
                cur = cur.next
            node = Node(insertVal, cur.next)
            cur.next = node

        return head

