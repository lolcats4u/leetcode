from typing import List
test_1 = [2,7,11,15]
head_1 = 9
def main(test:list, target):
    solution = Solution()
    solution.twoSum(test, target)
    print(solution)

class Solution:
    def __init__(self):
        self.sum = None
    
    def __str__(self):
        return str(self.sum)

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hash_table.keys():
                self.sum = [i, hash_table[diff]]
                return
            hash_table[num] = i
        self.sum = []
        return

if __name__ == "__main__":
    main(test_1, head_1)