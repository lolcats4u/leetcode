import timeit


def main():
    test1 = ["101111", "10"]
    test2 = ["1010", "1011"]
    test3 = ["10101011", "1010"]
    test4 = ["1", "11"]
    test5 = ["1", "111"]
    test6 = ["100", "110010"]
    tests = [test1, test2, test3, test4, test5, test6]

    for test in tests:
        print(timeit.timeit(Solution().addBinary(test[0], test[1]), number=1000))

    print("------------------------------------------------------------------------")

    for test in tests:
        print(timeit.timeit(SolutionList().addBinary(test[0], test[1]), number=1000))


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
        return self.sum

    def find_bin_sum(self, biggest_str, smallest_str):
        for i in range(-1, -(self.bigger_len + 1), -1):
            try:
                self.cast_bin_int_bin(int(biggest_str[i]), int(smallest_str[i]))
            except IndexError:
                start_index = self.smaller_len + 1
                while start_index <= self.bigger_len:
                    self.cast_bin_int_bin(0, int(biggest_str[-start_index]))
                    start_index += 1
                while self.carry == 1:
                    self.cast_bin_int_bin(0, 0)
                return
        while self.carry == 1:
            self.cast_bin_int_bin(0, 0)
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


class SolutionList:
    def __init__(self):
        self.sum = None
        self.a_len = None
        self.b_len = None
        self.diff = None
        self.bigger_len = None
        self.smaller_len = None
        self.sum = []
        self.carry = 0

    def addBinary(self, a: str, b: str) -> str:
        biggest_str, smallest_str = self.determine_biggest(a, b)
        self.find_bin_sum(biggest_str, smallest_str)
        (self.sum).reverse()
        return "".join(self.sum)

    def find_bin_sum(self, biggest_str, smallest_str):
        for i in range(-1, -(self.bigger_len + 1), -1):
            try:
                self.cast_bin_int_bin(int(biggest_str[i]), int(smallest_str[i]))
            except IndexError:
                start_index = self.smaller_len + 1
                while start_index <= self.bigger_len:
                    self.cast_bin_int_bin(0, int(biggest_str[-start_index]))
                    start_index += 1
                while self.carry == 1:
                    self.cast_bin_int_bin(0, 0)
                return
        while self.carry == 1:
            self.cast_bin_int_bin(0, 0)
        return

    def cast_bin_int_bin(self, num1: int, num2: int):
        int_sum = num1 + num2 + self.carry
        if int_sum == 0:
            self.sum.append("0")
            self.carry = 0
        elif int_sum == 1:
            self.sum.append("1")
            self.carry = 0
        elif int_sum == 2:
            self.sum.append("0")
            self.carry = 1
        else:
            self.sum.append("1")
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
