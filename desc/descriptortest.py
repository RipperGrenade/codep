class DescripClass:
    """descriptor test"""

    def __init__(self, val=None, initsize=0):
        self.val = val
        self.size = initsize

    def __get__(self, instance, owner):
        print("self descripting")
        return self.val

    def __set__(self, instance, value):
        print("set val:{0}".format(value))
        self.val = value

    def __delete__(self, instance):
        print("delete attr val and size")
        del self.val
        del self.size


class PropertyDescrip:
    """descriptor by Property()"""

    def __init__(self, val=None):
        if val is None:
            self.__val = 0
        else:
            self.__val = val

    def getvalbyp(self):
        print('getting val property')
        return self.__val

    def setvalbyp(self, sval):
        print('setting val property')
        self.__val += sval
        print('new __val:', self.__val)

    def delvalbyp(self):
        print('deleting val property')
        del self.__val

    val = property(getvalbyp, setvalbyp, delvalbyp, '_val is a property reachable by methdo property')


if __name__ == '__main__':
    objPropty = PropertyDescrip(2000)
    print(objPropty.val)
    objPropty.val = 300
    del objPropty.val

if __name__ == '__main__':
    descobj = DescripClass()
    print('descobj class', descobj)


class ClassInst:
    def __init__(self):
        self.val = 0

    def clsmethod(self, val):
        print('in class method, test function descriptor')
        self.val = val
        return self.val

    @staticmethod
    def staticmethod():
        print('in static method')

    @classmethod
    def clsclsmethod(cls):
        print('class method for function descriptor')


if __name__ == '__main__':
    ClassInst.staticmethod()
    ClassInst.clsclsmethod()
    for i in range(10):
        print('\n')

if __name__ == '__main__':
    clsinst = ClassInst()
    print(clsinst.clsmethod(2))
    print(clsinst.clsmethod)
    print(clsinst.clsmethod.__func__)
    print(clsinst.clsmethod.__self__)
    print(clsinst.clsmethod.__class__)
    print(id(clsinst))
    print(id(clsinst.clsmethod))
    print(ClassInst.clsmethod)
    print(ClassInst.clsmethod.__qualname__)

    print('class method:::', clsinst.clsclsmethod())
    print('class method:::method', clsinst.clsclsmethod)
    print('class method:::__func__', clsinst.clsclsmethod.__func__)
    print('class method:::__self__', clsinst.clsclsmethod.__self__)
    print('class method:::__class__', clsinst.clsclsmethod.__class__)
    print('class method:::', id(clsinst))
    print('class method:::', id(clsinst.clsclsmethod))
    print('class method:::', ClassInst.clsclsmethod)
    print('class method:::', ClassInst.clsclsmethod.__qualname__)

    print(clsinst.staticmethod)
    print(clsinst.staticmethod.__class__)
    print(id(clsinst))
    print(id(clsinst.staticmethod))

    print(ClassInst.staticmethod.__qualname__)

    print(type(clsinst))
