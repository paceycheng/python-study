# -*- coding: utf-8 -*-

paragraph = '''
Most discussions of GraphQL focus on data fetching, but any complete data platform needs a way to modify server-side data as well.
In REST, any request might end up causing some side-effects on the server, but by convention it's suggested that one doesn't use GET requests to modify data. GraphQL is similar - technically any query could be implemented to cause a data write. However, it's useful to establish a convention that any operations that cause writes should be sent explicitly via a mutation.
Just like in queries, if the mutation field returns an object type, you can ask for nested fields. This can be useful for fetching the new state of an object after an update.
'''

#print(paragraph)

# Q1: 印出這個段落的長度
print('-----A1-----')
a = len(paragraph)
print(a)


# Q2: 把文章裡 'GraphQL' 這個單字變全大寫, 其餘單字變全小寫
print('-----A2-----')
pp = paragraph.upper()
pp=pp.replace('GRAPHQL','graphql')
print(pp.swapcase())

# Q3: 印出這個段落有多少個英文單字(不含標點符號與空白)
print('-----A3-----')
b = paragraph.count(' ')
c = paragraph.count(',')
d = paragraph.count('\'')
print(a - b - c - d )


# Q4: x = 1, y = 6, 把兩個變數的值交換, 讓他變成 x = 6, y = 1, 只能使用加減乘除, 不能使用第三個變數
print('-----A4-----')
x = 1
y = 6

x = x + 5
y = y - 5
print(x)
print(y)