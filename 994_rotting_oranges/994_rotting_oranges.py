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
        mins = None
        row_len = len(grid[0])
        column_len = len(grid)

        seen_fresh_orange = False
        for row in grid:
            if 1 in row:
                seen_fresh_orange = True

        if seen_fresh_orange:
            for row_index in range(column_len):
                for column_index in range(row_len):
                    successful_rot = False
                    if grid[row_index][column_index] == 2:
                        try:
                            if grid[row_index][column_index + 1] == 1:
                                grid[row_index][column_index + 1] = 2
                                successful_rot = True
                        except IndexError:
                            continue
                        try:
                            if grid[row_index + 1][column_index] == 1:
                                grid[row_index + 1][column_index] = 2
                                successful_rot = True
                        except IndexError:
                            continue
                        try:
                            if grid[row_index][column_index - 1] == 1:
                                grid[row_index][column_index - 1] = 2 
                                successful_rot = True
                        except IndexError:
                            continue
                        try:
                            if grid[row_index - 1][column_index] == 1:
                                grid[row_index - 1][column_index] = 2 
                                successful_rot = True
                        except IndexError:
                            continue
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