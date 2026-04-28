class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # Step 1: Flatten grid
        nums = [num for row in grid for num in row]
        
        # Step 2: Check feasibility
        remainder = nums[0] % x
        for num in nums:
            if num % x != remainder:
                return -1
        
        # Step 3: Sort
        nums.sort()
        
        # Step 4: Find median
        median = nums[len(nums) // 2]
        
        # Step 5: Compute operations
        operations = 0
        for num in nums:
            operations += abs(num - median) // x
        
        return operations