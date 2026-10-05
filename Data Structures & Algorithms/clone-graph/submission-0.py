"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def dfs(node: Node, new_nodes: dict[int, 'Node']):
            if node.val in new_nodes: return
            new_nodes[node.val] = Node(val = node.val)
            for n in node.neighbors:
                dfs(n, new_nodes)
                new_nodes[node.val].neighbors.append(new_nodes[n.val])
            return
        if not node: return None
        new_nodes = {}
        dfs(node, new_nodes)
        return new_nodes[1]