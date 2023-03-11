# 자연수 n 입력
n = int(input())

# i는 0부터 8까지 반복
for i in range(9):
    # n은 입력받은 수, i+1은 1부터 9까지 반복
    # 문자와 숫자는 더할 수 없으므로, 숫자를 문자로 바꿔서 한 줄로 합치기 (면접에서는 그냥 숫자만 출력하면 되었음)
    print(str(n) + "x" + str(i+1) + " = " + str(n*(i+1)))
