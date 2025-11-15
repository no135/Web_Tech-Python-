name = input('input name: ')
weight = int(input('input weight: '))
height = float(input('input height(in Meter): '))
age = int(input('input age: '))
gender = input('input gender(male/female): ').lower()

def BMI(weight,height):
   return weight/(height*height)

def BMI_catagory(bmi):
    if bmi<18.5:
        return "You are underweight"
    elif bmi<25:
        return "You are normal weight"
    elif bmi<30:
        return "You are overweight"
    else:
        return "You are obese"

def BMR(weight,height,age,gender):
    height_cm = height*100
    if gender == "male":
        return 88.36+(13.4*weight)+(4.8*height_cm)-(5.7*age)
    else:
        return 447.6+(9.2*weight)+(3.1*height_cm)-(4.3*age)

bmi = BMI(weight,height)

print(bmi)
print(BMI_catagory(bmi))
print("you need "+str(BMR(weight,height,age,gender))+" clories")
