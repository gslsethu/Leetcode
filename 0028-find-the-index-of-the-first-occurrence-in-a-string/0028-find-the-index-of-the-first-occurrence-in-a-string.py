class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h=haystack.find(needle)
        if h!=-1:
            return h
        return -1
        