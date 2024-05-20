def main():
    solution = Solution()
    hay = "sadbutsad"
    needle = "sad"
    solution.strStr(hay, needle)


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            return haystack.index(needle)
        except ValueError:
            return -1
