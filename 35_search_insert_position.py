# Given a sorted array of distinct integers and a target value,
# return the index if the target is found. If not, return the index
# where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.


def main():
    nums = [1, 3, 5, 6]
    target = 0
    solution = Solution()
    stuff = solution.searchInsert(nums, target)
    print(stuff)


class Solution:
    def __init__(self):
        self.index = 0
        self.original_list = None

    def searchInsert(self, nums: list, target: int) -> int:
        half_len = len(nums) // 2
        if self.original_list is None:
            self.original_list = nums

        if len(nums) == 1:
            if target > nums[0]:
                self.index = self.index
            else:
                self.index = self.index + 1
        else:
            if nums[half_len] > target:
                self.index = self.index + (half_len - 1)
                self.searchInsert(nums[0:half_len], target)
            else:
                self.index = self.index + half_len
                self.searchInsert(nums[half_len:], target)

        return self.index


if __name__ == "__main__":
    main()
