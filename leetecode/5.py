class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Helper function to expand around the center
        def expandAroundCenter(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # After the while loop, the valid palindrome is s[left+1:right]
            return s[left+1:right]

        if not s:
            return ""
        
        longest = ""
        
        for i in range(len(s)):
            # Odd length palindrome (center is a single character)
            palindrome1 = expandAroundCenter(i, i)
            # Even length palindrome (center is between two characters)
            palindrome2 = expandAroundCenter(i, i + 1)
            
            # Update longest palindrome if needed
            longest = max(longest, palindrome1, palindrome2, key=len)
        
        return longest
