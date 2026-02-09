class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Step 1: In-order traversal to get the sorted values
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        # Step 2: Helper function to build the balanced BST from sorted values
        def build_balanced_bst(sorted_values):
            if not sorted_values:
                return None
            
            # Choose the middle element as the root to maintain balance
            mid = len(sorted_values) // 2
            root = TreeNode(sorted_values[mid])
            
            # Recursively build the left and right subtrees
            root.left = build_balanced_bst(sorted_values[:mid])
            root.right = build_balanced_bst(sorted_values[mid+1:])
            
            return root
        
        # Step 3: Get the sorted values from the BST
        sorted_values = inorder(root)
        
        # Step 4: Build and return the balanced BST
        return build_balanced_bst(sorted_values)
