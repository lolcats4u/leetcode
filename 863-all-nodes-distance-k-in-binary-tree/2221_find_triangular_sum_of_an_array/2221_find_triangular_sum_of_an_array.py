from typing import List
def main(test):
    print(Solution().triangularSum(test))

def tests():
    test_1 = [1,2,3,4,5] 
    test_2 = [5]
    return locals().values()

class Solution:
    def __init__(self):
        self.triangular_sum = None
    def triangularSum(self, nums: List[int]) -> int:
        if not self.triangular_sum:
            if len(nums) == 1:
                self.triangular_sum = nums[0]
                return self.triangular_sum
            else:
                new_sum_list = []
                for i, val in enumerate(nums):
                    try:
                        new_sum_list.append((val + nums[i + 1]) % 10)
                    except IndexError:
                        self.triangularSum(new_sum_list)
                


if __name__ == "__main__":
    tests = tests()
    for test in tests:
        main(test)