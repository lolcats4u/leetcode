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

        seen_fresh_orange = False
        for row in grid:
            if 1 in row:
                seen_fresh_orange = True
                break

        if seen_fresh_orange:
            for i, row in enumerate(grid):
                for j, item in enumerate(row):
                    successful_rot = False
                    if item == 2:
                        try:
                            if grid[i][j + 1] == 1:
                                grid[i][j + 1] = 2
                                successful_rot = True
                        except IndexError:
                            pass
                        try:
                            if j - 1 < 0:
                                raise IndexError
                            if grid[i][j - 1] == 1:
                                grid[i][j - 1] = 2
                                successful_rot = True
                        except IndexError:
                            pass
                        try:
                            if grid[i + 1][j + 1]:
                                grid[i + 1][j + 1] = 2
                                successful_rot = True
                        except IndexError:
                            pass
                        try:
                            if (i - 1) < 0 or (j - 1) < 0:
                                raise IndexError
                            if grid[i - 1][j - 1] == 1:
                                grid[i - 1][j - 1] = 2
                                successful_rot = True
                        except IndexError:
                            pass
                        if successful_rot:
                            mins += 1
        else:
            return 0

        for row in grid:
            if 1 in row:
                return -1
        
        return mins

if __name__ == "__main__":
    tests = tests()
    for test in tests:
        main(test)