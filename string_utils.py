def split_at_first_digit(formula):
    digit_location = 1
    for ch in formula[1:]:
        if ch.isdigit():
            break
        digit_location += 1
    if digit_location == len(formula):
        return formula, 1
    prefix = formula[:digit_location]
    number = int(formula[digit_location:])

    return prefix, number

def split_before_each_uppercases(formula):
    # Handle empty string
    if formula == "":
        return []

    start = 0
    end = 1
    split_formula = []

    # Loop through characters starting at index 1
    for ch in formula[1:]:
        if ch.isupper():
            split_formula.append(formula[start:end])
            start = end
        end += 1

    # Append the final section
    split_formula.append(formula[start:end])

    return split_formula
