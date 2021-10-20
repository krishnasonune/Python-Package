def maintenance_calories(weight,height,age,gender):
    if gender == 'male':
        sum = 10*weight + 6.25 * height - 5 * age + 5
        carbs = sum/100*60
        pro = sum/100*30
        fats = sum/100*20
        total = print(str(carbs) + ' calories from carbs' + '\n' + str(pro) + ' calories from protein' + '\n' + str(fats) + ' calories from fats')
        return total
    elif gender == 'female':
        carbs = sum / 100 * 60
        pro = sum / 100 * 30
        fats = sum / 100 * 20
        total = print(str(carbs) + ' calories from carbs' + '\n' + str(pro) + ' calories from protein' + '\n' + str(fats) + ' calories from fats')
        return total
    else:
        print('enter gender first')
