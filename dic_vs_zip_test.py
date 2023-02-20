a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c = {}
c = dict(zip(a, b))
print(c)
c['a'] = c['a'] + 111
print(c['a'])