def main():
    test1 = ["11", "1"]
    test2 = ["1010", "1011"]
    tests = [test1, test2]
    for test in tests:
        Solution().addBinary(test[0], test[1])


class Solution:
    def __init__(self):
        self.sum = None
        self.a_len = None
        self.b_len = None
        self.diff = None
        self.bigger = None
        self.smaller = None
        self.sum = ""
        self.carry = 0

    def addBinary(self, a: str, b: str) -> str:
        self.determine_biggest(a, b)
        return self.sum

    def find_bin_sum(self, biggest_str: str, smallest_str: str):
        # diff should be positive
        if self.diff != 0:
            start = -(self.bigger - 1)
            stop = -(self.smaller - 1)

        else:
            start = -(self.bigger - 1)
            stop = 0

        # iterate from the back until you've gone over the whole length of the smallest str
        for i in range(start, stop):
            self.cast_bin_int_bin(int(biggest_str[i]), int(smallest_str[i]))

        # handle last carry digit
        if self.diff == 0:
            self.cast_bin_int_bin(0, 0)
            return self.sum
        else:
            self.cast_bin_int_bin(0, biggest_str[stop - 1])
            self.sum = biggest_str[0 : self.diff] + self.sum
            return self.sum

    def cast_bin_int_bin(self, num1: int, num2: int):
        int_sum = num1 + num2 + self.carry
        if int_sum == 0:
            self.sum = "0" + self.sum
            self.carry = 0
        elif int_sum == 1:
            self.sum = "1" + self.sum
            self.carry = 0
        elif int_sum == 2:
            self.sum = "0" + self.sum
            self.carry = 1
        else:
            self.sum = "1" + self.sum
            self.carry = 1

    def determine_biggest(self, a: str, b: str):
        self.a_len = len(a)
        self.b_len = len(b)

        self.diff = self.a_len - self.b_len
        if self.diff < 0:
            self.bigger = self.b_len
            self.smaller = self.a_len
            self.diff = self.diff * -1
            self.find_bin_sum(b, a)
        else:
            self.bigger = self.a_len
            self.smaller = self.b_len
            self.find_bin_sum(a, b)


if __name__ == "__main__":
    main()
