#multi level inheritence

class A:
    
    def __init__(self) -> None:
        print("init of class A")
    
    def featureA(self):
        print("feature one of A")

class B:
    
    def __init__(self) -> None:
        print("init of class B")
    
    def featureB(self):
        print("feature one of B")

class C(A,B):
    
    def __init__(self) -> None:
        super().__init__()
        print("init of class C")
    
    def featureC(self):
        print("feature one of C")


c = C()
c.featureC()
c.featureA()