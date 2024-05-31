def binary_search(data, low, high, x):
    while low <= high: #
        mid = low + (high - low) // 2 # 5 + (8-5) // 2 ==> 6
        if data[mid] == x: # 2 != 4
            return mid
        if data[low] <= data[mid]: # 1 <= 2
            if data[low] <= x < data[mid]: # 1  <= 4 < 2
                high = mid - 1
            else: # 6 + 1 = 7
                low = mid + 1
        else:
            if data[mid] < x <= data[high]: # 1 < 4 < 5
                low = mid + 1 # 5
            else:
                high = mid - 1 # 8
    return -1

data = [6, 7, 8, 10, 1, 2, 3, 4, 5]
elem = 4

data = [3, 4, 5, 6, 7, 8, 10, 1, 2]
elem = 2

print(binary_search(data=data, low=0, high=8, x=elem))