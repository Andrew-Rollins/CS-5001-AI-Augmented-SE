def upper_ctr(input_string):
    uppercase_count = 0
    for char in input_string:
        if char >= 'A' and char <= 'Z':
            uppercase_count += 1
    return uppercase_count
