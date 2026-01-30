def main(root, target, k):
    solution = Solution().distanceK(root[0], target, k)

def tests():
    test_1 = {"root": [3,5,1,6,2,0,8,None,None,7,4],
              "target" : 1,
              "k" : 3
            }
    test_2 = {"root": [1],
              "target" : 1,
              "k" : 3
            }
    
    return locals()

class TreeTransform():
    def __init__(self, binary_tree_list):
        self.binary_tree_list = binary_tree_list
        self.head = None
        self.list_index = 0
    
    def transform(self, prev=None):
            if not self.head:
                self.head = TreeNode(self.binary_tree_list[self.list_index])
                self.head.left = None
            try:
                self.head.right = self.binary_tree_list[self.list_index+1]
            except KeyError:
                self.head.right = None
                return self.head
            
            TreeNode()



            self.transform(self, prev)
            
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.count = 0
        self.nodes_k_away = []
        self.target_found = False

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root.next and self.count < k:
            return []
        if root is not target and not self.target_found:
            self.distanceK(root.next, target, k)
        elif root is target:
            self.target_found = True
            self.count += 1
            self.distanceK(root.next, target, k)
        elif self.target_found and self.count < k:
            self.count += 1
            self.distanceK(root.next, target, k)
        else:
            self.target_found.append(root)
            return self.nodes_k_away

if __name__ == "__main__":
    tests = tests()
    for test in tests:
        test_instance = tests[test]
        main(test_instance["root"], test_instance["target"], test_instance["k"])