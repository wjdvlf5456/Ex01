do = 23
str1 = "현재온도는 %d도 입니다." % 23
print(str1)

str2 = "오늘은 %s년 %d월 %d일 입니다." % ("2022", 7, 15)
print(str2)

age = 33
print("제 나이는 %d살입니다." % age)

area = 76.483
print("원의 넓이는 %f 입니다." % area)

print("제 나이는 %10d살 입니다." % age)
print("제 나이는 %-10d살 입니다." % age)
print("원의 넓이는  %5.4f 입니다." % area)

print("수수료는 %d%% 입니다." % 20)

print("======================================")
age = 35

print("제 나이는 {0}살입니다.".format(43))
print("제 나이는 {0}살입니다.".format("스무"))
print("제 나이는 {0}살입니다.".format(age))
print("오늘은 {0}년 {1}월 {2}일 입니다.".format("2022", 7, 5.5))
# 순서 상관없이 변수명만 똑같으면 값을 넣을 수 있다.
print("오늘은 {year}년 {month}월 {day}일 입니다.".format(year="2022", day=5.5, month=7))

print("오늘은 {0:>10}년 {1:<10}월 {2:^10}일 입니다.".format("2022",3,2))


