# Redblack tree
- Balanced Binary Tree(균형이진트리) 중 하나

### 왜 Balnced Binary Tree ?
- BST의 최악의 경우, search 메소드의 Big-O $O(n)$
(example) key 가 1 -> 2 -> 3 -> ... -> 8 이렇게 들어온다면,
오른쪽 자식에 계속해서 붙어 나갈 것이다.
- 노드가 insert, delete 될 때, tree 가 균형을 알아서 맞춰주면 좋겠다...
- Balnced Binary Tree 의 종류
  1. AVL
  2. Redblack Tree
  3. B Tree
  4. B+ Tree
  5. 2-3 Tree
  6. 2-3-4 Tree

- 레드블랙트리의 경우, 최악의 경우 Big-O 는 O(logn)

### Redblack Tree의 정의 & Regulation
1. 트리의 모든 노드는 <span style="color:red"><b>Red</b></span> 아니면 <b>Black</b>
2. 루트와 외부 노드의 컬러는 <b>Black</b>
3. 루트에서 외부 노드로의 경로 중에 <span style="color:red"><b>Red</b></span> 노드가 연속으로 나올 수 없다.
(== <span style="color:red"><b>Red</b></span>의 자식 or 부모는 같은 <span style="color:red"><b>Red</b></span> 일 수 없다.)
4. 루트에서 외부 노드로의 모든 경로에서 <b>Black</b>노드의 수는 같다.


### Redblack Tree의 insert
1. BST insert
2. new_node의 color 를 <span style="color:red"><b>Red</b></span> 로 한다.
  - root node 에 new_node 는 정의에 의해 Black
3. Insert_fix 함수 호출
  - Redblack의 Regulation을 따르도록 재배열 한다.

### Redblack Tree의 insert_fix
1. Root 노드가 <span style="color:red"><b>Red</b></span>
  - Root 노드를 <b>Black</b>으로 바꾼다.

2. New_node 와 그 parent 노드가 전부 <span style="color:red"><b>Red</b></span> 이면, Regulation 에 위반하므로, 이를 고려준다.
  - 총 8개의 Case

Case | 종류                                               | 해결방법  |
-----|----------------------------------------------------|-----------|
LLr  | Uncle 이 <span style="color:red"><b>Red</b></span> |           |
LRr  | Uncle 이 <span style="color:red"><b>Red</b></span> |           |
LLb  | Uncle 이 <b>Black</b>                              |           |
LRb  | Uncle 이 <b>Black</b>                              |           |
RLr  | Uncle이 <span style="color:red"><b>Red</b></span>  | 위와 대칭 |
RRr  | Uncle 이 <span style="color:red"><b>Red</b></span> | 위와 대칭 |
RLb  | Uncle 이 <b>Black</b>                              | 위와 대칭 |
RRb  | Uncle 이 <b>Black</b>                              | 위와 대칭 |


### [New_node의 Parent 노드가 GrandParent의 왼쪽 자식인 경우]
1. XYr : Uncle 이 <span style="color:red"><b>Red</b></span> 인 경우,(=== 부모 레벨이 모두 <span style="color:red"><b>Red</b></span> )<br>
  (1) GrandParent 의 색(<b>Black</b>)을 <span style="color:red"><b>Red</b></span> 로 변경 <br>
  (2) Parent 의 색(<span style="color:red"><b>Red</b></span>)을 <b>Black</b>으로 변경 <br>
  (3) new_node label 을 GrandParent, parent label 을 GrandParent의 parent 로 변경 <br>
  (4) 이 때, 새로운 parent 가(즉, GrandParent의 parent 가 <b>Black</b>이면, 종료.
  <span style="color:red"><b>Red</b></span> 이면 반복해서 실행

2. XYb : Uncle 이 <b>Black</b>
(1) Parent 노드를 기준으로, Left-Rotate <br>
(2) GrandParent 노드를 <span style="color:red"><b>Red</b></span>로, parent 노드를 <b>Black</b> 으로 색을 바꾼다.
(3) Parent 노드를 기준으로, Right-Rotate <br>
