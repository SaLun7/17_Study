import pandas as pd
import numpy as np

data = {    
    '이름': ['김철수', '이영희', '박민수', '최지우'],
    '나이': [20, 21, 22, 20],
    '성별': ['남', '여', '남', '여'],
    '수학': [90, 85, 70, 100],
    '영어': [85, 95, 75, 90]
}

# 1. df 라는 이름의 데이터프레임을 만들어 주세요
df = pd.DataFrame(data)

# 2. 생성된 데이터프레임의 상위 2개 행만 출력하세요.
print(df.iloc[0:2])
print(df.head(2))

# 3. 데이터프레임의 요약 정보(컬럼명, 데이터 타입 )을 확인하세요
print(df.info())
print(df.columns)
print(df.dtypes)

# 4. '이름' 컬럼을 인덱스로 설정하세요. (기존 df를 수정)
df = pd.DataFrame(data, index=df["이름"])
df = df.drop("이름", axis=1)

# df  = df.set_index("이름")

# 5. loc을 사용하여 '이영희'의 '수학' 점수와 '영어' 점수만 추출하세요.
print(df.loc["이영희", ["수학", "영어"]])

# 6. iloc을 사용하여 첫 번째 행부터 두 번째 행까지, 그리고 2번째 열(수학)부터 마지막 열까지 슬라이싱하세요.
print(df.iloc[0:2, 2:])



data = {
    '이름': ['김철수', '이영희', '박민수', '최지우'],
    '나이': [20, 21, 22, 20],
    '성별': ['남', '여', '남', '여'],
    '수학': [90, 85, 70, 100],
    '영어': [85, 95, 75, 90]
}

# 1. 위 데이터로 시리즈 객체 sr을 만들어주세요
sr = pd.Series(data)

# 2. 시리즈의 인덱스 배열과 데이터값 배열을 각각 추출하여 화면에 출력하세요.
print(sr.index)
print(sr.values)


list_data = ["2010-01-02", 3.14, "ABC", 100, True]

# 3. 위 데이터를 시리즈 객체로 만들어 주세요
sr = pd.Series(list_data)

# 4. 데이터 타입을 출력헤보세요
print(sr.dtype)


tup_data = ("영인", "2010-05-01", "여", True)
index_labels = ["이름", "생년월일", "성별", "학생여부"]

# 5. 위 데이터를 시리즈객체로 생성해주세요. 
sr = pd.Series(tup_data, index = index_labels)

# 6. 해당 시리즈의 원소 개수, 형상(shape), 차원을 출력해주세요 
print(sr.size, sr.shape, sr.ndim)

# 7. 위치 기반(정수)으로 첫 번째 원소를 안전하게 조회하는 코드를 작성하세요. (iloc 활용)
print(sr.iloc[0])

# 8. 라벨 '이름'으로 원소를 조회하는 코드를 작성하세요.
print(sr["이름"])

# 9. 위치 인덱스 번호 리스트를 활용하여 '생년월일'과 '성별'을 가져오세요. (iloc 권장)
print(sr.iloc[1:3])
print(sr.iloc[[1, 2]])

# 10. 라벨 이름 리스트를 활용하여 '생년월일'과 '성별'을 가져오세요.
print(sr[["생년월일", "성별"]])

# ---
# 11. 아무 데이터도 전달하지 않은 기본형 빈 시리즈를 생성하세요.
sr = pd.Series()

# 12. 스칼라 값 5와 인덱스 ["a", "b", "c"]를 사용하여 시리즈를 생성하고 출력하세요.
sr = pd.Series(5, index=["a", "b", "c"])
print(sr)



list1 = [1, 2, 3, 4, 5]
list2 = [
    [1, 2, 3], 
    [4, 5, 6]
]
# 1. 아래 주어진 리스트 데이터를 활용하여 각각 1차원 배열 arr1과 2차원 배열 arr2를 생성하고 타입을 출력하세요.
arr1 = np.array(list1)
arr2 = np.array(list2)
print(type(arr1))
print(arr1.dtype)
print(type(arr2))
print(arr2.dtype)

# 2. 모든 원소가 0.으로 채워진 크기 5짜리 1차원 배열 zeros 생성
zeros = np.zeros(5)

# 3. 모든 원소가 1.으로 채워진 크기 2행 3열의 2차원 배열 ones 생성
ones = np.ones((2,3))

# 4. 1부터 시작하여 2씩 증가하며 10 미만인 정수로 구성된 배열 range_arr 생성
range_arr = np.arange(1, 10, 2)



arr3 = np.array([
    [[1, 2],
     [3, 4]], 
    [[5, 6],
     [7, 8]]
])
# 5. 배열 속성(dtype, shape, ndim, size) 출력해주세요
print(arr3.dtype, arr3.shape, arr3.ndim, arr3.size)


arr_base = np.array([1, 2, 3, 4, 5, 6])

# 6. 위 1차원 배열을 2차원 배열로 변경해주세요 
reshaped = arr_base.reshape((2, 3))

# 7. 배열의 데이터 타입을 실수형(float)으로 변경하여 float_arr에 저장하세요.
print(arr_base.dtype)
print(arr_base.astype(float))
print(arr_base.dtype)


arr_2d = np.array([
    [1, 2, 3], 
    [4, 5, 6]
])

# 8. ravel을 사용해 1차원 배열로 평탄화하여 출력하세요.
print(arr_2d.ravel())

# 9. flatten을 사용해 1차원 배열로 평탄화하여 출력하세요.
print(arr_2d.flatten())

# 10. 축을 바꾸어 2행3열 -> 3행 2열로 만들어주세요 
print(arr_2d.transpose())
print(arr_2d.T)


arr_x = np.array([5, 3, 3])
arr_y = np.array([1, 2, 6])

# 11. arr_x와 arr_y의 요소별 합(+)과 요소별 곱(*)을 각각 계산해 출력하세요.
print(arr_x + arr_y)
print(arr_x * arr_y)

# 12. arr_x가 arr_y보다 큰지 여부를 비교하는 비교 연산 결과를 출력하세요.
print(arr_x > arr_y)

# 13. arr_x에 단일 스칼라 값 2를 곱하여 모든 요소가 2배가 되도록 출력하세요.
print(arr_x * 2)


data = np.array([1, 2, 3, 4, 5])

# 14. data 배열에서 2보다 큰 원소들만 추출하세요.
cond = data > 2
print(data[cond])

# 15. data 배열에서 2보다 크면서 동시에 5보다 작은 원소들만 추출하세요. (비트 연산자 & 활용)
cond = (data > 2) & (data < 5)
print(data[cond])


stats_arr = np.array([1, 2, 3, 4])

# 16. 합계, 평균, 분산, 표준편차, 중앙값을 구하세요 
print(stats_arr.sum())
np.sum(stats_arr)
print(stats_arr.mean())
np.mean(stats_arr)
print(stats_arr.var())
np.var(stats_arr)
print(stats_arr.std())
np.std(stats_arr)

np.median(stats_arr)