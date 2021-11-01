def fatloss_calories(weight,height,age,gender):
    if gender == 'male':
        sum = (10*weight + 6.25 * height - 5 * age + 5) - 200
        pro = sum/100*50
        carb= sum/100*30
        fats = sum/100*20
        total = print(str(carb) + ' calories from carbs'+'\n'+ str(pro) + ' calories from protein'+'\n'+str(fats)+ ' calories from fats')
        return total
    elif gender == 'female':
        sum = (10 * weight + 6.25 * height - 5 * age - 161) - 200
        pro = sum / 100 * 50
        carb = sum / 100 * 30
        fats = sum / 100 * 20
        total = print(str(carb) + ' calories from carbs' +'\n'+ str(pro) + ' calories from protein'+'\n'+ str(fats) + ' calories from fats')
        return total
    else:
        print('enter gender first')
