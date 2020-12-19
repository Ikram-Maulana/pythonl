# Binary Tree python by
# Ikram Maulana
# 1930511075

# Kelas yang merepresentasikan Node
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # Traverse Preorder (Root, Left, Right)
    def PreOrder(self):
        print(self.data, end=' ')
        if self.left:
            self.left.PreOrder()
        if self.right:
            self.right.PreOrder()

    # Traverse Inorder (Left, Root, Right)
    def InOrder(self):
        if self.left:
            self.left.InOrder()
        print(self.data, end=' ')
        if self.right:
            self.right.InOrder()

    # Traverse Postorder (Left, Right, Root)
    def PostOrder(self):
        if self.left:
            self.left.PostOrder()
        if self.right:
            self.right.PostOrder()
        print(self.data, end=' ')


# Masukan Nilai root
root = Node(int(input("Masukan Nilai Root: ")))
root.left = Node(int(input("Masukan Nilai Child kiri of Root: ")))
root.right = Node(int(input("Masukan Nilai Child kanan of Root: ")))
root.left.left = Node(int(input("Masukan Nilai Child kiri of Kiri: ")))
root.left.right = Node(int(input("Masukan Nilai Child kanan of Kiri: ")))

# Print
print("==========================================")
print("Tree Python by Ikram Maulana || 1930511075")
print("==========================================")
print("Preorder Traversal: ", end="")
root.PreOrder()
print("\nInorder Traversal: ", end="")
root.InOrder()
print("\nPostorder Traversal: ", end="")
root.PostOrder()
print("\n==========================================")
