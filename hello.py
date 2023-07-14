def sum(a,b):
    result = a + b 
    return result
print(sum(1,2))

def say():
    return 'hi'
print(say())

def sums(a,b):
    print("%d,%d의 합은 %d입니다." %(a,b,a+b))
print(sums(1,2))

my = [1,2,3]
print(my.pop())

def sum_many(*args):
    sum = 0
    for i in args : 
        sum = sum + i
    return sum
print(sum_many(1,2,3))

#**kwargs = 키워드 파라미터 출력 

f = open("새 파일" , "w ",encoding="utf-8")

lines = f.readlines()
#readline = 리스트형식파일을 하나씩 읽는다(ex :1번째 줄입니다)
#readlines = 리스트형식파일에 있는 모든라인을 읽는다.close()써야함 대신 with 쓰면 안써도됨
#read = 통채로 읽는거
# 'w'(write) = 파일 읽기(ex : 메모장)
# 'r'(read) = 파일을 읽어 data변수에 저장
# 'a' = 파일 이어쓰기

for line in lines : 
     print(line)

f.close()

#class 함수반복안해도됨
