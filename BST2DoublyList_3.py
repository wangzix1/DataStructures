##https://jimmy-shen.medium.com/leetcode-426-convert-binary-search-tree-to-sorted-doubly-linked-list-5f66b3a143a8

if not root:
    return 
dummy = Node(0,None, None)
prev = dummy
stack, node = [], root
while stack or node:
    while node:
        stack.append(node)
        node = node.left
    node = stack.pop()
    node.left, prev.right, prev  = prev, node, node
    node = node.right
dummy.right.left, prev.right = prev, dummy.right
return dummy.right



