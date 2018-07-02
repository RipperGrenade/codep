if __name__ == '__main__':
    lst = [1, 'h', 4, 'hl', 'hello', 'python']
    it = lst.__iter__()
    nele = it.__next__()
    print('next', nele)
    for element in it:
        print(element)
    # while it.__next__() is not StopIteration:
    # print(it.__next__())
    # while next(it):
    # print(next(it))
    for element in iter(lst):
        print(element)
    for element in lst.__iter__():
        print(element)
    for element in lst:
        print(element)

    itera = iter(lst)
    tupleit = tuple(itera)
    print(tupleit)
    for element in tupleit:
        print(element)
    for element in iter(tupleit) or tupleit.__iter__() or range(30):
        print(element)
    it2 = tupleit.__iter__()
    tupe2 = tuple(it2)
    print(tupe2)

if __name__ == '__main__':
    dic = {'f': 1, 'j': 'hello', '4': 'rop', 6: 'world'}

    for key in iter(dic):
        print(key, type(key))
        print(dic[key], type(dic[key]))

if __name__ == '__main__':
    linelst = ['a\n', 'hello\n', 'b\n', 'world\n']
    generator_exp = (line.strip() for line in linelst if len(line) > 2)
    for element in generator_exp:
        print(element)
    complist = [line.strip() for line in linelst if len(line) < 9]
    print(type(complist))
    print(type(generator_exp))


    def exp(val):
        reslt = 0
        for ele in val:
            if isinstance(ele, str):
                ele = int(ord(ele[0]))
            reslt += ele
        return reslt

numlist = [1, 2, 3, 4, 9, 0]
letterlist = ['a', 'b', 'c']

print(exp(element for ele in linelst if len(ele) > 0
          for ele in numlist if ele > 0))

numletterlst = [(x, y) for x in numlist for y in letterlist]
numletter_iter = ((x, y) for x in numlist for y in letterlist)
print(numletterlst)
for com in numletter_iter:
    print(com)

if __name__ == '__main__':
    def upper(s):
        return s.upper()


    llist = ['a', 'b', 'c', 'python', 'hello']
    print(ord('a'), '  ', ord('z'))
    upplist = [upper(s) for s in llist]
    print('list comprehension', upplist)
    upptuple = (upper(s) for s in llist)
    print('generator expression', upptuple)


    def geniter(num):
        while num >= 97:
            val = yield chr(num)
            print('yield returnval ', val)
            if val is not None:
                print('sent val', val)
                num = ord(val)
            else:
                num -= 1


    for va in geniter(100):
        print(va)

    print(map(upper, llist))
    print(list(map(upper, llist)))
    print(tuple(map(upper, llist)))

    mapiteratorlist = list(map(upper, geniter(100)))
    print(mapiteratorlist)

    it = geniter(100)
    print(next(it))
    it.send('p')
    for element in it:
        print(element)
