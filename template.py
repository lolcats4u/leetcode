from typing import *
def main(test):
    solution = Solution().some_func()
    print(solution)

class Solution:
    def some_func():
        pass

def tests():
    pass
    return locals().values()

if __name__ == "__main__":
    tests = tests()
    for test in tests:
        main(test)