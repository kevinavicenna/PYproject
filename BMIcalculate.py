##BMI project

weight = int(input('Bobot '))
height = int(input('tinggi badan '))

BMI = weight/(height*height)

print('\nYour BMI is ',BMI)

if(BMI >0):
    if BMI <= 16:
        print('very underweight\n')
    elif BMI <= 18.5:
        print('underweight\n')
    elif BMI <= 25:
        print('Healthy\n')
    elif BMI <= 30:
        print('Overweight\n')
else:print('invalid cuy\n')