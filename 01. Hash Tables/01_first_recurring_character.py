def get_first_recurring_character(input: list):

    occurence = {}
    for ch in input:
        if ch in occurence:
            return ch
        else:
            occurence[ch] = 1
    return None


input_list = [2, 1, 3]
output = get_first_recurring_character(input_list)

print(output)
