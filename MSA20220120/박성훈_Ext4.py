student1 = {"국어":95, "영어":90, "수학":80, "과학":50}
student2 = {"국어":100, "영어":50, "수학":90, "과학":90}
student3 = {"국어":99, "영어":60, "수학":100, "과학":40}
student4 = {"국어":55, "영어":80, "수학":80, "과학":60}

def getList(student):
    listData = list(iter(student.values()))
    return listData

listStudent1 = getList(student1)
listStudent2 = getList(student2)
listStudent3 = getList(student3)
listStudent4 = getList(student4)

sumData1 = sum(listStudent1)
sumData2 = sum(listStudent2)
sumData3 = sum(listStudent3)
sumData4 = sum(listStudent4)

averageData1 = sumData1 / 4
averageData2 = sumData2 / 4
averageData3 = sumData3 / 4
averageData4 = sumData4 / 4

allSum  = sumData1 + sumData2 + sumData3 + sumData4
allAverage = (averageData1 + averageData2 + averageData3 + averageData4) / 4

temp = 0
