# Task: Implement a graph representation and breadth and depth first searches

from __future__ import annotations

class Node:

    def __init__(self, value):
        self.children = [] # Array of Nodes
        self.value = value

    def addChild(self, child: Node):
        self.children.append(child)
        return self

class Graph:
    def __init__(self, nodes):
        self.nodes = nodes

    def getNodes(self):
        return self.nodes

zeroNode = Node(0).addChild(Node(1))

oneNode = Node(1).addChild(Node(2))

twoNode = Node(2).addChild(Node(0))

threeNode = Node(3).addChild(Node(2))

graph = Graph([zeroNode, oneNode, twoNode, threeNode])






