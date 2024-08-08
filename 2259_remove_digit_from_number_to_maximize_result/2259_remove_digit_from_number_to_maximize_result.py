def main():
    test0 = ["123", "3"]
    test1 = ["1231", "1"]
    test2 = ["551", "5"]
    tests = [test0, test1, test2]

    for test in tests:
        Solution().removeDigit(test[0], test[1])


class Solution:
    def __init__(self):
        self.winner = None

    def removeDigit(self, number: str, digit: str) -> str:
        number_options = []
        for i, char in enumerate(number):
            if char == digit:
                number_options.append(int(number[0:i] + number[i + 1 :]))
        self.winner = self.largest_number(number_options)

        return self.winner

    def largest_number(self, list_of_nums: list) -> int:
        winner = 0
        for number in list_of_nums:
            if number > winner:
                winner = number

        return str(winner)


if __name__ == "__main__":
    main()
