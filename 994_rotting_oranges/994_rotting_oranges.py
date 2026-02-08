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
        self.impossible = None
        self.original_grid = None

    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not self.original_grid:
            self.original_grid = grid
            self.grid = [x for x in self.original_grid]
            self.number_of_elements = ((len(self.grid)) * (len(self.grid[0])))

        if self.recusion_depth >= self.number_of_elements:
            if self.mins:
                return self.mins
            else:
                self.impossible = -1
                return self.impossible
        
        if self.fresh_orange():
            if self.rot_and_mutate_grid():
                pass
            else:
                return self.mins
            self.recusion_depth += 1
            self.orangesRotting(self.grid)
        else:
            if self.mins:
                return self.mins
            else:
                return 0

    def fresh_orange(self):
        for row in self.grid:
            if 1 in row:
                return True


    def rot_and_mutate_grid(self):
        successful_rot = False
        for i, row in enumerate(self.grid):
            for j, item in enumerate(row):
                successful_rot = False
                if item == 2:
                    try:
                        # right
                        if self.grid[i][j + 1] == 1:
                            self.grid[i][j + 1] = 2
                            successful_rot = True
                    except IndexError:
                        pass
                    try:
                        # left
                        if j - 1 < 0:
                            raise IndexError
                        if self.grid[i][j - 1] == 1:
                            self.grid[i][j - 1] = 2
                            successful_rot = True
                    except IndexError:
                        pass
                    try:
                        # up
                        if i - 1 < 0:
                            raise IndexError
                        if self.grid[i - 1][j] == 1:
                            self.grid[i - 1][j] = 2
                            successful_rot = True
                    except IndexError:
                        pass
                    try:
                        # down
                        if self.grid[i + 1][j] == 1:
                            self.grid[i + 1][j] = 2
                            successful_rot = True
                    except IndexError:
                        pass

                if successful_rot:
                    self.mins += 1
                    
        return successful_rot

if __name__ == "__main__":
    tests = tests()
    for test in tests:
        main(test)
