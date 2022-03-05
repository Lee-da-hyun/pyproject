jumsu_1 = {100, 99, 88, 77}
jumsu_2 = {90, 99, 88, 66}

#두 학기 내내 동일한 성적인 점수는? 과목수는?
result = jumsu_2 & jumsu_1
print(result)
print(len(result))

#두 학기 동안 내가 획득한 전체 점수목록은?
result3 = jumsu_2.union(jumsu_1)
print(result3)

#정렬하고 싶어요
result33 = list(result3) #list()한 결과 비파괴형 함수
print(type(result3))
print(type(result33))
result33.sort() #void, 파괴형
print(result33)
result33.reverse()
print(result33)
#---파괴형 비파괴형 함수가 있으니 확인해가면서해,,,

#1학기 성적에 음악점수가 50점 추가
jumsu_1.add(50)
print(jumsu_1)

#2학기 성적에 음악77, 컴푸터100점 추가
jumsu_2.update({77,100})
print(jumsu_2)

#1학기성적 모두 삭제
jumsu_1.clear()
print(jumsu_1)