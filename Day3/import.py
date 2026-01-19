from module import *
bmi = BMI(weight,height)

print("hello, your BMI is: "+ str(bmi))
print(BMI_catagory(bmi))
print("you need "+str(BMR(weight,height,age,gender))+" clories")


