def bubble_sort(x: list):
    for size in reversed(range(len(x))):
        for i in range(size):
            if x[i] > x[i+1]:
                x[i], x[i+1] = x[i+1], x[i]
    return x

if __name__ == "__main__":
    print(bubble_sort([4,5,2,6,9,7,3,1]))