""" 
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
 """
def main(test):
    solution = Solution().isValid(test)
    print(solution)
    return solution
    

class Solution:
    def __init__(self):
        self.reverse_paren_dict = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        self.stack = []

    def isValid(self, s: str) -> bool:
         #this is a valid paren
        for char in s:
            if char in self.reverse_paren_dict.values():
                self.stack.append(char)
            elif char in self.reverse_paren_dict.keys():
                #if the stack doesn't exist, or if the first character isn't the compliment of the char
                if not self.stack or self.reverse_paren_dict[char] != self.stack.pop():
                    return False
        return not self.stack

def tests():
    test0 = ["()", True]
    test1 = ["()[]{}", True]
    test2 = ["(]", False]
    test3 = ["([])", True]
    test4 = ["([)]", False]
    return locals().values()

    
if __name__ == "__main__":
    tests = tests()
    for test in tests:
        assert main(test[0]) == test[1]