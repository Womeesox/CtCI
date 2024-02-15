"""
- traverse a tree recursively
- go left, right if left is done
- when you hit the end pass up current tree height + 1 (start with 0)
- mark as done before passing height
- from node that height was passed go right 
- if right is done too compare children's heights
- if whole tree done without returning false return true 
"""

import tree_implementation

