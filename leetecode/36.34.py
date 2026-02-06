class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        # Sort the array first
        nums.sort()
        
        # Initialize two pointers
        start = 0
        max_len = 0
        
        # Iterate with the 'end' pointer
        for end in range(len(nums)):
            # Check the condition for the current window
            while nums[end] > nums[start] * k:
                start += 1  # Shrink the window from the left
            
            # Update the max_len of valid subarray
            max_len = max(max_len, end - start + 1)
        
        # The minimum removals is the total elements minus the longest valid subarray
        return len(nums) - max_len
