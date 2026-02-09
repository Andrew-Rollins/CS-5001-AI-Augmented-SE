def frequency_Of_Largest(n, arr):
    max_value = arr[0]
    count = 1
    for i in range(1, n):
        if arr[i] > max_value:
            max_value = arr[i]
            count = 1
        elif arr[i] == max_value:
            count += 1
    return count
