def main():
    print("meow")
    nums = [3, 2, 2, 3]
    val = 3
    solution = Solution()
    my_answer = solution.removeElement(nums, val)
    print(my_answer)


class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)


if __name__ == "__main__":
    main()
