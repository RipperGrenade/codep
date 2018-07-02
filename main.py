if __name__ == '__main__':
    str1 = 'alias applog="cd /Users/mark/Library/Logs;ls -laiFsu;pwd"'
    l1 = str1.split('="')
    print(l1)
    l2 = l1[0].split(' ')
    print(l2, type(l2[1]))
    (h, s, t) = l1[1].partition('cd ')
    print(t.split('!')[0])

    b = bytearray('python', 'utf-8')
    b.append(253)
    print(b)

# from objct import objecttest
#
#
# if __name__ == '__main__':
#     obj = objecttest.ObjTest()
#     obj.ciptor
#     objecttest.ObjTest.ciptor
#     print(obj.__dict__)
#     print(objecttest.ObjTest.__dict__)
#
#     objecttest.ObjTest.staticmethod()
#     objecttest.ObjTest.clsmethod()
#     obj.instmethod()
#     print('propval here')
#     obj.propval
#     objecttest.ObjTest.staticpval
#     print('propval here')
#
#     # obj.ciptor
#     # obj.__dict__['ciptor']
#     print(objecttest.ObjTest.__dict__['ciptor'])
#     print(objecttest.ObjTest.__dict__['ciptor'].__get__)
#     objecttest.ObjTest.__dict__['ciptor'].__get__(obj, obj)
#
#     import inspect
#     from desc import descriptortest
#     from objct import objecttest
#
#     desc1 = descriptortest.DescripClass()
#     print(inspect.getmro(descriptortest.DescripClass))
#
#     ojb2 = objecttest.ObjTest()
#     print(inspect.getmro(objecttest.ObjTest))
#
#     print(object.mro())
#     print(object.__dict__)
#     print(object.__bases__)
#     print(object.__module__)
#     print(object.__class__)
#
#     print(dir(ojb2))
#     print(dir(object))
