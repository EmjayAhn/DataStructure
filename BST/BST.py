from binary_tree import TreeNode

class BST:


    def __init__(self):
        self.root=None


    def get_root(self):
        return self.root

    #재귀 함수로 remove 알고리즘을 구현한다.
    #cur 는 root 에서 시작
    def __remove_recursion(self, cur, target):
        # 첫번째 탈출조건
        # 트리에 target data 가 없을 때, None을 반환하고 나온다.
        # 밑으로 내려가면서 target data 를 못 찾으면,
        if not cur:
            return None, None
        # target data 가 현재 data 보다 작으면 왼쪽 서브트리로 진행한다.
        elif target < cur.data:
            cur.left, rem_node = __remove_recursion(cur.left, target)
        # target data 가 현재 data 보다 크면 오른쪽 서브트리로 진행한다.
        elif target > cur.data:
            cur.right, rem_node = __remove_recursion(cur.right, target)

        # 두번째 탈출조건
        # target data를 찾았을 때,
        else:
        # 1. 자식 노드가 0개 일 때 (= 리프노드를 지울때)
            if not cur.left and not cur.right:
                rem_node = cur
                cur = None
        # 2. 자식 노드가 1개 일 때
            # 오른쪽이 None -> 왼쪽 자식이 있을 때,
            elif not cur.right:
                rem_node = cur
                cur = cur.left
            # 왼쪽이 None -> 오른쪽 자식이 있을 때,
            elif not cur.left:
                rem_node = cur
                cur = cur.right
        # 3. 자식 노드가 2개 일 때
            else:
                #대체 노드 찾기 :
                #(1) 왼쪽 서브트리에서 가장 큰노드
                #or
                #(2) 오른쪽 서브트리에서 가장 작은노드

                #(1)여기서는 왼쪽 서브트리에서 가장 큰노드
                replace = cur.left
                while replace.right:
                    replace = replace.right
                cur.data, replace.data = replace.data, cur.data
                cur.left, rem_node = __remove_recursion(cur.left, replace.data)

                # (2)만약 오른쪽 서브트리 중 가장 작은 노드를 대체노드로 한경우,
                # replace = cur.right
                # while replace.left:
                #     replace = replace.left
                # cur.data, replace.data = replace.data, cur.data
                # cur.right, rem_node = __remove_recursion(cur.right, replace.data)

        return cur, rem_node



    #유저프로그래머가 사용하게 될 .remove() 메소드
    def remove(self, target):
        #Root를 항상 업데이트 해주어야한다. 루트 노드의 변경 가능성을 생각.
        self.root, removed_node = self.__remove_recursion(self.root, target)

        if removed_node:
            #삭제된 노드의 자식 노드를 모두 None 으로 만든다.
            removed_node.left = removed_node.right = None

        #삭제된 노드를 리턴하여, UserProgrammer에게 반환한다.
        return removed_node
