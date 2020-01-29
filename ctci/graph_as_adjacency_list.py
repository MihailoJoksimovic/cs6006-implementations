# Task: implement graph as an adjacency list

from __future__ import annotations

class Node:

    def __init__(self, value, next = None):
        self.value = value
        self.next = next

vertices = [
    Node(1, Node(4)), #0
    Node(2, Node(3, Node(4))), #1
    Node(1, Node(3)), #2
    Node(1, Node(4)), #3
    Node(0, Node(1))
]

def visit(node: Node):
    print(node.value)

def depth_first_search(root: Node, visited):
    """Runs a depth first search, starting from root node"""

    # Reachable nodes

    visited[root.value] = True

    reachable_node = vertices[root.value]

    while reachable_node is not None:
        if reachable_node.value in visited:
            if reachable_node.next:
                reachable_node = reachable_node.next

                continue
            else:
                break

        visited[reachable_node.value] = True

        depth_first_search(reachable_node, visited)

        reachable_node = reachable_node.next

    visit(root)



    # Iterate through all nodes that root can reach:



depth_first_search(Node(0), {})



