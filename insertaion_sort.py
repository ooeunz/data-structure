def insertation_sort(arr: list):
    for end in range(1, len(arr)):
        for i in range(end, 0, -1):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
    return arr

if __name__ == "__main__":
    print(insertation_sort([4,5,2,6,9,7,3,1]))