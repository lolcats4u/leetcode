from typing import List
test = [1,5,0,3,5]
test2 = [0]
def main(test):
    sol = Solution()
    nums = sol.minimumOperations(test)
    print(str(nums))
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        set_nums = list(set(nums))
        set_nums_len = len(set_nums)
        if set_nums_len == 1:
            if set_nums[0] == 0:
                return 0
            return 1
        else:
            sorted_setted_nums = [x for x in list(sorted(set_nums)) if x !=0]
            num_count = 0
            while sorted_setted_nums:
                num = sorted_setted_nums[0]
                new_nums = [x - num for x in sorted_setted_nums]
                num_count = num_count + 1
                if len(new_nums) == 1 and new_nums[0] == 0:
                    return num_count
                sorted_setted_nums = new_nums[1:]

if __name__ == "__main__":
    main(test2)