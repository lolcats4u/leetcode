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
        for row_index in column_len:
            for column_index in row_len:
                if mins > row_index * column_index:
                    return -1
                if 1 in grid:
                    if grid[row_index][column_index] == 2:
                        if row_index == 1:
                            if column_index == 1:
                                grid[row_index][column_index + 1] = 2
                                grid[row_index + 1][column_index] = 2
                                mins += self.orangesRotting(grid[row_index][column_index + 1])
                                mins += self.orangesRotting(grid[row_index + 1][column_index])
                                return 1
                            if column_index == row_len:
                                grid[row_index][column_index - 1] = 2
                                grid[row_index - 1][column_index] = 2
                                mins += self.orangesRotting(grid[row_index][column_index - 1])
                                mins += self.orangesRotting(grid[row_index - 1][column_index])
                                return 1
                        elif row_index == column_len:
                            if  column_index == 1:
                                grid[row_index][column_index + 1] = 2
                                grid[row_index - 1][column_index] = 2
                                mins += self.orangesRotting(grid[row_index][column_index + 1])
                                mins += self.orangesRotting(grid[row_index - 1][column_index])
                                return 1
                            if column_index == row_len:
                                grid[row_index][column_index - 1] = 2
                                grid[row_index - 1][column_index] = 2
                                mins += self.orangesRotting(grid[row_index][column_index - 1])
                                mins += self.orangesRotting(grid[row_index - 1][column_index])
                                return 1
                        else:
                            grid[row_index][column_index + 1] = 2
                            grid[row_index][column_index - 1] = 2
                            grid[row_index + 1][column_index] = 2
                            grid[row_index - 1][column_index] = 2
                            mins += self.orangesRotting(grid[row_index][column_index + 1])
                            mins += self.orangesRotting(grid[row_index][column_index - 1])
                            mins += self.orangesRotting(grid[row_index + 1][column_index])
                            mins += self.orangesRotting(grid[row_index - 1][column_index])
                            return 1
                else:
                    return mins

if __name__ == "__main__":
    tests = tests()
    for test in tests:
        main(test)