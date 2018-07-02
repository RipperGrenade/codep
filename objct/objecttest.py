from desc import descriptortest


class ObjTest:
    """descriptor in here"""
    ciptor = descriptortest.DescripClass('class_val', 20)
    clsvar = 'static class var'

    def getpval(self, propertyval='this is property value'):
        self.tmpval = propertyval + 'modified'
        print('Pppppppppproptyyyyyy vallllllllll', self.tmpval)
        return self.tmpval

    @staticmethod
    def getpvalstatic():
        print('staticcccc descriptor property')

    propval = property(getpval)
    staticpval = property(getpvalstatic)

    def __init__(self):
        self.desctr = descriptortest.DescripClass('instance_method', 10)
        self.cval = 0
        self.__privVar = 'private var by two leading underscores'
        self.tmpval = ''

    def getdesc(self):
        return self.desctr

    @classmethod
    def clsmethod(cls):
        print('this is class methond:', cls.clsvar)

    @staticmethod
    def staticmethod():
        print('accessing static method')

    def instmethod(self):
        print('instance method accessing', self.cval)
        print('instance self type', type(self), '\n\n')
