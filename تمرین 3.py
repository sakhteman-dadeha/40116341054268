
#تابع ای بنویسید که در عبارت پرانتز باز و بسته  را چک کند
    def match_s(self, str):
        pairs = {')': '(', ']': '[', '}': '{'}
        for i in str:
            if i in '({[':
                self.push(i)
            elif i in ')]}':
                if self.is_empty() or self.peek() != pairs[i]:
                    return False
                else:
                    self.pop()
        return self.is_empty()
