# BST : Binary Search Tree

## 1. BST의 특징
1. 모든 원소는 서로 다른 key를 가진다.
  - 이는 key가 같은 중복 데이터를 가질 수 없다는 의미!
2. 왼쪽 서브트리에 있는 모든 key들은 루트의 key 보다 작다.
3. 오른쪽 서브트리에 있는 모든 key들은 루트의 key 보다 크다.
4. 왼쪽 서브 트리와 오른쪽 서브트리도 이진탐색 트리이다.

## 2. BST의 ADT (Abstract Data Type : 추상 자료형)
- 구현을 해보기 위해, BST가 가질 ADT를 정리합니다.

```python
# 데이터 삽입
BST.insert(data) # return None

# 데이터 searching
BST.search(target) # return 해당 Node

# 데이터 remove
# BST에 해당 데이터가 있으면, 데이터를 가진 노드를 삭제하고, 그 노드를 반환
BST.remove(target) # returns 해당 Node

# remove에서 받은 노드의 데이터를 수정 후,
# 다시 삽입할 때 사용
BST.insert_node(node) # return None
```

## 3. BST의 구현

### 3-1. BST.remove
---
##### cf) Remove 와 Delete 의 차이
- 구어에서는 큰 차이가 없을 수 있겠지만, 현업 프로그래밍에서는 Remove 와 Delete를 구분한다고 한다.

Remove  |  제거할 target data를 set 에서 제거한 후, 제거된 target data 를 return 한다.
--|--
<b>Delete  |  <b>제거할 target data를 set 에서 제거한 후, return 하지 않는다.

- 보통 Remove 기능으로 구현하는게 일반적
- UserProgrammer 에게 제거된 target data 의 활용방안 권한을 넘김으로써, target data 의
object 를 활용 할 수 있도록 해준다.
---

##### Remove Case
- target 과 cur.data 를 비교해서, 밑으로 내려간다. 찾은 경우 다음의 Case 로 실행

1. 자식 노드가 0일 때 (= 지울 노드가 리프노드)
  - 지우려는 노드 (rem_node) 가 cur 가 되고,
  - cur 는 None 자식노드인 None 을 준다.


2. 자식 노드가 하나일 때
  - 왼쪽자식만 있는 경우,
  - rem_node 를 지우고, cur 왼쪽 자식에게 준다.(오른쪽 자식만 있는 경우, cur 를 오른쪽 자식에게 준다.)
3. 자식 노드가 두개일 때
  - 대체노드를 찾는다.
  - 대체노드의 경우 왼쪽 서브트리에서 가장큰노드 or 오른쪽 서브트리에서 가장 작은 노드로 찾는다.
  - 대체노드와 target을 임시적으로 바꾸고, 서브트리를 root 를 생각하여 대체노드위치에 있는 target 을 지운다.
