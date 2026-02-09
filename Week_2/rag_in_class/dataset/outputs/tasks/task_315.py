def find_Max_Len_Even(input_string):
    string_length = len(input_string)
    current_index = 0
    current_length = 0
    maximum_length = 0
    start_index = -1

    while current_index < string_length:
        if input_string[current_index] == ' ':
            if current_length % 2 == 0:
                if maximum_length < current_length:
                    maximum_length = current_length
                    start_index = current_index - current_length
            current_length = 0
        else:
            current_length += 1
        current_index += 1

    if current_length % 2 == 0:
        if maximum_length < current_length:
            maximum_length = current_length
            start_index = current_index - current_length

    if start_index == -1:
        return "-1"
    return input_string[start_index: start_index + maximum_length]
