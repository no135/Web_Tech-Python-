class student: #define a class
    def __init__(self, name): #constructor method which is called when creating instance
        self.name = name #store name in instance
    def greet(self):#method to greet the student
        return f'hello {self.name}' # return greeting the student

stu_obj = student('hanna') #create object using python
print (stu_obj.greet()) #call print method and print
print(stu_obj) #print

class Passengers:
    def __init__(self,name,passport_no):
        self.name = name
        self.passport_no = passport_no

    def __str__(self):
        return self.name

class Flight:
    def __init__(self):
        self.destination
        self.departure
        self.passanger = []
        self.capacity
    def add_passenger(self,name,passport_no):
        obj =  Passengers(name,passport_no)
        if self.capacity <= self.passanger.count():
            return f'Flight is full'
        else :
            self.passanger.append(obj)
            return f'You have successfully booked Flight'




