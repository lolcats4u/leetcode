def main():
    stuff = "Hello World"
    solution = Solution()
    print(solution.lengthOfLastWord(s=stuff))


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])


if __name__ == "__main__":
    main()
