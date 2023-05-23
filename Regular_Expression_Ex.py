import re  #정규표현식 라이브러리 삽입

#전화번호 추출하기
inhatc_num = "인하공업전문대학 : 032-870-2114"

regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  #\d : 모든 숫자
matchobj = regex.search(inhatc_num)
tc_num = matchobj.group()
print(tc_num)

#문자클래스
#adcd라는 정규표현식 패턴 생성
pattern = "[abcd]"
re_pattern = re.compile(pattern)

text = "inhatc_bigdata"
#text에서 pattern에 해당되는 문자 리턴받아 return_pattern에 저장
return_pattern = re_pattern.findall(text)
print(return_pattern)

#'|' 사용
text = "Regular, Expression, big, data"
text_pattern = "Regular|data"
re_pattern = re.compile(text_pattern)

return_pattern = re_pattern.findall(text)
print(return_pattern)
