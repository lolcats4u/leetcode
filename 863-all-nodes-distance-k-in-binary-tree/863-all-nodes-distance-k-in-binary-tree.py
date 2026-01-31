def main(root, target, k):
    node_num = 1
    layer_width= 1
    current_layer = []
    binary_tree = transform(root)

    solution = Solution().distanceK(binary_tree, target, k)

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

node_num = 1
layer_width= 1
current_layer = []


def transform(binary_tree_list:list=None, head:TreeNode=None, node_num:int=1, layer_width=1, current_window = [], current_layer=[], tree_head=None):
    if not head:
        head = TreeNode(binary_tree_list[0])
        tree_head = head
        head.left = TreeNode(binary_tree_list[1])
        head.right = TreeNode(binary_tree_list[2])
        node_num = node_num + 2
        layer_width = 4
        current_layer = binary_tree_list[3:7]
        current_window = current_layer
    current_window_length = len(current_window)
    if current_window_length > 2:
        half = current_window_length // 2
        transform(binary_tree_list, head.left, node_num, layer_width, current_layer=current_layer ,current_window=current_window[:half])
        transform(binary_tree_list, head.right, node_num, layer_width, current_layer=current_layer, current_window=current_window[half:])
    elif current_window_length == 2:
        node_num += 2
        head.left = TreeNode(current_window[0])
        head.right = TreeNode(current_window[1])

        if node_num == len(binary_tree_list):
            return tree_head
        if len(remainder) < layer_width:
            while len(remainder)< layer_width:
                binary_tree_list += None
            current_layer = binary_tree_list[node_num + 1:]
            half = len(current_layer)/2
            transform(binary_tree_list,head.left, node_num, layer_width, current_window=current_layer[:half+1])
            transform(binary_tree_list,head.right, node_num, layer_width,tcurrent_window=current_layer[half:])

            
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