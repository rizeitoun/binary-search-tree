# Creates and sorts a binary tree

class TreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        fmt = 'TreeNode(data={}, left={}, right={})'
        return fmt.format(self.data, self.left, self.right)

    # Adds new entry to node depending on its value.
    def __add__(self, new_data):
        if new_data <= self.data:
            if self.left is None:
                self.left = TreeNode(new_data)
            else:
                self.left += new_data
        else:
            if self.right is None:
                self.right = TreeNode(new_data)
            else:
                self.right += new_data
        return self

    # Sorts node locally.
    def get_sort(self):
        sorted_data = []
        if self.left is None:
            sorted_data.append(self.data)
        else:
            sorted_data = self.left.get_sort()
            sorted_data.append(self.data)

        if self.right is not None:
            sorted_data.extend(self.right.get_sort())

        return sorted_data

class BinarySearchTree(object):
    def __init__(self, raw_tree_data):
        self.tree = TreeNode(raw_tree_data[0])
        for i, value in enumerate(raw_tree_data):
            if i > 0:
                self.tree += value

    def data(self):
        return self.tree

    def sorted_data(self):
        return self.tree.get_sort()

if __name__ == "__main__":
    print(BinarySearchTree(['4', '2', '6', '1', '3', '5', '7',]).data())
    print(BinarySearchTree(['4', '2', '6', '1', '3', '5', '7']).sorted_data())