"""
dictionary는 key:value 쌍으로 이루어진 데이터를 저장하는 자료구조
"""

my_dict = {'name':"홍길동", 'age':20}
#my_dict = dict()
print(type(my_dict))
#dict를 key로 값을 조회
print(my_dict['name'])
#dict에 새로운 key와 value를 추가
my_dict['addr'] = '충주'

print(my_dict.get('name1'))
result = my_dict.get('name1')
if result :
    print(result)
else :
    print("해당 내용이 존재하지 않습니다.")

if 'name1' in my_dict:
    print("name1 key가 있습니다.")
else :
    print("name1 key가 없습니다.")

for key, value in my_dict.items():
    print(key, value)
