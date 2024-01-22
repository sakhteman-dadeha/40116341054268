
#تمرین :با اسفاده از پشته تابع ای بنویسید که محتوای یک لیست را معکوس کند
    
    def reverse(lst):
        s=Stack()
        for e in lst:
            s.push(e)
        for i in range(len(lst)):
            lst[i]=s.pop()

    def revers_Stack(s):
        s1=Stack()
        s2=Stack()
        while not s.is_empty():
            s1.push(s.pop())
        while not s1.is_empty():
            s2.push(s1.pop())
        while not s2.is_empty():
            s.push(s2.pop())

    def respost(self, lst):
        for e in lst:
            if e == '*':
                t2 = self.pop()
                t1 = self.pop()
                if t1 is not None and t2 is not None:
                    t = t1 * t2
                    self.push(t)

            elif e == '+':
                t2 = self.pop()
                t1 = self.pop()
                if t1 is not None and t2 is not None:
                    t = t1 + t2
                    self.push(t)

            elif e == '-':
                t2 = self.pop()
                t1 = self.pop()
                if t1 is not None and t2 is not None:
                    t = t1 - t2
                    self.push(t)

            elif e == '/':
                t2 = self.pop()
                t1 = self.pop()
                if t1 is not None and t2 is not None and t2 != 0:
                    t = t1 / t2
                    self.push(t)
            else:
                self.push(e)
        return self.pop()
