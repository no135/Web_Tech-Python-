#using fizz for divisibility by 3 ,buzz for divisibility by5 and fizzbuzz for divisibility by 3 and 5
print ('fizz buzz')

num = int(input('input number : '))

if num % 3 ==0 and num % 5 ==0:
        print('FizzBuzz')

elif num % 3 ==0:
    print ('Fizz')


elif num % 5 ==0:
        print('buzz')

else:
    print(num)