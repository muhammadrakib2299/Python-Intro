class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Start with the first string as the initial common prefix
        prefix = strs[0]
        
        # Compare prefix with each string in the array
        for string in strs[1:]:
            # Reduce the prefix by checking common part with each string
            while not string.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""  # No common prefix, return empty string
        
        return prefix
