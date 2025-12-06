def get_first_recurring_character(input: list):

    occurence = {}  # this can be set, since set are hash tables too: `occurence = set()`
    for ch in input:
        if ch in occurence:
            return ch
        else:
            occurence[ch] = 1  # if set(), simply: occurence.add(ch)
    return None


input_list = [2, 1, 3]
output = get_first_recurring_character(input_list)

print(output)
