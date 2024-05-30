# You are given a large integer represented as an integer array digits, where
# each digits[i] is the ith digit of the integer. The digits are ordered from
# most significant to least significant in left-to-right order. The large integer
# does not contain any leading 0's.


# Increment the large integer by one and return the resulting array of digits.
def main():
    solution = Solution()
    print(solution.plusOne([9]))


class Solution:
    def plusOne(self, digits: list) -> list:
        num = 0
        order_of_magnitude = 1
        digits = list(map(int, digits))
        for digit in reversed(digits):
            num += digit * order_of_magnitude
            order_of_magnitude = order_of_magnitude * 10
        num = num + 1
        return [int(x) for x in str(num)]


if __name__ == "__main__":
    main()
