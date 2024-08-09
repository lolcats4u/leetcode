def main():
    test1 = ["101111", "10"]
    test2 = ["1010", "1011"]
    test3 = ["10101011", "1010"]
    test4 = ["1", "11"]
    test5 = ["1", "111"]
    test6 = ["100", "110010"]
    tests = [test1, test2, test3, test4, test5, test6]
    for test in tests:
        Solution().addBinary(test[0], test[1])


class Solution:
    def __init__(self):
        self.sum = None
        self.a_len = None
        self.b_len = None
        self.diff = None
        self.bigger_len = None
        self.smaller_len = None
        self.sum = ""
        self.carry = 0

    def addBinary(self, a: str, b: str) -> str:
        biggest_str, smallest_str = self.determine_biggest(a, b)
        self.find_bin_sum(biggest_str, smallest_str)

        if self.sum[0] == "0":
            return self.sum[1:]
        else:
            return self.sum

    def find_bin_sum(self, biggest_str: str, smallest_str: str):
        ##### opportunities for early exit
        if self.a_len == 1 and self.b_len == 1:
            self.cast_bin_int_bin(int(biggest_str[0]), int(smallest_str[0]))
            # capture remaining carry
            self.cast_bin_int_bin(0, 0)
            return

        if self.a_len == 2 or self.b_len == 2:
            if self.diff == 0:
                for i in range(-1, -2):
                    self.cast_bin_int_bin(int(biggest_str[i]), int(smallest_str[i]))
                self.cast_bin_int_bin(0, 0)
                return
            else:
                for i in range(-1, -3, -1):
                    self.cast_bin_int_bin(int(biggest_str[i]), int(smallest_str[i]))
                start_index = -3
                if self.carry == 1:
                    while self.carry == 1:
                        try:
                            self.cast_bin_int_bin(int(biggest_str[start_index]), 0)
                            start_index -= 1
                        except IndexError:
                            self.cast_bin_int_bin(0, 0)
                            return
                    front_slice = self.bigger_len + start_index
                    if front_slice == 0:
                        self.sum = biggest_str[0] + self.sum
                        return
                    else:
                        self.sum = biggest_str[:front_slice] + self.sum
                        return

                self.cast_bin_int_bin(int(biggest_str[-2]), 0)
                self.cast_bin_int_bin(0, 0)
                return
        #####

        else:
            # diff should be positive
            if self.diff != 0:
                start = -1
                stop = -(self.smaller_len + 1)

            else:
                start = -1
                stop = -(self.bigger_len + 1)

            # iterate from the back until you've gone over the whole length of the smallest str
            for i in range(start, stop, -1):
                self.cast_bin_int_bin(int(biggest_str[i]), int(smallest_str[i]))

            # handle last carry digit
            if self.diff == 0:
                self.cast_bin_int_bin(0, 0)
                return

            # append remaining digits
            else:
                if self.carry == 1:
                    start_index = -(self.smaller_len + 1)
                    while self.carry == 1:
                        try:
                            self.cast_bin_int_bin(int(biggest_str[start_index]), 0)
                            start_index -= 1
                        except IndexError:
                            self.cast_bin_int_bin(0, 0)
                            return
                    self.sum = biggest_str[: self.diff + start_index] + self.sum
                    return
                else:
                    slice = biggest_str[: self.diff] + self.sum
                    self.sum = biggest_str[0 : self.diff] + self.sum

                return

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
            self.bigger_len = self.b_len
            self.smaller_len = self.a_len
            self.diff = self.diff * -1
            return b, a
        else:
            self.bigger_len = self.a_len
            self.smaller_len = self.b_len
            return a, b


if __name__ == "__main__":
    main()
