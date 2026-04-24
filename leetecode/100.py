class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # both are null
        if not p and not q:
            return True
        
        # one is null or values differ
        if not p or not q or p.val != q.val:
            return False
        
        # check left and right
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)