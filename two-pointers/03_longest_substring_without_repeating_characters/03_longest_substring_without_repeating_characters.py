class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_found = 0
        chars = set()
        left = 0
        
        for right in range(len(s)):
            if s[right] not in chars:
                chars.add(s[right])
                max_found = max(max_found, right - left + 1)
            else:
                while s[right] in chars:
                    chars.remove(s[left])
                    left += 1
                chars.add(s[right])
        
        return max_found
