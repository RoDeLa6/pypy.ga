# i, j 입력
i = int(input())
j = int(input())

# 1행 1열의 값
result = 1

# i행 1열의 값
for x in range(i-1):
    # 컴퓨터는 0부터 센다는 걸 잊지 말자고요!
    result = result + (2 + x)

# i행 j열의 값
for y in range(j-1):
    result = result + i + y

print(result)

"""
     1 |  2 |  4 |  7 | 11 | ...
     3 |  5 |  8 | 12 | ...
     6 |  9 | 13 | ...
    10 | 14 | ...
    15 | ...
    ...
    
    표에서 "1행 n열"의 값은 1 → 2 → 4 → 7 → 11 → ... 로, 증가하는 변화폭이 1부터 시작해서 1씩 커집니다.
    "2행 n열"의 값은 3 → 5 → 8 → 12 → ... 로, 변화폭이 2부터 시작해서 1씩 커집니다.
    이에 따라 i행은 처음 더해지는 수가 i이고, 1씩 커지며 증가합니다.
    
    마찬가지로 "n행 1열"의 값 또한 1 → 3 → 6 → 10 → 15 → .... 로 증가하는 변화폭이 2부터 시작하여 1씩 커집니다.
    모두 종합하여 "i행 1열"의 값을 구한 다음, "i행 j열"의 값을 구하면 원하는 값을 얻을 수 있습니다. 
    
    물론 "1행 j열"을 먼저 구하고, "i행 j열"을 구해도 순서만 바뀐 것이니 상관은 없습니다.
"""
