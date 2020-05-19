def select_sort(x: list):
    for size in reversed(range(len(x))):
        maxv = 0
        for i in range(1, size+1):
            if x[i] > x[maxv]:
                maxv = i
        x[maxv], x[size] = x[size], x[maxv]
    return x

if __name__ == "__main__":
    print(select_sort([4,5,2,6,9,7,3,1]))