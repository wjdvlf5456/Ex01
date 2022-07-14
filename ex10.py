from operator import le

str1 = "FirstString"
str2 = "SecondString"

print(str1 + str2)  #print(str1 + 10) --> 문자열만 가능
print(str1 * 3)
print(str1 + str(10))
print(str1[5])
print(str1[-1])
print(str1[2:5])    #[이상:미만]
print(str1[1:9:3])  #[이상:미만:증가]
print(str1[:9])     #[:미만]
print(len(str1))    #len(str) --> 문자열의 길이

print(str1[:])
print(str1[::3])    #Fstn으로 출력됨
print(str1[-3])

name = "우영우"
name = "우영후"
name2 = name[:-1:]

print(name)     #우영후
print(name2)    #우영
