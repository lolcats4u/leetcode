def main():
    solution = Solution()
    a = "0011"
    b = "0011"
    print(solution.addBinary(a, b))


class Solution:
    def __init__(self):
        self.a = None
        self.b = None
        self.zip_a_b = None
        self.a_len = None
        self.b_len = None
        self.sum = None

    def addBinary(self, a: str, b: str) -> str:
        self.a = a
        self.b = b
        self.zip_binary()
        carry = 0

        try:
            

    def zip_binary(self):
        self.a_len = len(self.a)
        self.b_len = len(self.b)
        if self.a_len == self.b_len:
            self.zip_a_b = zip(self.a, self.b)
        elif self.a_len > self.b_len:
            new_b = ""
            for _ in range(self.a_len - self.b_len):
                new_b += "0"
            new_b += self.b
            self.b = new_b
            self.zip_a_b = zip(self.a, self.b)
        else:
            new_a = ""
            for _ in range(self.b_len - self.a_len):
                new_a += "0"
            new_a += self.b
            self.zip_a_b = zip(self.a, self.b)


if __name__ == "__main__":
    main()
