# 전체 학생들의 과목별 총 합 점수와 평균을 구하는 프로그램

student1 = {"국어":95, "영어":90, "수학":80, "과학":50}
student2 = {"국어":100, "영어":50, "수학":90, "과학":90}
student3 = {"국어":99, "영어":60, "수학":100, "과학":40}
student4 = {"국어":55, "영어":80, "수학":80, "과학":60}

korean = []
mathmatic = []
english = []
science = []

def getData(student):
    for key, value in student.items():
        if key == "국어":
            korean.append(value)
        elif key == "영어":
            english.append(value)
        elif key == "수학":
            mathmatic.append(value)
        elif key == "과학":
            science.append(value)

if __name__ == '__main__':
    getData(student1)
    getData(student2)
    getData(student3)
    getData(student4)
    
    sum_k = sum(korean)
    average_k = sum_k / len(korean)
    sum_e = sum(english)
    average_e = sum_e / len(english)
    sum_m = sum(mathmatic)
    average_m = sum_m / len(mathmatic)
    sum_s = sum(science)
    average_s = sum_s / len(science)

    temp = 0
