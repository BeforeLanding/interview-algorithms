"""146. LRU 缓存
题目：https://leetcode.cn/problems/lru-cache/
题意：实现 get、put，容量满时淘汰最久没有被访问的键。

思路：字典按 key 找节点，双向链表维护使用顺序。
使用一个循环哨兵 dummy：dummy.next 最新，dummy.prev 最旧。
命中 get 或更新 put 时，把节点移到表头；超容量时删掉表尾和字典记录。
每次 get/put 平均 O(1)，空间 O(capacity)。节点保存 key，方便淘汰时删除字典项。

参考：灵茶山艾府，单哨兵循环双向链表思路；重新整理辅助函数与示例。
https://leetcode.cn/problems/lru-cache/solutions/2456294/tu-jie-yi-zhang-tu-miao-dong-lrupythonja-czgt/
"""


class Node:
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.prev = self
        self.next = self


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes: dict[int, Node] = {}
        self.dummy = Node()

    def _remove(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def _push_front(self, node: Node) -> None:
        first = self.dummy.next
        node.prev = self.dummy
        node.next = first
        first.prev = node
        self.dummy.next = node

    def _touch(self, node: Node) -> None:
        self._remove(node)
        self._push_front(node)

    def get(self, key: int) -> int:
        node = self.nodes.get(key)
        if node is None:
            return -1
        self._touch(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.nodes.get(key)
        if node is not None:
            node.value = value
            self._touch(node)
            return
        node = Node(key, value)
        self.nodes[key] = node
        self._push_front(node)
        if len(self.nodes) > self.capacity:
            oldest = self.dummy.prev
            self._remove(oldest)
            del self.nodes[oldest.key]


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 10)
    cache.put(2, 20)
    assert cache.get(1) == 10  # 访问后 1 最新，2 最旧
    cache.put(3, 30)
    assert cache.get(2) == -1
    cache.put(1, 100)  # 更新已有键，也会变成最新
    cache.put(4, 40)
    assert cache.get(3) == -1
    assert cache.get(1) == 100
    assert cache.get(4) == 40
    single = LRUCache(1)
    single.put(0, 0)
    single.put(5, 50)
    assert single.get(0) == -1
    assert single.get(5) == 50
    print("146. LRU 缓存：通过")
