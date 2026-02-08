from typing import List


def main(test):
    solution = Solution().orangesRotting(test)
    print(solution)


def tests():
    test_0 = [
        [2, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]
    test_1 = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    test_2 = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    test_3 = [[0, 2]]
    test_4 = [[1], [2]]
    return locals().values()


class Solution:
    def __init__(self):
        self.mins = 0
        self.recusion_depth = 0
    def orangesRotting(self, grid: List[List[int]]) -> int:
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
                            # right
                            if grid[i][j + 1] == 1:
                                grid[i][j + 1] = 2
                                successful_rot = True
                        except IndexError:
                            pass
                        try:
                            # left
                            if j - 1 < 0:
                                raise IndexError
                            if grid[i][j - 1] == 1:
                                grid[i][j - 1] = 2
                                successful_rot = True
                        except IndexError:
                            pass
                        try:
                            # up
                            if i - 1 < 0:
                                raise IndexError
                            if grid[i - 1][j] == 1:
                                grid[i - 1][j] = 2
                                successful_rot = True
                        except IndexError:
                            pass
                        try:
                            # down
                            if grid[i + 1][j] == 1:
                                grid[i + 1][j] = 2
                                successful_rot = True
                        except IndexError:
                            pass
                        if successful_rot:
                            self.mins += 1
            self.recusion_depth += 1
            try:
                self.orangesRotting(grid)
            except RecursionError:
                for row in grid:
                    if 1 in row:
                        seen_fresh_orange = True
                        break
                if seen_fresh_orange:
                    self.mins = -1
                    class Impossible(Exception("Impossible Grid")):
                        self.mins = -1

                else:
                    return self.mins
            except Impossible:
                return -1
        else:
            return 0

        if self.mins == 0:
            for row in grid:
                if 1 in row:
                    return -1

        return self.mins


if __name__ == "__main__":
    tests = tests()
    for test in tests:
        main(test)
