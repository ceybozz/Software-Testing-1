import re

class RangeError(ValueError): pass        
class IntError(ValueError): pass
class RomanError(ValueError): pass

romanNumerals = (('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), ('XC', 90), 
('L', 50), ('XL', 40), ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)) 

# R = roman numbers input
def from_roman(R):
    roman_numeral = re.compile('''^ # beginning of string
                M{0,4} # thousands - 0 to 4 Ms
                (CM|CD|D?C{0,3}) # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 Cs),
                # or 500-800 (D, followed by 0 to 3 Cs)
                (XC|XL|L?X{0,3}) # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 Xs),
                # or 50-80 (L, followed by 0 to 3 Xs)
                (IX|IV|V?I{0,3}) # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 Is),
                # or 5-8 (V, followed by 0 to 3 Is)
                $ # end of string
                ''', re.VERBOSE)
                
    # Convert Roman to int
    if not R: 
        raise RomanError('No Input!')
    if not isinstance(R, str): 
        raise RomanError('Non-integers can not be converted!') 
    if not roman_numeral.search(R):
        raise RomanError('Invalid Roman Number: {0}!'.format(R))
    result = 0
    index = 0
    for numeral, integer in romanNumerals:
        while R[index:index + len(numeral)] == numeral: 
            result += integer
            index += len(numeral)
    return result

# I = Int input
def  to_roman(I) :
    # Convert int to Roman
    if not isinstance(I, int): 
        raise IntError('Non-integers can not be converted!') 
    if isinstance(I, str):
        raise IntError('Str can not be convert!')
    if not(0 < I < 4000):
        raise RangeError('Int out of range (must be 1..3999)!')
    result = ''
    for numeral, integer in romanNumerals:
        while I >= integer: 
            result += numeral
            I -= integer
    return result
    
if __name__ == '__main__':
    intInput = int(input('Convert int to roman: ')) 
    print('Roman is: {0}'.format(to_roman(intInput)))

    romanInput = input('Convert roman to int: ')
    print('Int is : {0}'.format(from_roman(romanInput))) 