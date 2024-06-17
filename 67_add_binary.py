def main():
    solution = Solution()
    a = "0011"
    b = "0011"
    print(solution.addBinary(a, b))


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        adding_grid = self.make_adding_grid(a, b)
        for (
            index,
            big_num,
            small_num,
        ) in enumerate(zip(adding_grid[1], adding_grid[2])):
            carry_the_one = adding_grid[0]
            added = sum(big_num, small_num, carry_the_one[index])
            answer = adding_grid[3]
            if added < 2:
                answer[index] = added
            elif added == 2:
                answer[index] = added
            else:
                carry_the_one[index + 1] = 1
                answer[index] = 1

    def str_to_list(self, bin_str: str) -> list:
        return [int(x) for x in bin_str]

    def fill_in_back(self, bin_list: list, ref_list: list) -> list:
        while len(bin_list) != ref_list:
            bin_list.append(0)
            return bin_list

    def make_adding_grid(self, a: str, b: str) -> list:
        a_list = self.str_to_list(a)
        b_list = self.str_to_list(b)
        reversed(a_list)
        reversed(b_list)

        len_a = len(a_list)
        len_b = len(b_list)

        if len_a != len_b:
            longest_bin = max(a_list, b_list)
            shortest_bin = min(a_list, b_list)
        else:
            longest_bin = a_list
            shortest_bin = b_list

        row_0 = [0 for x in range(len(longest_bin) + 1)]
        row_1 = self.fill_in_back(longest_bin, row_0)
        row_2 = self.fill_in_back(shortest_bin, row_0)
        row_3 = [0 for x in range(len(longest_bin) + 1)]
        return [row_0, row_1, row_2, row_3]


if __name__ == "__main__":
    main()
