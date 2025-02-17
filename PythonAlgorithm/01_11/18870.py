# 1. 리스트를 중복 제거후 정렬하기
# 2. 필요한 값을 비교후 순서를 출력하기

# def sort_remove_duplicates(arr):
#     if len(arr) <= 1:
#         return arr
    
#     pivot = arr[len(arr) // 2]
#     left = []  # pivot보다 작은 값을 저장
#     right = []  # pivot보다 큰 값을 저장

#     # arr의 각 요소를 반복하며 pivot 기준으로 분리
#     for x in arr:
#         if x < pivot:
#             left.append(x)
#         elif x > pivot:
#             right.append(x)
#     # 중복 제거: pivot을 한 번만 포함
#     return sort_remove_duplicates(left) + [pivot] + sort_remove_duplicates(right)

# def find_indices(list1, list2):
#     indices = []
#     for item in list2:
#         if item in list1:
#             indices.append(list1.index(item))
#         else:
#             return '잘못됐어'
#     return indices

# list_num = int(input())
# find_list = list(map(int, input().split()))
# if(len(find_list) != list_num):
#     print('잘못 입력했어요')
# else:
#     result_list = sort_remove_duplicates(find_list)
#     result = find_indices(result_list, find_list)
#     print(" ".join(map(str, result)))



def sort_remove_duplicates(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = []
    right = []

    for x in arr:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
    # 중복 제거
    return sort_remove_duplicates(left) + [pivot] + sort_remove_duplicates(right)

def find_indices(sorted_list, list2):
    # 정렬된 리스트 list1의 값과 인덱스를 매핑
    index_map = {}
    for idx, value in enumerate(sorted_list):
        index_map[value] = idx  # value을 키로, idx를 값으로 저장
    
    # 원래 리스트 list2의 각 값에 대해 정렬된 리스트에서의 인덱스 찾기
    indices = []
    for item in list2:
        indices.append(index_map[item])  # item의 인덱스를 찾아서 결과 리스트에 추가
    
    return indices


def main():
    # 사용자 입력
    list_num = int(input())
    find_list = list(map(int, input().split()))

    if len(find_list) != list_num:
        print('잘못 입력했어요')
    else:
        sorted_list = sort_remove_duplicates(find_list)  # 중복 제거 및 정렬
        result = find_indices(sorted_list, find_list)  # 정렬된 리스트에서 원래 리스트 값의 인덱스 찾기
        print(" ".join(map(str, result)))


main()