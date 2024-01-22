
#تمرین : با استفاده از ساختمان داده پشته تابع ای را بنویسید که عددی را از مبنای 10 به 2 ببرد
    def dec2bin(number):
        s=Stack()
        while number>0:
            r=number%2
            s.push(r)
            number=number//2

        b=""
        while not s.is_empty():
            b=b+str(s.pop())
            return b

    def is_empty(self):
        if len(self.stack)<=0:
            return True
        else:
            return False
        