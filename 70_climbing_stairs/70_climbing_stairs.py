def main():
    solution = Solution()

class Solution:
    def __init__(self):
        self.n = None
        self.available_step_lists = []
        self.number_of_twos = None
        self.current_one_list = []
        self.shrunk_list = None
        self.number_of_gaps = 0
        self.gap_lengths = []
        self.max_ones = 0
        self.iterators = []


    def climbStairs(self, n: int) -> int:
        self.n = n
        ones_list = [1 for x in range(self.n)]
        self.available_step_lists.append(ones_list)
        if n > 1:
            self.number_of_twos = 1
    
    def create_unique_step_list(self):
        whole_iterator = []
        self.gap 
        for gap in self.gap_lengths:
            iterator_peice = [2] + [1 for x in range(gap)]
            whole_iterator.append(iterator_peice)
        length_diff = self.n - len(whole_iterator)
        remainder_list = [1 for x in range(length_diff)]
        for i in range(length_diff):
            self.available_step_lists.append(remainder_list.insert(whole_iterator,i))


    def increment_twos(self):
        if self.max_ones != 0:
            self.max_ones -= (self.number_of_twos*2)
            self.create_unique_step_list()
            self.number_of_twos += 1
            self.increment_twos()



    


        


        
