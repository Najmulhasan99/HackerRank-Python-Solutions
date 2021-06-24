#python 2

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    Narr= sorted(list(set(arr)))
print(Narr[-2])
