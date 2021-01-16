# Python Tree Transversal by
# Ikram Maulana
# 1930511075
# Teknik Informatika 3B

# Kelas yang merepresentasikan Node
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # Transversal Preorder (Root, Kiri, Kanan)
    def PreOrder(self):
        print(self.data, end=' ')
        if self.left:
            self.left.PreOrder()
        if self.right:
            self.right.PreOrder()

    # Transversal Inorder (Kiri, Root, Kanan)
    def InOrder(self):
        if self.left:
            self.left.InOrder()
        print(self.data, end=' ')
        if self.right:
            self.right.InOrder()

    # Transversal Postorder (Kiri, Kanan, Root)
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
root.right.left = Node(int(input("Masukan Nilai Child Kiri of Kanan: ")))
root.right.right = Node(int(input("Masukan Nilai Child Kanan of Kanan: ")))

# Print
print("===============================================")
print("Tree Transversal by Ikram Maulana || 1930511075")
print("===============================================")
print("Preorder Traversal: ", end="")
root.PreOrder()
print("\nPostorder Traversal: ", end="")
root.PostOrder()
print("\nInorder Traversal: ", end="")
root.InOrder()
print("\n=============================================")
