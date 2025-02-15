from random import randint

dice_imgs = ['1', '2', '3', '4', '5', '6']
dice_nums = randint(0, 5)
#randint(1, 6) 
print(dice_imgs[dice_nums])

#check leap or not
year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


#fizzbuzz
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)