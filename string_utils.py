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


def split_before_each_uppercases(formula):
    # Initialize start, end, and the result list
    start = 0
    end = 1
    split_formula = []

    # Loop from the second character onward
    for ch in formula[1:]:
        # If an uppercase letter is found, slice and update
        if ch.isupper():
            split_formula.append(formula[start:end])
            start = end
        end += 1

    # Append the final piece after the loop
    split_formula.append(formula[start:end])

    return split_formula

