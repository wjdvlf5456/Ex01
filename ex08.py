#확장 연산자
x=2
x=x*5
print(x)

x-=3
print(x)

x**=3
print(x)

print("==============================")

#관계 연산자
print(1>3)
print(2<4)
print(4<=5)
print(4>=5)
print(6==9)
print(6!=9)

print("==============================")

a=10
b=20
c=a
d=10
print(a==b)
print(a is b)
print(a is c)
print(a is d)

print(id(a))
print(id(b))
print(id(c))
print(id(d))    #컴퓨터가 먼제 이전에 같은 값이 있는지 확인 후 같은 값이 존재하면 같은 주소를 부여한다.


print(True and True)

print("==============================")
print(abs(-3))      # 절대값으로
print(int(3.1415))  # 정수형으로
print(float(3))     # 실수형으로
print(complex(3))   # 복소수형으로
print(pow(2, 10))   # 승수 계산


