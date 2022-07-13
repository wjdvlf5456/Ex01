#정수형

a = 101
print(a,type(a))

#앞에 0b 가 붙으면 그 숫자는 이진수로 인식한다.
b = 0b101   #2진수
print(b,type(b))

#8진수
c= 0o101
print(c)

#16진수
d = 0x101
print(d)

#10진수 -> 2진수,8진수,16진수
print(bin(5))
print(oct(65))
print(hex(257))

#파이썬에서는 long형이 없고 int형이 된다.
e = 2**1024
print(e,type(e))