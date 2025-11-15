#function is reusable block of code that perform specific task
#uses def
#positional argument is argument that is passed to function BASED on its position.
#default argument is argument is use automatic paramenter if there is no argument is passed
#keyword argument is argument that need the explicit nameing of parameter when passing values.
def greet(name:str,lname:str):
    return f'hello {name}'
print(greet('hanna','kebede'))