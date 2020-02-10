class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self._data == []:
            return None
        return self._data.pop()

    def top(self):
        if self._data:
            return self._data[-1]
        else:
            return ''

    def show(self):
        print(self._data)

    def get_size(self):
        return len(self._data)


class Queue:
    def __init__(self):
        self._data = []

    def put(self, item):
        self._data.append(item)

    def get(self):
        if self._data == []:
            return None
        res = self._data[0]
        self._data.remove(res)
        return res

    def show(self):
        print(self._data)


class LinkNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def append(self, data):
        item = self
        while item.next is not None:
            item = item.next
        item.next = LinkNode(data)
        return self

    def travel(self):
        item = self
        while item is not None:
            print(item.data)
            item = item.next

    def travel_get(self):
        item = self
        while item is not None:
            yield item
            item = item.next

    def travel_get2(self):
        item = self
        res=[]
        while item is not None:
            res.append(item)
            item = item.next
        return res

    def order(self, data):
        pre=self
        temp=LinkNode(data)
        for item in self.travel_get():
            if item.data > data:
                break
            pre=item
        temp.next=pre.next
        pre.next=temp
        return self

    def order2(self, data):
        item = self
        pre=self
        temp = LinkNode(data)
        while item is not None:
            if item.data > data:
                break
            pre = item
            item=item.next
        temp.next = pre.next
        pre.next = temp
        return self

    def search(self, data):
        item = self
        index = 0
        while item is not None:
            if item.data == data:
                return index
            index += 1
            item = item.next
        return -1

    def insert(self, pos, data):
        item = self
        index = 0
        while item is not None:
            if index == (pos - 1):
                break
            index += 1
            item = item.next
        temp = LinkNode(data)
        temp.next = item.next
        item.next = temp


class BTree:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def travel(self, subtree):
        if subtree is None:
            return
        print(subtree.data)
        self.travel(subtree.left)
        self.travel(subtree.right)

    def max_depth(self, subtree, depth):
        if subtree is None:
            return depth

        max_left = self.max_depth(subtree.left, depth + 1)
        max_right = self.max_depth(subtree.right, depth + 1)
        return max_left if max_left > max_right else max_right


class MethodToBeTested:
    def __init__(self):
        self._stack = Stack()

    # 给定一个字符串{xxx[xxx{xxx}]xx{x[xxx]xxx{xxx}xx}x}判断其中的 {}[]() 是否成对出现
    #   该代码有问题，不能实现成对出现的功能
    def match_brackets(self, items):
        for i in items:
            if i in "{[(":
                self._stack.push(i)
            elif i in ")]}":
                ret = self._stack.pop()
                if ret is None:
                    return 99999
        return self._stack.get_size()

    # 判断字符串中 []{}() 是否完全配对出现
    def parrent_brackets(self, items) -> bool:
        for i in items:
            if self._stack.top() + i in ["{}", "[]", "()"]:
                self._stack.pop()
            else:
                self._stack.push(i)
        return self._stack.get_size() == 0



# if __main__ == '__main__':
class TestDataStruct:
    def setup(self):
        self._stack = Stack()
        self._method = MethodToBeTested()
        self._queue = Queue()

    def test_stack(self):
        self._stack.push(1)
        self._stack.push(2)
        self._stack.push(3)
        self._stack.push(4)
        self._stack.show()
        assert self._stack.pop() == 4
        assert self._stack.pop() == 3
        assert self._stack.pop() == 2
        assert self._stack.pop() == 1
        assert self._stack.pop() is None
        self._stack.show()

    # 给定一个字符串{xxx[xxx{xxx}]xx{x[xxx]xxx{xxx}xx}x}判断其中的 {}[]() 是否成对出现
    def test_match(self):
        data = "{xxx[xxx{xxx}]xx{x[xxx]xxx{xxx}xx}x}"
        assert self._method.match_brackets(data) is True
        data1 = "{xxx[xxx(xxx}]xx{x[xxx]xxx{xxx}xx}x}"
        assert self._method.match_brackets(data1) is True
        data2 = "{xxx[xxx}]xx{x[xxx]xxx{xxx}xx}x}"
        assert self._method.match_brackets(data2) is False

    def test_parrent(self):
        assert self._method.parrent_brackets("[]") is True
        assert self._method.parrent_brackets("[{}]") is True
        assert self._method.parrent_brackets("[{()}]") is True

        assert self._method.parrent_brackets("[") is False
        assert self._method.parrent_brackets("[{)]") is False
        assert self._method.parrent_brackets("[{(}])") is False

    def test_queue(self):
        self._queue.put(1)
        self._queue.put(2)
        self._queue.put(3)
        assert self._queue.get() == 1
        assert self._queue.get() == 2
        assert self._queue.get() == 3

    def test_link(self):
        link = LinkNode(0)
        link.append(1).append(2).append(3).append(4)
        link.travel()
        print(link.search(0))
        link.insert(3, 2.5)
        link.travel()

    def test_link_order(self):
        link = LinkNode(0)
        link.order(5).order(3).order(1).order(4).order(2)
        data=[item.data for item in link.travel_get()]
        print(data)
        assert data == [0,1,2,3,4,5]

    def test_link_order2(self):
        link = LinkNode(0)
        link.order2(5).order2(3).order2(1).order2(4).order2(2)
        data=[item.data for item in link.travel_get2()]
        print(data)
        assert data == [0,1,2,3,4,5]


    def test_btree(self):
        ''' 0
          1     2
        3 4 | 5 6 '''
        tree = BTree(0)
        tree.left = BTree(1)
        tree.right = BTree(2)
        tree.left.left = BTree(3)
        tree.left.right = BTree(4)
        tree.right.left = BTree(5)
        tree.right.right = BTree(6)
        tree.left.left.right = BTree(7)
        tree.travel(tree)
        print(tree.max_depth(tree, 0))
