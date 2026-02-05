from typing import List
from copy import copy

def main(test):
    solution = Solution().generateParenthesis(test)
    print(solution)
class Solution:
    def __init__(self):
        self.parentheses_options = []
    def generateParenthesis(self, n: int) -> List[str]:
        def case_1(parenthesis_string:str, count:int) -> str:
            if len(parenthesis_string) != (2*count):
                return (parenthesis_string + f"({case_1(parenthesis_string, n)})")
            else:
                return parenthesis_string

        def case_2(parenthesis_string, count:int) -> str:
            if len(parenthesis_string) != (2*count): 
                return (parenthesis_string + f"(){case_2(parenthesis_string, n)}")
            else:
                return parenthesis_string
        
        def branch_case(parenthesis_string:str, count, parenthesis_options:list, *cases):
            for case in cases:
                parenthesis_string += branch_case(case(parenthesis_string), count, parenthesis_options, cases)
            parenthesis_options.append(parenthesis_string)
        
        branch_case("", n, self.parentheses_options, case_1, case_2)

def tests():
    test_1 = 3
    test_2 = 1
    return locals().values()

if __name__ == "__main__":
    tests = tests()
    for test in tests:
        main(test)