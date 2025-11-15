#declaring dictionary
#student = dic()
students = {'name':'hanna', 'age':'26', 'sec':'B'}

#using length
print(len(students))

#accessing element
print(students['name'])

#adding item
students['last_name']= 'kebede'
students['first_name']= 'abebe'
print(students)

#modifying(update) item
students['last_name']='yakob'
print(students)

#check if the key exist
print('name' in students)

#remove item from dictionary
students.pop('fist_name')

#get the key in the list
print(students.key)

#get the value in the list
print(students.value)

