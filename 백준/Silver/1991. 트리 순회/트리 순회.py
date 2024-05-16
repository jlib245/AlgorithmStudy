import sys
input = sys.stdin.readline

def preorder(node : str):
    preRes.append(node)
    for i in route[ord(node)-65]:
        if i != '.':
            preorder(i)
    return

def inorder(node : str):
    left, right = route[ord(node)-65]
    for i in (left, right):
        if not printed[ord(node)-65] and (left == '.' or printed[ord(left)-65] ):
            printed[ord(node)-65] = True
            inRes.append(node)
        if i != '.':
            inorder(i)
    return

def postorder(node : str):
    left, right = route[ord(node)-65]
    for i in (left, right):
        if i != '.':
            postorder(i)
        if not printed[ord(node)-65] and (left == '.' or printed[ord(left)-65]) and (right == '.' or printed[ord(right)-65]):
            printed[ord(node)-65] = True
            postRes.append(node)    
    return

N = int(input())

route = [0]*26
for i in range(N):
    node, left, right = input().rstrip().split()
    route[ord(node)-65] = (left, right)


preRes = []
inRes = []
postRes = []

preorder("A")

printed = [False]*26
inorder("A")

printed = [False]*26
postorder("A")

print(*preRes, sep='')
print(*inRes, sep='')
print(*postRes, sep='')