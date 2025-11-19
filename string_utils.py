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
    # Test 5: Empty string → return empty list
    if formula == "":
        return []

    # Test 2: No uppercase letters → return the entire string
    if not any(ch.isupper() for ch in formula):
        return [formula]

    start = 0
    end = 1
    split_formula = []

    # Loop through characters starting at index 1
    for ch in formula[1:]:
        # If uppercase, slice and reset start
        if ch.isupper():
            split_formula.append(formula[start:end])
            start = end
        end += 1

    # Append the last part
    split_formula.append(formula[start:end])
