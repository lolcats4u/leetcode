def main(test):
    instruction_zip = zip(test[0], test[1])
    result = []
    for instruction in instruction_zip:
        if instruction[0] == "get":
            result.append(solution.get(instruction[1][0]))
        elif instruction[0] == "put":
            result.append(solution.put(instruction[1][0], instruction[1][1]))
        else:
            solution = LRUCache(instruction[1][0])
            result.append(None)
    print(result)


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = []

    def get(self, key: int) -> int:
        last_entry = None
        for entry in self.cache:
            if key in entry:
                last_entry = entry
        if not last_entry:
            return -1
        self.cache = [x for x in self.cache if x != last_entry]
        self.put(last_entry[0], last_entry[1])
        return last_entry[1]

    def put(self, key: int, value: int) -> None:
        new_entry = [[key,value]]
        if len(self.cache) == 0:
            self.cache = new_entry
            return
        elif len(self.cache) >= self.capacity:
            del self.cache[-1]

        self.cache = self.cache + new_entry

def tests():
    test_1 = (
        ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
        [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]],
    )
    test_24 = (
        ["LRUCache","put","put","get","put","put","get"],
        [[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]
    )
    return locals().values()


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == "__main__":
    tests = tests()
    for test in tests:
        main(test)
