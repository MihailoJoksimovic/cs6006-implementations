from ctci.common.classes import *

bst = BinarySearchTree()
bst.insert(50)
bst.insert(40)
bst.insert(60)
bst.insert(30)
bst.insert(45)
bst.insert(20)
bst.insert(43)
bst.insert(48)


print("In-order traversal:")
in_order_traversal(bst.root_node)


print("Pre-order traversal:")
pre_order_traversal(bst.root_node)

print("Post-order traversal:")
post_order_traversal(bst.root_node)

