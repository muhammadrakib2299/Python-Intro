class Solution:
    def inorderTraversal(self, root):
        res = []
        
        def dfs(node):
            if not node:
                return
            dfs(node.left)        # Left
            res.append(node.val) # Root
            dfs(node.right)      # Right
        
        dfs(root)
        return res