##BMI project
print('------BMI CALCULATOR------')
weight = int(input('Input your weight : '))
height = float(input('Input your height : '))

if (height > 100 or height > 3):
    raise Exception("Number height must be float! eg : 1.7")
else:
    BMI = weight/(height*height)

    print('\nYour BMI is ',BMI)

    if(BMI >0):
        if BMI <= 16:
            print('Status : very underweight\n')
        elif BMI <= 18.5:
            print('Status : Underweight\n')
        elif BMI <= 25:
            print('Status : Healthy\n')
        elif BMI <= 30:
            print('Status : Overweight\n')
        elif BMI >= 30:
            print('Status : Over Weight')
    
    else:print('Status : invalid\n')
