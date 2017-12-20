# -*- coding:UTF-8 -*-

a='中国：china'
print(a)

if a.__contains__('：'):
    print(a.index('：'))
    print(a[a.index('：')+1:])
