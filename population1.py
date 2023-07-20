# Q. 도시 3개 선택하여 인구의 합계가 500만에 가장 가까운 조합과 그 인구를 구하시오
# 부산광역시 : 3416918, 인천광역시 : 2925967, 대구광역시 : 2453041, 대전광역시 : 1525849, 광주광역시 : 1496172 
# 경기도 수원시 : 1193894, 울산광역시 : 1147037, 경기도 고양시 : 1068641, 경기도 용인시 : 1061440, 경상남도 창원시 : 1044579
# 경기도 성남시 : 942649, 충청남도 청주시 : 840047, 경기도 부천시 : 828947, 경기도 화성시 : 818760, 경기도 남양주시 : 702545
# 전라북도 전주시 : 654963, 충청남도 천안시 : 652845, 경기도 안산시 : 650599, 경기도 안양시 : 565392, 경상남도 김해시 : 542713
# 경기도 평택시 : 521642, 경상북도 포항시 : 506494, 제주시 : 489202

# 목표값
goal = 5000000

# 각 도시의 인구
pref = [
    3416918, 2925967, 2453041, 1525849, 1496172, 1193894, 1147037, 
    1068641, 1061440, 1044579, 942649, 840047, 828947, 818760, 
    702545, 654963, 952845, 650599, 565392, 542713, 521642, 
    506494, 489202
]

# 500만 명에 가까운 인구 수
min_total = 0

# 두 지역의 인구 수를 저장하는 임시 변수
local_temp = 0

# 지역 1~3 인구 수의 인덱스를 저장
local_index1 = 0
local_index2 = 0
local_index3 = 0

def search(total, pos):
    global min_total, local_temp, local_index1, local_index2, local_index3
    if pos >= len(pref):
        return
    if total < goal:
        if abs(goal - (total + pref[pos])) < abs(goal - min_total):
            min_total = total + pref[pos]
            local_temp = total
            local_index1 = pos
        search(total + pref[pos], pos + 1)
        search(total, pos + 1)
    
    for local_index2 in range(22):
        for local_index3 in range(22):
            if local_temp - pref[local_index2] == pref[local_index3]:
                break
        break

search(0, 0)
print(min_total)
print(pref[local_index1])
print(pref[local_index2])
print(pref[local_index3])