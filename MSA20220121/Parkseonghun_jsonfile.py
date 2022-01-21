try:
    chageFile = open("Datalab\\mydata.json", "rb")
    tempData = json.load(chageFile)
    resultData1 = tempData["name"]
    resultData2 = tempData["age"]
    resultData3 = tempData["address"]
    resultData4 = tempData["email"]
    resultData5 = tempData["empcheck"]
except Exception as ex:
    error = str(ex)
    print("오류:" + error)
else:
    chageFile.close()

jsonData1 = {
    "empid" : 12345678,
    "name" : "홍길동",
    "info" : [
        {"date1" : "2022-01-21", "home": "서울시"},
        {"dep" : "개발", "email": "aaa@aaa.co.kr"}
    ]
}

try:
    changeFile = open("Datalab\\mydata2.json", "w")
    json.dump(jsonData1, changeFile)
except Exception as ex:
    error = str(ex)
    print("오류: " + error)

else:
    chageFile.close()
    
try:
    changeFile =open("Datalab\\mydata3.json", "w", encoding="utf-8")
    json.dump(jsonData1, changeFile, ensure_ascii=False)
except Exception as ex:
    error = str(ex)
    print("오류: " + error)
else:
    changeFile.close
    
try:
    changeFile =open("Datalab\\mydata4.json", "w")
    json.dump(jsonData1, changeFile, ensure_ascii=False, indent=4)
except Exception as ex:
    error = str(ex)
    print("오류: " + error)
else:
    changeFile.close
    
try:
    changeFile = open("Datalab\\mydata5.json", "w", encoding="utf-8")
    json.dump(jsonData1, changeFile, ensure_ascii=False, indent=4)
except Exception as ex:
    error = str(ex)
    print("오류: " + error)
else:
    changeFile.close()

#디버깅 변수 선언함
temp = 0
