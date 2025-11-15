#tuples is collection of  ordered, immunatble
names = ['hanna','alex',1,23,4.6,True]

list = tuple()

print(type(names))

str = list(names)
str[0]='abc'
print(str)