def insertion_sort(x: list):
    for size in range(1, len(x)):
        for i in range(size, 0, -1):
            if x[i-1] > x[i]:
                x[i-1], x[i] = x[i], x[i-1]
    return x

if __name__ == "__main__":
    print(insertion_sort([4,5,2,6,9,7,3,1]))