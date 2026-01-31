from typing import List
def main(test):
    print(Solution().triangularSum(test))

def tests():
    test_1 = [1,2,3,4,5] 
    test_2 = [5]
    return locals().values()

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            new_sum_list = []
            for i in range(len(nums)-1):
                new_sum_list.append(((nums[i] + nums[i+1]) % 10))
            return self.triangularSum(new_sum_list)

if __name__ == "__main__":
    tests = tests()
    for test in tests:
        main(test)