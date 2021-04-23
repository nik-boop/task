
class ring:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return f'{self.val}'

    def data(self):
        return self.val

    def Next(self, next):
        self.next = next
        return self.next

    def Head(self, next):
        self.next = next
        return self


class listr:
    def __init__(self, val=None):
        if val is not None:
            try:
                iterator = iter(val)
            except TypeError:
                self.head = ring(val)
                self.last = self.head
            else:
                #List = list(val)
                self.head = ring(val[0])
                self.last = self.head
                for i in val[1:]:
                    self.append(i)
        else:
            self.head = None
            self.last = None

    def __len__(self):
        return self.len()

    def append(self, val):
        if self.head == None:
            self.head = ring(val)
            self.last = self.head
        else:
            self.last = self.last.Next(ring(val))

    def show(self):
        if self.head == None: return None
        a = self.head
        while a.next != None:
            yield a.data()
            a = a.next
        else:
            yield a.data()
    def listr(self):
        if self.head == None: return None
        a = self.head
        while a.next != None:
            yield a
            a = a.next
        else:
            yield a

    def Head(self,var):
        if self.head == None:
            self.head = ring(var)
            self.last = self.head
        else:
            self.head = ring(var).Head(self.head)
    def len(self):
        if self.head == None: return 0
        else: k=0
        a = self.head
        while a.next != None:
            a = a.next
            k+=1
        else:
            k+=1
        return k

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False
    def find(self,number = None, value = None):
        if number != None:
            if number > self.len()-1 or number < 0 : return 'IndexError'
            a = self.head
            for i in range(number):
                a = a.next

            return a

    def rewrit(self,number,value):
        self.find(number).val = value

    def pop(self,number = None):
        fl = False
        if number is None: number = self.len() - 1; fl = True
        if self.head is None: return None
        if number > self.len()-1 or number < 0 : return 'IndexError'
        if number == 0:
            var = self.head.data()

            if self.head.next is not None:
                if self.len() != 2:
                    self.head = self.head.next
                else:
                    self.head = self.head.next
                    self.last = self.head
            else:
                self.head=None
                self.last=None
            return var
        a = self.head
        for i in range(number-1):
            a = a.next
        else:
            var = a.next.data()
            if fl != True:
                a.Next(a.next.next)
            else:
                a.Next(None)
            return var

#Тест
l = listr([-5, -4, -3, -2, -1, 0, 1])
l.append(2)
for i in range(3,10):
    l.append(i)
print(l.head.data(),l.last.data())
l.Head(-6)
l1 = listr()
print(list(l.show()))
print(len(l))
print(l1.pop())
print(list(l.show()))
print(l.find(len(l)-1).data())
