student1 = {"국어":95, "영어":90, "수학":80, "과학":50}
student2 = {"국어":100, "영어":50, "수학":90, "과학":90}
student3 = {"국어":99, "영어":60, "수학":100, "과학":40}
student4 = {"국어":55, "영어":80, "수학":80, "과학":60}

def getGrade(student):
    sum = 0
    average = 0
    for value in student.values():
        sum = sum + value

    average = sum / len(student)

    return sum, average

sum1, average1 = getGrade(student1)
sum2, average2 = getGrade(student2)
sum3, average3 = getGrade(student3)
sum4, average4 = getGrade(student4)

allSum = (sum1 + sum2 + sum3 + sum4)
allAverage = (average1 + average2 + average3 + average4) / 4

temp = 0
