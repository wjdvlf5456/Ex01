#upper,lower

s='I Like Python. I Like Java Also'
print(s.upper())                    #모든 글자를 대문자로 변환
print(s.lower())                    #모든 글자를 소문자로 변환
print(s.swapcase())                 #소문자는 대문자, 대문자는 소문자로 변환
print(s.capitalize())               #첫 글자만 대문자
print(s*3)
print(s+s)

#검색관련
print(s.find("Like"))
print(s.find("Like",5))             #5번째 자리부터 "Like"란 문자를 찾았을 때 나오는 "Like"의 자리
print(s.find("Like",5,40))          #s.find(찾을 문자, 시작 Index, 끝 Index)
print(s.find('JS'))                 #찾는 값이 없으면 -1을 반환한다.
print(s.rfind('a'))                 #rfind는 우측 맨 끝부터 문자를 찾는다.

print(s.index("th"))                #index(str형) 이 몇뻔재에 있는지 찾아주는 함수이다. 값이 없으면 -1이 아니라 오류가 난다.

print(s.startswith("I Like"))       #입력한 값으로 시작하는지 확인 후 True or False 반환
print(s.startswith("I Like",2))     #입력한 숫자부터 입력한 문자로 시작하는지 확인

print(s.endswith("Also"))           #입력한 문자로 끝나는지 확인
print(s.endswith('Java', 0 , 26))   #endswith(끝나는문자, 문자열의시작, 문자열의끝)

s = '    spam and ham     '
print(s.strip())                    #공백제거
print(s.rstrip())                   #우측 공백 제거
print(s.lstrip())                   #좌측 공백 제거

s='<><abc><><defg><><>'
print(s.strip('<>'))                #출력결과: abc><><defg

s = 'Hello Java Java java'
print(s.replace( 'Java', 'Python')) #(교체할 문자, 교체 후 문자)

s = 'king and queen'
print(s.center(60))                 #s.center(공백포함하여 글자길이)
print(s.center(60, '-'))            #양 옆에 우측에 있는 글자를 추가
print(s.ljust(60, '-'))             #우측에 추가    s는 좌측에 위치
print(s.rjust(60, '-'))             #좌측에 추가    s는 우측에 위치

print('1234'.isdigit())             #전부 숫자인지 판별
print('abcd'.isalpha())             #전부 문자인지 판별

print('1234'.isalpha())             #isalpha()는 문자이면 True이니 '1234'일 때 False 출력
print('abcd'.isdigit())             #isdight()는 숫자이면 True이니 'abcd'일 때 False 출력

print('abcd'.islower())             #전부 소문자인지 판별
print('ABCD'.isupper())             #전부 대문자인지 판별

print('\n\n'.isspace())             #공백으로만 이루어졌는지 판별
print(' '.isspace())
print(''.isspace())                 #''는 공백이 아니라 아예 값이 없어서 False를 출력한다.