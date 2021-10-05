class Node:
    def _init_(self,key):
       self.key=key
       self.left=None
       self.right=None
i=[]
def inorder(root):
    if root is not None:
        inorder(root.left)
        i.append(root.key)
        inorder(root.right)
j=[]
def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        j.append(root.key)
        
k=[]
def preorder(root):
    if root is not None:
        k.append(root.key)
        preorder(root.left)
        preorder(root.right)
p=[]     
def display(root):
    if root is not None:
        p.append(root.key)
        display(root.left)
        display(root.right)
        
        
def insert(node,key):
    if node is None:
        return Node(key)
    if key<node.key:
        node.left=insert(node.left,key)
    else:
        node.right=insert(node.right,key)
    return node
    
def minvalue(node):
    c=node
    while(c.left is not None):
        c=c.left
    return c
    
def deletion(root,key):
    if root is None:
        return root
    if key < root.key:
        root.left=deletion(root.left,key)
    elif(key>root.key):
        root.right=deletion(root.right,key)
    else:
        if root.left is None:
            temp=root.right
            root=None
            return temp
            
        elif root.right is None:
            temp=root.left
            root=None
            return temp
        temp=minValue(root.right)
        root.key=temp.key
        root.right=deletion(root.right,temp.key)
    return root
    
def search(root,k):
    if root is not None:
        if root.key ==k:
            return k
        elif(root.key>k):
            return search(root.left,k)
        else:
            return search(root.right,k)
            
root=None
t=1
while(t):
    t=int(input())
    if t==1:
        root=insert(root,int(input()))
    elif(t==2):
        root=deletion(root,int(input()))
    elif(t==3):
        m=int(input())
        n=search(root,m)
        if n==m:
            print("Search Successful Element",m," is present in the BST")
    elif(t==4):
        print("The Tree Elements are:")
        display(root)
        for h in sorted(p):
            print(h)
        p=[]
    elif(t==6):
        preorder(root)
        print("The Preorder Traversal is:",k)
    elif(t==5):
        inorder(root)
        print("The Inorder Traversal is:",i)
    elif(t==7):
        postorder(root)
    elif(t==8):
        break