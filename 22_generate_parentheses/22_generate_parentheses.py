from typing import List
from copy import copy

def main(test):
    solution = Solution().generateParenthesis(test)
    print(solution)
class Solution:
    def __init__(self):
        self.parentheses_options = []
    def generateParenthesis(self, n: int) -> List[str]:
        count_case_1 = n
        count_case_2 = n
        def case_1(n,paren_option, options):
                if n != 0:
                    n -=1
                    paren_option_1 = paren_option + f"({self.generateParenthesis(n)})"
                    paren_option_2 = case_2(n, paren_option_1, options)

                else: 
                    options.append(paren_option_1, paren_option_2)

        def case_2(n, paren_option, options):
            if n != 0:
                n -= 1
                paren_option_1 = paren_option + f"(){self.generateParenthesis(n)}"
                paren_option_2 += case_1(n, paren_option_1, options)
            else:
                options.append(paren_option_1, paren_option_2)
        
        while count_case_1 != 0 and count_case_2 != 0:
            case_1(count_case_1, "", self.parentheses_options)
            case_2(count_case_2, "", self.parentheses_options)

def tests():
    test_1 = 3
    test_2 = 1
    return locals().values()

if __name__ == "__main__":
    tests = tests()
    for test in tests:
        main(test)