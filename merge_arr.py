def merge_sort(x: list):
    if len(x) < 2:
        return x
    
    mid = len(x) // 2
    low_arr = merge_sort(x[:mid])
    high_arr = merge_sort(x[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
        
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]

    return merged_arr

if __name__ == "__main__":
    print(merge_sort([4,5,2,6,9,7,3,1]))