# Given a sorted array of distinct integers and a target value,
# return the index if the target is found. If not, return the index
# where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.


def main():
    nums = [1, 3, 5, 6]
    target = 7
    solution = Solution()
    stuff = solution.searchInsert(nums, target)
    print(stuff)


class Solution:
    def __init__(self):
        self.original_list = None
        self.index = None

    def searchInsert(self, nums: list, target: int) -> int:
        half_len = len(nums) // 2
        head = nums[0:half_len]
        tail = nums[half_len:]
        if not self.original_list:
            self.original_list = nums

        if not self.index:
            if len(nums) > 1:
                if target > head[-1]:
                    self.searchInsert(tail, target)
                else:
                    self.searchInsert(head, target)
            else:
                num = nums[0]
                original_list = self.original_list
                if target > nums[0]:
                    self.index = original_list.index(num) + 1
                else:
                    self.index = original_list.index(num)
        return self.index


if __name__ == "__main__":
    main()
