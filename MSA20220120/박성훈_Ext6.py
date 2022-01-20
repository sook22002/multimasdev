student1 = {"국어":95, "영어":90, "수학":80, "과학":50}
student2 = {"국어":100, "영어":50, "수학":90, "과학":90}
student3 = {"국어":99, "영어":60, "수학":100, "과학":40}
student4 = {"국어":55, "영어":80, "수학":80, "과학":60}

tupleData1 = tuple(student1.values())
tupleData2 = tuple(student2.values())
tupleData3 = tuple(student3.values())
tupleData4 = tuple(student4.values())

allData = list(tupleData1 + tupleData2 + tupleData3 + tupleData4)

sumData1 = 0
sumData2 = 0
sumData3 = 0
sumData4 = 0
i = 0
#Ext5의 for문을 while로 변경
while i < len(allData):
    if 0 <= i < 4:
        sumData1 = sumData1 + allData[i]
    elif 4 <= i < 8:
        sumData2 = sumData2 + allData[i]
    elif 8 <= i < 12:
        sumData3 = sumData3 + allData[i]
    else:
        sumData4 = sumData4 + allData[i]
        
    i = i + 1  

allSum = sum(allData)
allAverage = allSum / len(allData)


temp = 0
