def split_at_first_digit(formula):
    digit_location = 1
    for ch in formula[1:]:
        if ch.isdigit():
            break
        digit_location += 1
    if digit_location == len(formula):
        return formula, 1
    prefix = formula[:digit_location]
    number = formula[digit_location:]

    return prefix, number
