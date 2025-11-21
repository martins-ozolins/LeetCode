class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s = [0 for _ in range(26)]
        count_t = [0 for _ in range(26)]

        for c in s:
            count_s[ord(c) - ord("a")] += 1

        for c in t:
            count_t[ord(c) - ord("a")] += 1

        return count_s == count_t
