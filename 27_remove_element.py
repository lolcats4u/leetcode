def main():
    print("meow")
    nums = [3, 2, 2, 3]
    val = 3
    solution = Solution()
    my_awnswer = solution.removeElement(nums, val)
    print(my_awnswer)


class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)


if __name__ == "__main__":
    main()
