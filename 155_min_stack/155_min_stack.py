
def main(test):
    for test_operation in test:
        if test_operation[0] == "MinStack":
            solution = MinStack()
            
        elif test_operation[0] == "push":
            solution.push(test_operation[1])

        elif test_operation[0] == "pop":
            solution.pop()

        elif test_operation[0] == "top":
            top = solution.top()
            print(top)

        elif test_operation[0] == "getMin":
            min = solution.getMin()
            print(min)
        else: 
            raise ValueError


    print(solution.stack)
    return solution.stack

class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack = [val] + self.stack

    def pop(self) -> None:
        self.stack = self.stack[1:]


    def top(self) -> int:
        return self.stack[0]
        

    def getMin(self) -> int:
        return min(self.stack)


def tests():
    test_0 = zip(["MinStack","push","push","push","getMin","pop","top","getMin"], [[],[-2],[0],[-3],[],[],[],[]])
    return locals().values()

if __name__ == "__main__":
    tests = tests()
    for test in tests:
        main(test)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()