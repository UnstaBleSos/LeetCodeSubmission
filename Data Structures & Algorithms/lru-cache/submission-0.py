class DoublyList:
    def __init__(self,key=0,val=0,prev=None,next=None):
        self.prev = prev
        self.next = next
        self.key = key
        self.val = val

class LRUCache:
    def __init__(self, capacity: int):
        self.size = capacity
        self.cache={}
        self.head = DoublyList()
        self.tail = DoublyList()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        node.prev.next = node.next
        node.next.prev = node.prev

        oldhead = self.head.next

        node.prev = self.head
        self.head.next = node

        node.next = oldhead
        oldhead.prev = node

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            node.prev.next = node.next
            node.next.prev = node.prev
            oldhead = self.head.next
            node.prev = self.head
            self.head.next = node
            node.next = oldhead
            oldhead.prev = node
        else:
            newNode = DoublyList(key,value)
            self.cache[key] = newNode
            oldhead = self.head.next
            newNode.prev= self.head
            self.head.next = newNode
            newNode.next = oldhead
            oldhead.prev = newNode
            if len(self.cache)>self.size:
                lru = self.tail.prev
                lru.prev.next = lru.next
                lru.next.prev = lru.prev

                
                
                self.cache.pop(lru.key)