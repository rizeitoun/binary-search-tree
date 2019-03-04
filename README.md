# Binary Search Tree in Python
#### This is a binary search tree exercise from the Python track of exercism.io.  Goal was to make a python script to efficiently store and retrieve sorted data using a binary tree format to avoid array limitations.  

#### Implementation code is in binary_search_tree.py
#### Example tests from exercism where showing input and output as first and second parameters into assertEqual.
```
    def test_can_sort_complex_tree(self):
        self.assertEqual(
            BinarySearchTree(['2', '1', '3', '6', '7', '5']).sorted_data(),
            ['1', '2', '3', '5', '6', '7']
        )
```