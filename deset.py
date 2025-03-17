import unittest

class BinaryTree:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class ZigZag:
    def __init__(self,root):
        self.tree = root

    def show(self):
        odg=[]
        pogoj=True
        level=0
        while pogoj:
            nivoe=nivo(self.tree,level)
            if nivoe==[]:
                pogoj=False
            if level%2==1:
                nivoe=nivoe[::-1]
            odg=odg+nivoe
            level+=1
        string=''
        for el in odg:#lahko bi izboljsal, da nebi potreboval te zanke 
            string= string+ f', {el}'
        return string[2:]

#pomozna funkcija, ki nam izpise elemente na posameznem nivolju
def nivo(tree,level):
    if tree is None:
        return []
    if level==0:
        if tree.value is None:
            return []
        else:
            return [tree.value]
    else:
        return nivo(tree.left,level-1) + nivo(tree.right,level-1)

#testiranje      

class TestZigZag(unittest.TestCase):
    def test_empty_tree(self):
        tree = None
        zigzag = ZigZag(tree)
        self.assertEqual(zigzag.show(), "")

    def test_single_BinaryTree(self):
        tree = BinaryTree(1)
        zigzag = ZigZag(tree)
        self.assertEqual(zigzag.show(), "1")

    def test_full_tree(self):
        tree = BinaryTree(1)
        tree.left = BinaryTree(2)
        tree.right = BinaryTree(3)
        tree.left.left = BinaryTree(4)
        tree.left.right = BinaryTree(5)
        tree.right.left = BinaryTree(6)
        tree.right.right = BinaryTree(7)
        zigzag = ZigZag(tree)
        self.assertEqual(zigzag.show(), "1, 3, 2, 4, 5, 6, 7")

    def test_unbalanced_tree(self):
        tree = BinaryTree(1)
        tree.left = BinaryTree(2)
        tree.left.left = BinaryTree(4)
        tree.left.left.left = BinaryTree(8)
        tree.right = BinaryTree(3)
        tree.right.right = BinaryTree(7)
        zigzag = ZigZag(tree)
        self.assertEqual(zigzag.show(), "1, 3, 2, 4, 7, 8")

    def test_zigzag_tree(self):
        tree = BinaryTree(1)
        tree.left = BinaryTree(2)
        tree.right = BinaryTree(3)
        tree.left.left = BinaryTree(4)
        tree.right.right = BinaryTree(5)
        zigzag = ZigZag(tree)
        self.assertEqual(zigzag.show(), "1, 3, 2, 4, 5")

#klic testov
if __name__ == "__main__":
    unittest.main()

    