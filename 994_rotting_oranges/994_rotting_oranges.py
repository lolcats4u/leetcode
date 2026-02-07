from typing import List
def main(test):
    solution = Solution().orangesRotting(test)
    print(solution)

def tests():
    test_1 = [[2,1,1],[1,1,0],[0,1,1]]
    test_2 = [[2,1,1],[0,1,1],[1,0,1]]
    test_3 = [[0,2]]
    return locals().values()

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        mins = 0
        row_len = len(grid[0])
        column_len = len(grid)
        for row_index in range(column_len):
            for column_index in range(row_len):
                if mins > (row_len * column_len):
                    return -1
                if grid[row_index][column_index] == 2:
                    try:
                        grid[row_index][column_index + 1] = 2 if grid[row_index][column_index + 1] == 1 else self.orangesRotting(grid)
                        grid[row_index + 1][column_index] = 2 if grid[row_index + 1][column_index] == 1 else self.orangesRotting(grid)
                        grid[row_index][column_index - 1] = 2 if grid[row_index][column_index - 1] == 1 else self.orangesRotting(grid)
                        grid[row_index - 1][column_index] = 2 if grid[row_index - 1][column_index] == 1 else self.orangesRotting(grid)
                        mins += 1
                    except IndexError:
                        continue
                else:
                    mins += 0
        return mins

if __name__ == "__main__":
    tests = tests()
    for test in tests:
        main(test)