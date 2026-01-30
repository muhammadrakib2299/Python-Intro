class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i

            # Edge handling
            maxLeft1 = float('-inf') if i == 0 else nums1[i - 1]
            minRight1 = float('inf') if i == m else nums1[i]

            maxLeft2 = float('-inf') if j == 0 else nums2[j - 1]
            minRight2 = float('inf') if j == n else nums2[j]

            # Correct partition
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # Odd total length
                if (m + n) % 2 == 1:
                    return float(max(maxLeft1, maxLeft2))
                # Even total length
                return (max(maxLeft1, maxLeft2) +
                        min(minRight1, minRight2)) / 2.0

            # Move binary search
            elif maxLeft1 > minRight2:
                right = i - 1
            else:
                left = i + 1
