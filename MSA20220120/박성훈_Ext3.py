student1 = {"국어":95, "영어":90, "수학":80, "과학":50}
student2 = {"국어":100, "영어":50, "수학":90, "과학":90}
student3 = {"국어":99, "영어":60, "수학":100, "과학":40}
student4 = {"국어":55, "영어":80, "수학":80, "과학":60}

allStudent = [student1, student2, student3, student4]

sumList = []
averageList = []
allSum = 0
allaverage = 0
cnt = 0

while(cnt < 4):
    sumData = 0
    average = 0
    for value in iter(allStudent[cnt].values()):
        sumData = sumData + value

    average = sumData / len(allStudent[cnt])

    sumList.append(sumData)
    averageList.append(average)

    cnt = cnt + 1

allSum = sum(sumList)  # Ext2에서 해당 부분의 for문 대신 sum 매서드 사용

allaverage = sum(averageList)

allaverage = allaverage / len(allStudent)


temp = 0
# 전체합 1219
# 전체평균 76.1875
