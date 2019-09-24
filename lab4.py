class University:
    def __init__(self):
        self.name =" "
        self.age = 0
        self.mark = 0
    def validatemarks(self):
        if self.mark>0 and self.mark<100:
            return True
        else:
            return False
    def validateage(self):
        if self.age>20:
            return True
        else:
            return False
    def check_quali(self):
        if self.validatemarks()and self.validateage():
            if self.mark>=65:
                return True
            else:
                return False
        else:
            return False
    def setter(self,n,a,m):
        self.name=n
        self.age=a
        self.mark=m
    def getter(self):
        print("name",self.name)
        print("age",self.age)
        print("mark",self.mark)
        if self.check_quali():
            print("given information is valild")
        else:
            print("invalid info")

s1=University()
s1.setter("xyz",22,85)
s1.getter()
s2=University()
s2.setter("abc",21,35)
s2.getter()
