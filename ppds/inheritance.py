class A:
    def afun(self):
        print('This is a A Funtion')

class B(A):
    def bfun(self):
        print("This is a B Function")

class C(A):
    def cfun(self):
        print("This is a C Function")

class D(B,C):
    def dfun(self):
        self.afun()
        self.bfun()
        self.cfun()
        print('This is a D Funtion')
    
data = D()
data.dfun()