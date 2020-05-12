def quick_sort(arr: list):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    less_arr, equal_arr, big_arr = [], [], []

    for num in arr:
        if num < pivot:
            less_arr.append(num)
        elif num > pivot:
            big_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(less_arr) + equal_arr + quick_sort(big_arr)

if __name__ == "__main__":
    print(quick_sort([4,5,2,6,9,7,3,1]))