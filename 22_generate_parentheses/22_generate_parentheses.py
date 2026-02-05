from typing import List
from copy import copy

def main(test):
    solution = Solution().generateParenthesis(test)
    print(solution)
class Solution:
    def __init__(self):
        self.parentheses_options = []
    def generateParenthesis(self, n: int) -> List[str]:
        def case_1(parenthesis_string:str) -> str:
            return (parenthesis_string + f"({case_1(parenthesis_string, n)})")

        def case_2(parenthesis_string) -> str:
            return (parenthesis_string + f"(){case_2(parenthesis_string, n)}")
        
        def branch_case(parenthesis_string:str, count, parenthesis_options:list, *cases):
            for case in cases:
                parenthesis_string = ""
                while len(parenthesis_string) != (count *2):
                    parenthesis_string = branch_case(case(parenthesis_string), count, parenthesis_options, cases)
                parenthesis_options.append(parenthesis_string)

def tests():
    test_1 = 3
    test_2 = 1
    return locals().values()

if __name__ == "__main__":
    tests = tests()
    for test in tests:
        main(test)