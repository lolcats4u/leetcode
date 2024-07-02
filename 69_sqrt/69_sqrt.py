def main():
    print("Meow")
    solution = Solution()
    print(solution)


class Solution:
    def __init__(self):
        self.sqrt = 0
        self.floor_perfect = 0
        self.ceiling_perfect = 0

    def mySqrt(self, x: int) -> int:
        self.find_nearest_perfect_squares(self.test_case, x)
        self.find_sqrt(self, self.floor_perfect, self.ceiling_perfect)

        return int("%.0f" % (self.sqrt))

    def find_nearest_perfect_squares(self, x: int):
        floor_int = 0
        while (floor_int * floor_int) < (x * x):
            floor_int += 1
        self.floor_perfect = floor_int
        self.ceiling_perfect = floor_int + 1

    def find_sqrt(self, x: int, floor, ceiling):
        average = (floor + ceiling) / 2
        average_squared = average * average

        if average_squared < x:
            self.find_sqrt(self, average, ceiling)
        elif average_squared > x:
            self.find_sqrt(self, floor, average)
        else:
            self.sqrt = average


if __name__ == "__main__":
    main()
