from queue1 import Queue
from stack1 import Stack

class TreeNode:
    def __init__(self, data=None):
        self.__data=data
        self.__left=None
        self.__right=None

    def __del__(self):
        print('data {} is deleted'.format(self.__data))

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data=data

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        self.__left=left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        self.__right=right

def preorder(cur):
    if not cur:
        return

    print(cur.data, end='  ')
    preorder(cur.left)
    preorder(cur.right)

def inorder(cur):
    if not cur:
        return

    inorder(cur.left)
    print(cur.data, end='  ')
    inorder(cur.right)

def postorder(cur):
    if not cur:
        return

    postorder(cur.left)
    postorder(cur.right)
    print(cur.data, end='  ')

def iter_preorder(cur):
    s=Stack()
    while True:
        while cur:
            print(cur.data, end='  ')
            s.push(cur)
            cur=cur.left
        cur=s.pop()
        if not cur:
            break
        cur=cur.right    

def iter_inorder(cur):
    s=Stack()
    while True:
        while cur:
            s.push(cur)
            cur=cur.left
        cur=s.pop()
        if not cur:
            break
        print(cur.data, end='  ')
        cur=cur.right

def iter_postorder(cur):
    s1=Stack()
    s2=Stack()

    s1.push(cur)
    while not s1.empty():
        cur=s1.pop()
        s2.push(cur)

        if cur.left:
            s1.push(cur.left)
    
        if cur.right:
            s1.push(cur.right)
    
    while not s2.empty():
        cur=s2.pop()
        print(cur.data, end='  ')
            
def levelorder(cur):
    q=Queue()

    q.enqueue(cur)
    while not q.empty():
        cur=q.dequeue()
        print(cur.data, end='  ')
        if cur.left:
            q.enqueue(cur.left)
        if cur.right:
            q.enqueue(cur.right)

if __name__=="__main__":
    n1=TreeNode(1)
    n2=TreeNode(2)
    n3=TreeNode(3)
    n4=TreeNode(4)
    n5=TreeNode(5)
    n6=TreeNode(6)
    n7=TreeNode(7)

    n1.left=n2; n1.right=n3
    n2.left=n4; n2.right=n5
    n3.left=n6; n3.right=n7

    #preorder(n1)
    iter_preorder(n1)
    print()

    #inorder(n1)
    iter_inorder(n1)
    print()

    #postorder(n1)
    iter_postorder(n1)
    print()

    levelorder(n1)
    print()



