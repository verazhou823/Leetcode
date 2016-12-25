class Node(object):
    def __init__(self,key,value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dic = dict()
        self.cap = capacity
        self.fakehead = Node(0,0)
        self.tail = Node(0,0)
        self.fakehead.next = self.tail
        self.tail.prev = self.fakehead


    def get(self, key):
        """
        :rtype: int
        """
        if self.dic.get(key):
            value = self.dic.get(key).val
            if self.dic.get(key) != self.tail.prev :
                self.rem(key)
                self.add(key,value)
            return value
        else:
            return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if self.dic.get(key):
            self.rem(key)
        elif len(self.dic) == self.cap:
            head = self.fakehead.next.key
            self.rem(head)
        self.add(key,value)
        return

    def add(self,key,value):
        newNode = Node(key,value)
        newNode.prev = self.tail.prev
        newNode.prev.next = newNode
        newNode.next = self.tail
        self.tail.prev = newNode
        self.dic[key] = newNode

    def rem (self,key):
        remNode = self.dic.get(key)
        remNode.prev.next = remNode.next
        remNode.next.prev = remNode.prev
        self.dic.pop(key)



lru = LRUCache(3)
lru.set(1,1)
lru.set(2,2)
print(lru.get(1))
lru.set(3,3)
lru.set(4,4)
print(lru.get(4))
print(lru.get(3))
print(lru.get(2))
print(lru.get(1))
print(lru.fakehead.next.key)
print(lru.tail.key)
lru.set(5,5)
print(lru.get(1))
print(lru.get(2))
print(lru.get(3))
print(lru.get(4))
print(lru.get(5))
