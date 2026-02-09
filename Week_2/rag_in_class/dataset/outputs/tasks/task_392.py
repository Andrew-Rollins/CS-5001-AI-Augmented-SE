def get_max_sum(n):
    result = [0, 1]
    for i in range(2, n + 1):
        result.append(max(i, result[i // 2] + result[i // 3] + result[i // 4] + result[i // 5]))
    return result[n]
