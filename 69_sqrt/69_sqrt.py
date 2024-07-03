def main():
    print("cat")
    solution = Solution()
    print(solution.mySqrt(8))


class Solution:
    def __init__(self):
        self.sqrt = 0
        self.floor_perfect = 0
        self.ceiling_perfect = 0

    def mySqrt(self, x: int) -> int:
        self.find_nearest_perfect_squares(x=x)
        self.find_sqrt(x=x, floor=self.floor_perfect, ceiling=self.ceiling_perfect)

        return int("%.0f" % (self.sqrt))

    def find_nearest_perfect_squares(self, x: int):
        ceiling_square = 0
        while (ceiling_square * ceiling_square) < x:
            ceiling_square += 1
        self.floor_perfect = ceiling_square - 1
        self.ceiling_perfect = ceiling_square

    def find_sqrt(self, x: int, floor, ceiling):
        average = (floor + ceiling) / 2
        average_squared = average * average

        if average_squared < x:
            self.find_sqrt(x=x, floor=average, ceiling=ceiling)
        elif average_squared > x:
            self.find_sqrt(x=x, floor=floor, ceiling=average)
        else:
            self.sqrt = average


if __name__ == "__main__":
    main()
