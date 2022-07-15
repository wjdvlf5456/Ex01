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



