class RangeError(ValueError): pass        
class IntError(ValueError): pass
class leapYearError(ValueError):pass

def to_leap_year(year):
    if isinstance(year, str):
        raise leapYearError('No str!')
    if not isinstance(year, int): 
        raise IntError('Non-int can not convert!') 
    if not year:
        raise leapYearError('No input!')
    if not(0 < year):
        raise RangeError('Out of range (must be between 1...3999)') 
    return find_leap_year(year)

def find_leap_year(year):
    if(year %4 == 0 and year %100 != 0 or year %400 == 0):
        return("is a leap year")
    else:
        return("is not a leap year")

if __name__ == '__main__':
    leapYear = int(input('Find leap year: '))
    print('{0} {1}'.format(leapYear ,to_leap_year(leapYear)))