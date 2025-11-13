
def split_before_each_uppercases(formula):

    import re
    parts = re.findall('[A-Z][^A-Z]*', formula)
    return parts

def split_at_first_digit(formula):
    
    import re
    match = re.search(r'(.*?)(\d.*)', formula)
    
    if match:
        return list(match.groups())
    else:
        return [formula, ""]


def split_chem_formula(formula):
    import re
    return re.findall(r'([A-Z][a-z]?\d*)', formula)
