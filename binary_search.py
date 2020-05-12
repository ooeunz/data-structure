def binary_search(target: int, data: list):
    data.sort()
    start, end = 0, len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return mid
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return None

if __name__ == "__main__":
    lst = [i for i in range(11)]
    target = 1

    idx = binary_search(target, lst)

    if idx:
        print(lst[idx])
    else:
        print('찾으시는 타겟 {}이 없습니다.'.format(target))