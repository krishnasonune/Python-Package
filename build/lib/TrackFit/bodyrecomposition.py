def bodyRecomposition_calories(weight,height,age,gender):
    if gender == 'male':
        sum = 10*weight + 6.25 * height - 5 * age + 5
        procar = sum/100*40
        fats= sum/100*20
        total = print(str(procar) + ' calories from carbs' + '\n' + str(procar) + ' calories from protein' + '\n' + str(fats) + ' calories from fats')
        return total
    elif gender == 'female':
        sum = 10 * weight + 6.25 * height - 5 * age - 161
        procar = sum / 100 * 40
        fats = sum / 100 * 20
        total = print(str(procar) + ' calories from carbs'+ '\n' + str(procar) + ' calories from protein'+ '\n' +str(fats) + ' calories from fats')
        return total
    else:
        print('enter gender first')
