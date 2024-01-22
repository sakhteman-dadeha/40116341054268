
class Dnode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# کلاس لینک لیست چرخشی 
class Clinkedlist:
    def __init__(self):
        self.head = None
# نمایش
    def display(self):
        t = self.head
        if t is None:
            print("empty")
            return
        while t.next != self.head:
            print(t.data, end="-->")
            t = t.next

        print(t.data)
# اضافه در ابتدا
    def addfirst(self, data):
        n = Dnode(data)
        if self.head is None:
            self.head = n
            n.next = n
            return
        n.next = self.head
        t = self.head
        while t.next != self.head:
            t = t.next

        t.next = n
        self.head = n
#  ... اضافه بعد از 
    def addafter(self, m, data):
        if self.head is None:
            return -1

        n = Dnode(data)
        t = self.head
        while t.data != m:
            t = t.next
            if t == self.head:
                return -1

        n.next = t.next
        t.next = n
# حذف
    def delete(self, data):
        if self.head is None:
            print("empty")
            return
        if self.head.next == self.head:
            if self.head.data == data:
                self.head = None
                return
            return -1
        t = self.head
        while t.data != data:
            p = t
            t = t.next
            if t == self.head:
                return -1

        p.next = t.next
        t.next = None