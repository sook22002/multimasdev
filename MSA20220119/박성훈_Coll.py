# 1번

grade = {"국어":95, "영어":90, "수학":80, "과학":50}

sum = 0
for value in grade.values():
    sum = sum + value

average = sum / len(grade)

# 2번

setData3 = {i for i in range(1, 101) if i%3 == 0}
setData5 = {i for i in range(1, 101) if i%5 == 0}

resultData1 = setData3 & setData5
resultData2 = setData3 | setData5

# 3번
listData1 = [i for i in range(7, -9, -2)]
for i in range(len(listData1)):
    print(listData1[i])

#4번
tupleData = tuple(listData1)

temp = 0
