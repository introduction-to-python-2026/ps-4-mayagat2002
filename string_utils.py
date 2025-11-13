
def split_before_each_uppercases(formula):
 sentence =[]
    for letter in formula:
       if letter == upercase:
        sentence.append " "
    sentence.append"letter"
    return sentence

def split_at_first_digit(formula):
    word ="" 
    form = []
    for letter in formula:
        word.append(letter)
     if(letter == digit) :
      
    else:
        return [formula, ""]


def split_chem_formula(formula):
    import re
    return re.findall(r'([A-Z][a-z]?\d*)', formula)
