names = list()
names = ['hanna','alex',1,23,4.6,True]
print(type(names))
print(len(names))
print(names[4])
print(names[-6])#using negative indexing which start from last value of the list
 
 #list unpacking
name = ['hanna','alex','abel','yakob','mike']
first, second, *third =name 
print (*third)

#list slicing
str = ['hanna','alex','abel','yakob','mike']
new_list = str[2:4]
print(new_list)

#negative slicing
new_list = str[-4:-2]
print (new_list)

#modify index
str[0] ='alem'
print (str)

#checking element in list
print('hanna' in str)

#add item to list
str.append('hanna')
print(str)

#insert item in specific index
str.insert(2,'kale')
print(str)

#remove item from list
str.remove('hanna')
print(str)

#clear all item
str.clear()
print(str)

#copy element
str1 = name.copy()
print(str1)

#joining list
num=[1,2,3,4,5]
newlist =num+name
newlist =num.extend(name)
print(newlist.count())

#finding an index
index = str.index('alem')
print(index)

