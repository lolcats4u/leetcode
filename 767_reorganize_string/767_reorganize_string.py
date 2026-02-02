def main(test):
    print(Solution().reorganizeString(test))

class Solution:
    def __init__(self, s):
        self.reorganizeString
        
    def reorganizeString(self, s: str) -> str:
        hash_table = self.hash_str(s)
        str_pattern = []
        for key, value in hash_table:
            if not str_pattern:
                str_pattern.append(key)
            if len(str_pattern) == 1:
                str_pattern.append(key)
                

        pass

    def hash_str(self, s:str) -> dict:
        str_table = {}
        for char in s:
            if char not in str_table:
                str_table[char] = 1
            else:
                str_table[char] += 1
        return dict(sorted(str_table.items()))


def tests():
    test_1 = "aab"
    test_2 = "aaab"
    return locals().values()

if __name__ == "__main__":
    tests = tests()
    for test in tests:
        main(test)