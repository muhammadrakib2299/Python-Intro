class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        from functools import lru_cache
        
        @lru_cache(None)
        def build(start, end):
            if start > end:
                return (None,)
            
            trees = []
            for root_val in range(start, end + 1):
                for left in build(start, root_val - 1):
                    for right in build(root_val + 1, end):
                        root = TreeNode(root_val)
                        root.left = left
                        root.right = right
                        trees.append(root)
            
            return tuple(trees)
        
        return list(build(1, n))