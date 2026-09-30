# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        q = collections.deque()
        q.append(root)
        node_list = []
        while q:
            node = q.popleft()
            if node == None:
                node_list.append("N")
            else:
                node_list.append(str(node.val))
                q.append(node.left) if node.left else q.append(None)
                q.append(node.right) if node.right else q.append(None)
        
        return "#".join(node_list)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = collections.deque(data.split("#"))
        q = collections.deque()
        val = vals.popleft()
        if val == "N" or val == "": 
            return None
        
        root = TreeNode(val=int(val))
        q.append(root)

        while q:
            node = q.popleft()
            left = vals.popleft()
            right = vals.popleft()
            if left != "N":
                node.left = TreeNode(int(left))
                q.append(node.left)
            
            if right != "N":
                node.right = TreeNode(int(right))
                q.append(node.right)

        return root



