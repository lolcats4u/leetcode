from typing import List

def main(test):
    solution = Solution().generateParenthesis(test)
    print(solution)
class Solution:
    def __init__(self):
        self.parentheses_options = [""]
    def generateParenthesis(self, n: int) -> List[str]:
        recursion_depth = 0
        while recursion_depth != n:
            pass


                        

def tests():
    test_1 = 3
    test_2 = 1
    return locals().values()

if __name__ == "__main__":
    tests = tests()
    for test in tests:
        main(test)